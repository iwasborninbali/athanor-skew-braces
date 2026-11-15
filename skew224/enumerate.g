# skew224: classical-brace star-associativity audit, GAP 4.12 / YangBaxter 0.10.7.
# Load this file with Read("skew224/enumerate.g"); from the repository root.
# Set SKEW224_MIN and SKEW224_MAX before Read to override [1..868].
# Only orders satisfying IsBraceImplemented(n) are enumerated.

if LoadPackage("cryst") <> true then
    Error("Could not load cryst");
fi;
if LoadPackage("polycyclic") <> true then
    Error("Could not load polycyclic");
fi;
if LoadPackage("YangBaxter") <> true then
    Error("Could not load YangBaxter");
fi;

if not IsBound(SKEW224_MIN) then SKEW224_MIN := 1; fi;
if not IsBound(SKEW224_MAX) then SKEW224_MAX := 868; fi;
if not IsInt(SKEW224_MIN) or not IsInt(SKEW224_MAX)
   or SKEW224_MIN < 1 or SKEW224_MAX < SKEW224_MIN then
    Error("Require integers 1 <= SKEW224_MIN <= SKEW224_MAX");
fi;

# A and M are synchronized lists of the *same* brace elements, as stored
# by YangBaxter's SkewbraceAList / SkewbraceMList attributes. Internally
# both group laws are permutation multiplication, but M is in its own
# coordinate system. Sort each permutation list and map products back to
# the additive coordinates using binary searches, never Position on a
# size-n brace list in an n^2 inner loop.
SKEW224_Tables := function(br)
    local n, rawA, rawM, A, M, mcoord, mToA, addT, circT, neg, starT;
    n := Size(br);
    rawA := SkewbraceAList(br);
    rawM := SkewbraceMList(br);
    if Length(rawA) <> n or Length(rawM) <> n then
        Error("YangBaxter coordinate lists have wrong length");
    fi;
    A := SortedList(rawA);
    M := SortedList(rawM);
    mcoord := List(A, a -> rawM[Position(rawA, a)]);
    mToA := List(M, m -> PositionSorted(A, rawA[Position(rawM, m)]));
    addT := List([1..n], i -> List([1..n],
        j -> PositionSorted(A, A[i] * A[j])));
    circT := List([1..n], i -> List([1..n],
        j -> mToA[PositionSorted(M, mcoord[i] * mcoord[j])]));
    neg := List([1..n], i -> PositionSorted(A, Inverse(A[i])));
    # star(a,b) = -a + (a circle b) - b, in classical additive notation.
    starT := List([1..n], i -> List([1..n],
        j -> addT[addT[neg[i]][circT[i][j]]][neg[j]]));
    return rec(A := A, add := addT, circ := circT, star := starT);
end;

# All checks here are EXACT, not heuristic. For every fixed x, the map
# y |-> x*y is additive in y. It suffices to compare additive homomorphisms
# on generators in the LAST slot. For the right law one checks the first
# slot at every x and each additive generator g; these translations
# generate all of (B,+). This reduces the triple tests to n^2*d and n*d^2.
SKEW224_Analyze := function(br)
    local t, n, grp, gens, gg, i, j, g, h, associative, twoSided,
          addT, starT;
    n := Size(br);
    grp := UnderlyingAdditiveGroup(br);
    if not IsAbelian(grp) or not IsClassical(br) then
        Error("SmallBrace returned a nonclassical brace");
    fi;
    t := SKEW224_Tables(br);
    addT := t.add;
    starT := t.star;
    gens := List(SmallGeneratingSet(grp),
                 g -> PositionSorted(t.A, g));
    if n > 1 and Length(gens) = 0 then
        Error("Nontrivial additive group has no generators");
    fi;

    # Independently check the left distributive law, using generator steps.
    for i in [1..n] do
        for j in [1..n] do
            for g in gens do
                if starT[i][addT[j][g]] <>
                   addT[starT[i][j]][starT[i][g]] then
                    Error("Left distributivity failed (database/API issue)");
                fi;
            od;
        od;
    od;

    associative := true;
    for i in [1..n] do
        if not associative then break; fi;
        for j in [1..n] do
            if not associative then break; fi;
            for g in gens do
                if starT[starT[i][j]][g] <>
                   starT[i][starT[j][g]] then
                    associative := false;
                    break;
                fi;
            od;
        od;
    od;

    twoSided := true;
    for i in [1..n] do
        if not twoSided then break; fi;
        for g in gens do
            if not twoSided then break; fi;
            for h in gens do
                if starT[addT[i][g]][h] <>
                   addT[starT[i][h]][starT[g][h]] then
                    twoSided := false;
                    break;
                fi;
            od;
        od;
    od;
    return rec(assoc := associative, twoSided := twoSided,
               tables := t);
