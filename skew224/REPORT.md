# skew224 — classical star associativity versus two-sidedness

Athanor lab / 2026-11-15. **Status: priority resolved in the literature; computational replay NOT YET RUN on the guide's GAP VM.** No original mathematical discovery is claimed. This is a new reproducibility harness, not an assertion that P2.24 remains open.

## Question

Vendramin, *Problems on skew left braces*, *Advances in Group Theory and Applications* **7** (2019), Problem **2.24**, printed p. 26: for a classical left brace `(B,+,circ)`, with abelian `(B,+)`, does associativity of `a*b = lambda_a(b)-b = -a+(a circ b)-b` force the right brace law `(a+b) circ c = (a circ c)-c+(b circ c)`? This is equivalent to right distributivity `(a+b)*c=a*c+b*c`.

**Answer: YES, in every classical brace, with or without 2-torsion.** Ivan Lau, *An Associative Left Brace Is a Ring*, **Theorem 1.1**, arXiv:1811.04894 (first posted 12 November 2018; revised 22 December 2019), *Journal of Algebra and Its Applications* **19** (2020), no. 9, DOI [10.1142/S0219498820501790](https://doi.org/10.1142/S0219498820501790), proves exactly this. Its Corollary 1.2 identifies the resulting Jacobson radical ring. [Primary PDF, pp. 2 and 4–5](https://arxiv.org/pdf/1811.04894). Andrea Sciandra, *Associativity of the star-product of skew braces*, arXiv:2609.22995 (September 2026), also acknowledges the classical equivalence [abstract](https://arxiv.org/abs/2609.22995). In contrast, skew braces can have associative `*` without being two-sided: the `attack/` order-16 witness is nonclassical, so not a contradiction.

**All small prime-power cases:** for every prime `p`, every classical brace of order `p^2` or `p^3` (indeed of arbitrary finite or infinite order) with associative `*` is two-sided. Proof: these structures satisfy the hypotheses of Lau's Theorem 1.1, whose conclusion is exactly the defining right brace law; the left brace law already holds. Conversely, if two-sided, `*` is bilinear and `circ` is associative, so comparing the two expansions of `(a circ b) circ c = a circ (b circ c)` yields `(a*b)*c=a*(b*c)`; thus equivalence holds. This is a **corollary of the cited published theorem**, not a new independent proof of Lau's implication. No exhaustive computation is needed to settle `p^2` or `p^3`.

## Method

Files: `enumerate.g`, `check_witness.py`, this report and `SHA256SUMS`. Input is an inclusive integer interval given by GAP globals `SKEW224_MIN` and `SKEW224_MAX` (defaults **1..868**, increasing order); only `IsBraceImplemented(n)` orders are processed. **API caveat:** YangBaxter 0.10.7's `NrSmallBraces(n)` does **not** return `fail` for unsupported orders: its actual implementation throws a GAP error. Check `IsBraceImplemented(n)` first, then obtain `NrSmallBraces(n)` and loop over every `SmallBrace(n,k)`. This may also include prime, prime-square and coprime-`n,phi(n)` formula cases rather than on-disk catalogue files; no arbitrary bound `n<=150` is silently asserted as complete.

The program reads the package's synchronized `SkewbraceAList` and `SkewbraceMList` permutation coordinates, sorts each, maps between coordinates, and constructs the full addition, circle and star lookup tables. It checks `IsClassical` and abelianness of `UnderlyingAdditiveGroup`, verifies the left distributive law, then independently tests star associativity and right distributivity. It uses `IsTwoSided` as an explicit package cross-check on all braces of `n<=16`, on one representative of every order up to 32, and on **any putative counterexample**. The package's `IsTwoSided` is cubic, so using it on every brace would be unnecessarily expensive. For a witness, the additive structure is printed via `StructureDescription`. At `n<=64`, its full two Cayley tables are printed as an independently checkable zero-based `WITNESS_JSON` record, with additive identity index 0.

**Proof of the reduced tests.** For every classical *left* brace, the map `c -> a*c` is a homomorphism of the additive group for each fixed `a`. Therefore both functions `c -> (a*b)*c` and `c -> a*(b*c)` are additive, and agree everywhere if they agree on any generating set `G` of `(B,+)`. Testing all `(a,b)` and `c in G` thus **exactly** decides star associativity. Likewise, for each fixed `c`, the right law says `F_c(a+b)=F_c(a)+F_c(b)`, where `F_c(x)=x*c`. Once left distributivity is known, it suffices to check this with `c in G`. For such `c`, checking `F_c(x+g)=F_c(x)+F_c(g)` for every `x in B`, `g in G` implies the full law: any `b` is a sum of generators, including negative multiples represented by positive multiples in this finite group, and successive applications telescope. The left-law check itself uses the same generator-step argument. **These are exhaustive equivalences, not random samples.**

Per brace, precomputing three tables from sorted permutation coordinates uses `O(n^2 log n)` comparison/search operations, with memory `O(n^2)`; left-law and star-associativity tests cost at most `O(n^2 d)`, right-law `O(n d^2)`, where `d=|G|` is the size of a small additive generating set (usually much smaller than `n`). Both properties often fail early, and tests short-circuit. The native package cross-check has `O(n^3)` cost but is deliberately limited. **Catalogue performance caveat:** for `n>15`, YangBaxter unbinds `BRACES[n]` after constructing each brace. The script temporarily restores the one decoded order catalogue after each `SmallBrace(n,k)` and releases it after `ORDER`, avoiding repeated reading/parsing of e.g. the roughly 21 MB `Bsize32.g` source file. This trades RAM for speed. The GAP process is single-threaded; four VM cores do not automatically parallelize it.

The independent Python checker accepts `WITNESS_JSON` records and directly verifies: both sets of group axioms (including all triple associativity tests); abelian addition; left brace compatibility; associative star; and an explicit failure of right brace distributivity. It does not import GAP or trust any computed boolean. `NO_TABLE_WITNESSES` only means the input contains none and is **not** an independent proof of an exhaustive negative search.

## Exact command for the guide

Run from the repository root in the lab's **GAP 4.12** installation with **YangBaxter 0.10.7, cryst, polycyclic**, and Python 3, using only free/local tools:

```sh
set -o pipefail  # bash: propagate a failing GAP exit status through tee
printf 'SKEW224_MIN := 1;; SKEW224_MAX := 868;; Read("skew224/enumerate.g");; QUIT;\n' \
  | gap -q -b 2>&1 | tee skew224/run.log
python3 skew224/check_witness.py skew224/run.log | tee skew224/checker.log
sha256sum -c skew224/SHA256SUMS
```

To limit the range, change **only** the two integer literals in the `printf` expression, for example `SKEW224_MIN := 1;; SKEW224_MAX := 32;;`. **Important:** use Bash (or separately check GAP's exit status); without `pipefail`, `tee` can hide a GAP failure. An interrupted run still leaves every completed `ORDER` line trustworthy as an observed result, but no `COMPLETE` marker.

Output is line-oriented; no counts have been fabricated:

```
SKEW224 GAP YangBaxter classical; range=1..868; format=ORDER n count associative_star two_sided assoc_not_two_sided
BEGIN n number_of_braces
PROGRESS n k/number_of_braces           # after every 100 braces
ORDER n number_of_braces associative_star two_sided assoc_not_two_sided
SKIP n not-implemented                  # unsupported n; no zero count asserted
WITNESS n=n k=k additive=C2 x C2       # ONLY if such a brace occurs
WITNESS_JSON {"n":...,"k":...,"additive_table":[...],"multiplicative_table":[...]}
COMPLETE range=1..868                  # only if the range ends normally
```

`ORDER` gives the five requested fields, in increasing `n`; there is exactly one such line for each finished supported order. By Lau's theorem, the last field must be **0** for every order. An exception would indicate a code/API/data defect unless independently certified and reconciled with the theorem. The first two counters should be equal to each other mathematically, but their values require the actual run. `run.log` and `checker.log` are **guide-generated output**, not pushed/generated here; the checker can certify only an actual `WITNESS_JSON` record.

**Running-time estimate:** not benchmarked. On the 4-core VM, begin with `1..16`, then `1..32`; small orders should plausibly take seconds to minutes, whereas order 32 has **25,281** classical entries (published count) and a full `1..868` audit could take **hours or longer** depending on the actual database, permutation cost and available RAM. Do **not** treat this estimate as an execution result. The largest on-disk classical table in the published YangBaxter 0.10.7 tag is `Bsize32.g` (~21 MB); the largest implemented file order in that tagged tree is 168, but special constructed orders may be supported above that. Completion and elapsed wall time must be measured by the guide.

## Results — TO BE FILLED FROM THE GUIDE'S RUN

**NOT RUN here.** There is no `ORDER` transcript, verified witness table, result count, or performance measurement. The following statements are predictions from external mathematics, **not computed observations**: `associative_star = two_sided` and `assoc_not_two_sided = 0` for every genuinely classical brace. On completion, attach the guide's complete log, `grep '^ORDER ' skew224/run.log` output, Python checker output, elapsed time, package/version stamp, and SHA-256 of generated logs. Keep intermediate `BEGIN`/`PROGRESS` lines so partial coverage can be audited. Do not replace missing `ORDER` lines with zeros.

## Priority check

1. **Earlier experimental search:** A. Konovalov, A. Smoktunowicz, L. Vendramin, *On skew braces and their ideals*, online 22 December 2018; *Experimental Mathematics* **30** (2021), 95–104, §2.2, [arXiv:1804.04106](https://arxiv.org/abs/1804.04106), [DOI](https://doi.org/10.1080/10586458.2018.1492476). It reports checking its classical-brace database for associative-star non-two-sided examples, finding none, and names eight order-16 **skew** examples. The cited version describes 8,828 classical database entries; Lau's revised preprint mentions an earlier sample of 8,683, which may reflect a different snapshot and is not silently equated.
2. **General proof:** Ivan Lau, Theorem 1.1, [arXiv:1811.04894](https://arxiv.org/abs/1811.04894), first posted 12 November 2018, published 2020. This **fully settles the classical question without any 2-torsion caveat**; it takes absolute precedence over a finite enumeration.
3. **Recent explicit confirmation:** Andrea Sciandra, [arXiv:2609.22995](https://arxiv.org/abs/2609.22995), September 2026, states the same equivalence for classical braces and investigates skew variants. No originality is claimed for this observation.
4. **Internal lab:** `status/REPORT.md` incorrectly still labels row `2.24 / 26` O/U; `attack/REPORT.md` already records Lau's proof and reproduces an order-16 *skew* witness; `verify/` and `guide/2026-11-15-replays/` certify earlier finite tests. This branch does **not** modify their files, as requested; a separate status correction is warranted.

## Not covered

- No GAP run, full default-range enumeration, measured runtime or computed small-brace counts in this contribution; **the guide must run it**. No claimed counterexample or claim of a new theorem.
- The source package is a database and construction engine, **not an exhaustive classification for every order `<=868`**. Every `SKIP` means no package implementation, not a claim that braces do not exist. No proof of the catalogue's completeness or absence of duplicates beyond its own assertions.
- `IsTwoSided` native cross-check is deliberately not performed on every large brace; the independently justified generator test is performed on every processed brace. A large-order proposed witness has identifier and additive type but no Cayley tables if `n>64`, per request; independent witness verification would then require a separate export.
- The Python verifier checks supplied tables, **not** completeness of the list of `SmallBrace(n,k)` or the GAP computation's proper termination. Small-case theoretical conclusions cite Lau's published proof, not a new self-contained proof of his theorem. Skew (nonclassical) implications, infinite skew braces, and all unrelated 2019 problems are outside scope.
- No paid services, no pushes to `main`, no generated VM logs, and no circular self-hash in `SHA256SUMS`.
