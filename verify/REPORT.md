# Independent verification — Guarnieri–Vendramin, *Skew braces and the Yang–Baxter equation*

Verification date: **2026-11-15**. Status: **finite, reproducible partial verification**, not a general proof or an audit of the authors' source code.

## Scope

Primary source: L. Guarnieri and L. Vendramin, *Skew braces and the Yang–Baxter equation*, *Mathematics of Computation* **86** (2017), 2519–2534, [arXiv:1511.03171v3](https://arxiv.org/pdf/1511.03171), especially printed pp. 3–14. Also consulted L. Vendramin, *Problems on skew left braces*, *Advances in Group Theory and Applications* **7** (2019), 15–37 ([PDF](https://www.advgrouptheory.com/journal/Volumes/7/Vendramin%20-%20Problems%20on%20skew%20left%20braces.pdf)); the later article is context, **not** a source of computational evidence here.

**Conventions:** `c(n)` counts skew left braces, `b(n)` classical/left braces (abelian additive group), `t(n)` two-sided braces, all **up to brace isomorphism**. The paper uses a multiplicative notation for the first group; in this program `G` is the additive/first group, and `circle[a,b] = a * lambda[a](b)`.

**Method H:** from scratch, build a multiplication table for each isomorphism type of group `G`, enumerate its automorphisms by images of generating sets, enumerate *all* subgroups of `G ⋊ Aut(G)` for which projection to `G` is injective, and classify order-`|G|` regular subgroups under the action of `Aut(G)`. Subgroup generation is exhaustive: every subgroup has a generating set, and each step adds one element not yet in the subgroup; for a regular subgroup its intermediate subgroups necessarily have injective projection and orders dividing `|G|`. Pruning by automorphism conjugacy is sound because it preserves both extensibility and regularity.

**Method D (independent):** for each additive group `G` and **each** possible multiplicative group `K` of the same order, enumerate all bijections `K → G` preserving the identity; transport `K`'s multiplication; directly test whether all maps `lambda_a(b) = a^{-1}*(a circle b)` are additive automorphisms. Canonicalize the resulting brace tables under additive-group automorphisms. No holomorph-subgroup generation is used by this second method. Both methods independently construct the finite group automorphism sets; this is a shared input technique, not an independent check of the complete list of small groups.

The computation ran on Python **3.13.5**, Linux x86-64, standard library only. **No GAP, YangBaxter package or Magma was used.** The run covers complete groups of the following orders:

`1–15, 17–23, 25–26, 28–30` (**28 orders**). Direct method D independently covers `1–10` (**10 orders**). The script checks multiplicative associativity, brace compatibility and the right two-sided condition by direct Cayley-table substitution. On **every** H brace of orders `1–12`, it additionally exhaustively checks the paper's formula for `r` is bijective, left- and right-nondegenerate, obeys the Yang–Baxter braid equation on triples, and is involutive **if and only if** the additive group is abelian. For larger orders this last expensive test was deliberately not run.

## Findings

### Numerical claims — complete independent status inventory

**CONFIRMED over tested orders**: Table 5.1, printed p. 11: `c(n)` for `n = 1–15, 17–23, 25–26, 28–30` agrees **entry for entry**. The paper's complete Table 5.1 is transcribed below, in increasing `n` order (thirty positions); an asterisk denotes **NOT CHECKED** here:

```
n        1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
c(n)     1  1  1  4  1  6  1 47  4  6  1 38  1  6  1
n       16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
c(n)  1605* 1 49  1 43  8  6  1 855* 4  6 101*29  1 36
```

**CONFIRMED over the same 28 orders**: Table 5.3, printed p. 12: all tested `b(n)` entries match; the rest, including authors' question marks, are **NOT CHECKED**. Full inventory below (each row is twelve consecutive orders, starting at the given `n`):

```
n=  1:   1 1 1 4 1 2 1 27 4 2 1 10
n= 13:   1 2 1 357* 1 8 1 11 2 2 1 96*
n= 25:   4 2 37* 9 1 4 1 ? 1 2 1 46
n= 37:   1 2 2 106 1 6 1 9 4 2 1 1708
n= 49:   4 8 1 11 1 80 2 91 2 2 1 28
n= 61:   1 2 11 ? 1 4 1 11 1 4 1 489
n= 73:   1 2 5 9 1 6 1 1985 ? 2 1 34
n= 85:   1 2 1 90 1 16 1 9 2 2 1 ?
n= 97:   1 8 4 51 1 4 1 106 2 2 1 494
n=109:   1 6 2 1671 1 6 1 11 11 2 1 395
```

In that inventory, **only** orders in the tested set above are confirmed; all entries beyond 30 are **NOT CHECKED**, regardless of asterisks. A `?` is an unknown **in the 2016 paper**, not a zero. Explicitly, the authors left `b(32), b(64), b(81), b(96)` unknown (Problem 6.1).

**CONFIRMED over tested orders ≤ 24**: Table 5.5, printed p. 12, `t(n)` agrees for `n = 1–15, 17–23` (**22 orders**). `t(16), t(24)` were **NOT CHECKED**. Complete table:

```
n       1 2 3 4 5 6 7 8 9 10 11 12
 t(n)    1 1 1 4 1 1 1 22 4  1  1  4
n      13 14 15 16 17 18 19 20 21 22 23 24
 t(n)    1  1  1 221*1  4  1  4  1  1  1  22*
```

**CONFIRMED in finite samples**: Conjecture 6.6 (p. 13), `q(4m)=2` for odd `m>2`, verified independently at `m=3,5,7`, i.e. multiplicative dicyclic/quaternion groups of orders **12, 20, 28**. Isomorphism to `Q_(4m)` was checked by independently searching generator-image bijections for the computed circle group. Output: `QUAT 12 2`, `QUAT 20 2`, `QUAT 28 2`. This covers the *odd* branch for only three values, not the other residue classes or the full conjecture.

**CONFIRMED in finite samples**: Conjecture 6.2 (p. 13; the displayed formula says `m mod 4` although `p` is the quantified prime): from `b(20)=11` for `p=5` and `b(28)=9` for `p=7`. These are just two instances, not an independent proof or a check to `p=997`. The printed `m` appears to be a notation typo, not a counterexample.

**CONFIRMED for all enumerated braces through order 12**: Theorem 3.1 (p. 6), its nondegenerate Yang–Baxter solution and involutivity criterion, by exhaustive substitution. The tests include nonabelian additive groups; they are not confined to involutive solutions. All generated H representatives also satisfy Definition 1.1 (p. 3), Proposition 1.9's additive-automorphism test (p. 4), Corollary 1.10 (p. 4) and the bijective-cocycle identity for the identity bijection (Proposition 1.11, p. 5).

**CONFIRMED**: Example 1.3 (p. 3), for *every* group, by a complete direct argument: `a circle b=ab` gives the trivial brace; `a star b=ba` gives `lambda_a(b)=a^{-1}ba`, an inner automorphism, hence a brace. If an additive-group automorphism is also an isomorphism between these two circle laws, it yields `f(ab)=f(a)f(b)=f(b)f(a)` for all `a,b`, forcing commutativity. If the group is abelian, the two circle laws coincide. Thus they are isomorphic exactly when the group is abelian.

**CONFIRMED with a complete argument**: Theorem 4.2 and Proposition 4.3 (pp. 9–10), the holomorph classification. For a skew brace, the compatibility identity makes every `lambda_a` an automorphism of the first group and associativity yields `lambda_(a circle b)=lambda_a lambda_b`. Therefore `H={(a,lambda_a)}` is closed under holomorph multiplication, and projection `H→G` is bijective, so the action is regular. Conversely, let `H` be regular and write its unique element projecting to `a` as `(a,f_a)`. Define `a circle b=a f_a(b)`. Holomorph multiplication gives `(a,f_a)(b,f_b)=(a f_a(b),f_a f_b)`; hence `circle` is associative with identity and inverses as transported from `H`. Because `f_a` is an automorphism, `a circle (bc) = (a circle b)a^{-1}(a circle c)` follows immediately. Any `u∈Aut(G)` conjugates `(a,f_a)` to `(u(a),u f_a u^{-1})`, which precisely transports the circle law via `u`. Conversely, a brace isomorphism must preserve the first law, so lies in `Aut(G)` and performs that conjugation. This proves both directions of the isomorphism-orbit correspondence, and explains the enumeration.

**CONFIRMED**: The finite-group versions of Lemma 4.1 (p. 9), Algorithm 5.1 (p. 10) and Remark 5.2 (p. 10), by direct construction. The `H` log records counts per additive group; the `D` log records independently transported candidate bijections and accepted brace orbits. The `two_sided` check tests the *defining* right-distributive identity directly, rather than using Lemma 5.4 as a black box.

### Other checkable claims — explicitly scoped statuses

| Location | Claim | Status in this audit |
|---|---|---|
| Examples 1.4–1.6, p. 3 | Semidirect-product and exact-factorization brace constructions | **NOT CHECKED** in full generality; no standalone example-specific harness |
| Lemma 1.7 and Remark 1.8, p. 4 | Identities and inverse lambda formula | **FINITE CHECK** implicit for the constructed braces where the code uses the formulas; no separate universal proof |
| Proposition 1.9, Corollary 1.10 and Proposition 1.11, pp. 4–5 | Lambda/cocycle characterizations | **FINITE CHECK** through order 30 for lambda homomorphisms via subgroup construction; universal claims not independently reproved here |
| Example 2.2, Lemmas 2.3 and 2.5, pp. 5–6 | Ideals, quotients, socle | **NOT CHECKED** by independent exhaustive ideal enumeration |
| Corollary 3.3 and Examples 3.4–3.6, p. 7 | Restriction and explicit YBE examples | **NOT CHECKED** separately |
| Proposition 3.7, Theorems 3.8–3.9 and Corollary 3.10, pp. 8–9 | Braid conjugacy / structure-group reconstruction / finiteness | **NOT CHECKED** generally; no finite presentation or universal construction implemented |
| Lemma 5.4, pp. 11–12 | Alternative lambda criterion for two-sidedness | **NOT CHECKED** as written; two-sidedness verified from its defining identity |
| Tables 5.2 and 5.4, pp. 11–12 | Original Magma CPU timings | **NOT REPRODUCIBLE** as historical performance claims without original code and hardware; the present run reports its own elapsed time |
| Problem 6.1, p. 13 | `b(32), b(64), b(81), b(96)` | **NOT CHECKED** (original paper lists these as unknown) |
| Conjecture 6.3, p. 13 | `b(9p)` formula | **NOT CHECKED** independently (no tested order is `9p`, prime `p>3`) |
| Conjecture 6.4, p. 13 | `b(p²q)=4` for stated primes | **NOT CHECKED** independently; paper states this was proved elsewhere |
| Conjecture 6.6, p. 13 | Remaining odd `m` and all even `m`; authors' `m≤512` claim | **NOT CHECKED** beyond `m=3,5,7` |
| Question 6.7, p. 13 | Classification of possible additive groups for quaternion braces and author's `m≤512` observation | **PARTIAL**: tested odd `m=3,5,7`, counts only; not a full subgroup-type audit |
| Question 6.8, p. 14 | Counts by specified abelian additive group | **PARTIAL**: individual counts `quaternion_multiplicative` appear per group at `n=12,20,28` in the log; general question open here |
| Conjecture 6.9 and Table 6.1, p. 14 | Quaternion braces of order `2^k`, `k>4`, partition `1+6` | **NOT CHECKED** (orders ≥ 32) |
| Remark 6.10, p. 14 | Cyclic prime-power additive-group claims | **FINITE CHECK** for additive `C4,C8,C9,C25`; original cited theorems not reproved |

No **refuted mathematical claim** was found in the tested range. An editorial issue (the `m` in Conjecture 6.2) is not counted as a mathematical refutation.

## Evidence

Run exactly from the repository root:

```sh
python3 verify/verify.py --holomorph-max 30 --direct-max 10 \
  --orders 1-15,17-23,25-26,28-30 --seconds 1200 \
  > verify/replay.log 2>&1
# Compare ORDER lines, QUAT lines and FINISHED JSON to verify/run.log.
# Timing, platform details, and Python versions may vary.
grep -E '^(ORDER|QUAT|FINISHED)' verify/replay.log
sha256sum verify/verify.py verify/run.log
sha256sum -c verify/SHA256SUMS
```

`run.log` contains one `GROUP` record for every additive group, including `aut`, `partials`, `attempted`, total `braces`, `classical`, `two_sided`, optional `independent_D`, and optional `quaternion_multiplicative`. Each `ORDER` record is followed by `MATCH`, and every discrepancy or failed algebraic identity raises an assertion and terminates the process. The `FINISHED` record presents the final result set. Reported total wall time was about **30 seconds** in this environment (under the 30-minute CPU budget).

**SHA-256** (original computation files, not Git blob SHA-1):

```
1af2c8467c7fa0f0d8413d7eff43d836c879660d1d723b8ce45344b409329381  verify/verify.py
cf0e2a926af1cf1b2622a1027bae1ef4600283e79aed8280d6b7bb683a3be0e2  verify/run.log
```

Important limitation: the two counting paths share handcrafted group models and automorphism enumeration infrastructure. Method D does **not** reuse Method H's regular-subgroup enumeration. Full third-party GAP/YangBaxter replication was not possible here; no claim of such replication is made.

## Not covered

The excluded orders **16, 24, 27** are exactly the gaps within `1–30` in this run. For 16 and 27, elementary abelian groups have large automorphism groups; the generic holomorph-conjugation table is impractically large. For 24, this script does not contain an exhaustively vetted model list of all 15 groups of that order. The complete tables beyond 30, historical runtime measurements, and assertions in Section 6 for primes to 997, `m` to 512, or quaternion orders `2^k` for `k=5,…,9` are not independently confirmed. The 2019 problem list was consulted for scope, not exhaustively verified.

We do not claim that matching published numbers proves the group-model catalog is correct; small-order group classifications used to assemble models remain an explicit external mathematical input. Apart from the proofs reproduced above, finite algebraic tests do not prove the unrestricted theorems. The paper PDF was accessed and examined from its public arXiv URL; a local binary copy is **not** included because the container has no outbound network connectivity.

## Next steps

1. Replace the handcrafted group catalog with independently generated presentations or GAP SmallGroups, and check all isomorphism classes are present and pairwise inequivalent.
2. Implement a more scalable regular-subgroup orbit search for groups of orders 16, 24 and 27; then complete Table 5.1 through order 30, and extend Table 5.5 through order 24.
3. Add a standalone ideals/socle and Yang–Baxter reconstruction tester, and verify Lemma 5.4 against its exact lambda formula.
4. Install GAP with the public YangBaxter package in an environment with repository/package access and compare independent outputs; pursue quaternion orders `2^k` separately.