end;

# Convert GAP's 1-based indices to zero-based indices with the additive
# identity at index 0, so JSON tables are a self-contained certificate.
SKEW224_PrintWitnessTables := function(n, k, tables)
    local z, order, newPos, addOut, circOut, i;
    z := PositionSorted(tables.A, ());
    order := Concatenation([z], Filtered([1..n], i -> i <> z));
    newPos := List([1..n], i -> Position(order, i) - 1);
    addOut := List(order, i -> List(order,
        j -> newPos[tables.add[i][j]]));
    circOut := List(order, i -> List(order,
        j -> newPos[tables.circ[i][j]]));
    Print("WITNESS_JSON {\"n\":", n, ",\"k\":", k,
          ",\"additive_table\":", addOut,
          ",\"multiplicative_table\":", circOut, "}\n");
end;

SKEW224_Run := function(lo, hi)
    local n, total, k, br, r, a, t, bad, d, native, cached;
    Print("SKEW224 GAP YangBaxter classical; range=", lo, "..", hi,
          "; format=ORDER n count associative_star two_sided assoc_not_two_sided\n");
    for n in [lo..hi] do
        if not IsBraceImplemented(n) then
            Print("SKIP ", n, " not-implemented\n");
        else
            total := NrSmallBraces(n);
            # YangBaxter deliberately Unbinds BRACES[n] after each
            # SmallBrace(n,k) for n>15. Retain this one order's decoded
            # catalogue in memory, or large orders would reread and parse
            # the same megabyte-sized file once per brace.
            if IsBound(BRACES[n]) then
                cached := BRACES[n];
            else
                cached := fail;  # prime / p^2 / Burnside special case
            fi;
            Print("BEGIN ", n, " ", total, "\n");
            a := 0;
            t := 0;
            bad := 0;
            for k in [1..total] do
                br := SmallBrace(n, k);
                if n > 15 and cached <> fail then
                    BRACES[n] := cached;
                fi;
                r := SKEW224_Analyze(br);
                if r.assoc then a := a + 1; fi;
                if r.twoSided then t := t + 1; fi;
                if r.assoc and not r.twoSided then
                    bad := bad + 1;
                    d := StructureDescription(UnderlyingAdditiveGroup(br));
                    Print("WITNESS n=", n, " k=", k, " additive=", d, "\n");
                    if n <= 64 then
                        SKEW224_PrintWitnessTables(n, k, r.tables);
                    fi;
                fi;
                # YangBaxter's IsTwoSided is cubic; use it on small
                # examples, one representative through n=32, and ALL
                # putative counterexamples as a second API cross-check.
                if n <= 16 or (n <= 32 and k = 1) or
                   (r.assoc and not r.twoSided) then
                    native := IsTwoSided(br);
                    if native <> r.twoSided then
                        Error("IsTwoSided disagrees with table test");
                    fi;
                fi;
                if k mod 100 = 0 then
                    Print("PROGRESS ", n, " ", k, "/", total, "\n");
                fi;
            od;
            Print("ORDER ", n, " ", total, " ", a, " ", t, " ", bad, "\n");
            if n > 15 and cached <> fail then
                Unbind(BRACES[n]);
            fi;
        fi;
    od;
    Print("COMPLETE range=", lo, "..", hi, "\n");
end;

SKEW224_Run(SKEW224_MIN, SKEW224_MAX);
