# Skew braces: state of the art and ideas

**Athanor lab research memo — 2026-11-15**  
**Evidence policy:** claims below are either **L** (located in a primary paper, but not independently proved or recomputed), **C** (independently checked with the committed program, output, and separate checker), or **U** (unverified / no reliable closure established). A paper's assertion is not a new Athanor result. **S** = settled in the cited literature; **P** = partly addressed; **O** = still an open-ended question or no complete resolution located. Negative answers are marked S(negative).

## Scope

Primary sources actually inspected: L. Guarnieri and L. Vendramin, *Skew braces and the Yang–Baxter equation*, *Mathematics of Computation* **86** (2017), 2519–2534, [arXiv:1511.03171](https://arxiv.org/pdf/1511.03171), especially Algorithm 5.1, Table 5.3, §6 printed pp. 13–14 ([DOI](https://doi.org/10.1090/mcom/3161)); and L. Vendramin, *Problems on skew left braces*, *Advances in Group Theory and Applications* **7** (2019), 15–37, [publisher PDF](https://www.advgrouptheory.com/journal/Volumes/7/Vendramin%20-%20Problems%20on%20skew%20left%20braces.pdf), §2, Problems 2.1–2.50 ([arXiv:1807.06411](https://arxiv.org/abs/1807.06411); [DOI](https://doi.org/10.32037/agta-2019-003)).

Definitions and transfer mechanism: for the same set A, an additive group (A,+) and circle group (A,∘) form a skew left brace iff a∘(b+c) = a∘b−a+a∘c. Classical left braces additionally have abelian (A,+). The map λ_a(b)=−a+a∘b yields a regular subgroup of Hol(A,+) ≅ (A,+) ⋊ Aut(A,+). Conversely, each regular subgroup gives a skew brace; isomorphism classes for fixed additive A are the Aut(A)-conjugacy classes. The associated r_A(a,b)=(λ_a(b), λ_a(b)^{-1}_{∘}∘a∘b) is a non-degenerate YBE solution, involutive iff A is abelian. See [GV17 Proposition 1.11, Theorem 3.1, §4, Algorithm 5.1](https://arxiv.org/pdf/1511.03171) and [Byott–Ferri 2025, introduction p. 2](https://arxiv.org/pdf/2402.12547). Not every solution is just r_A for a finite brace without additional realization/reconstruction data.

**Quotation scope.** The request for verbatim reproduction of all 58 source items cannot be met wholesale here: the underlying papers are copyrighted. We give one short exact 2017 item and one short 2019 item; every other formulation is a faithful *paraphrase* with exact numbered location and a clickable original PDF for checking the verbatim wording. Mathematical formulas and counts are factual facts. The 2017 paper has eight numbered items in §6 (Problem 6.1, Conjectures 6.2–6.4 and 6.6, Questions 6.7–6.8, Conjecture 6.9). Definition 6.5 and Remark 6.10 are **not** open problems. Other introductory rhetorical questions have answers in the paper (e.g. §3), so are not counted as additional open problems.

## Findings

### 2017 source: every numbered question / conjecture

| Source item and exact location | Wording / mathematical content | 2026-11-15 status and evidence |
|---|---|---|
| **Problem 6.1**, §6.1, printed p. 13 | Verbatim: “Compute b(32), b(64), b(81) and b(96).” | **S–L.** Bardakov–Neshchadim–Yadav [BNY20, §3 Table 1](https://arxiv.org/pdf/1907.08978): b(32)=25,281, b(81)=804, b(96)=195,971. Ballester-Bolinches–Esteban-Romero–Pérez-Calabuig [BEP24, Theorem 1.1, Corollary 1.2](https://doi.org/10.1007/s11587-023-00772-2): b(64)=15,095,601, last additive-type contribution 10,326,821. |
| **Conjecture 6.2**, §6.1, p. 13 | For prime p>3, b(4p)=11 if p≡1 mod 4, and 9 if p≡3 mod 4. | **S–L**, Dietzel, [*Braces of order p²q*](https://arxiv.org/abs/1801.06911), especially introductory conjectures and Corollaries 3–4; published *J. Algebra Appl.* 20 (2021), 2150140. The original printed cases mistakenly write “m” instead of “p”. |
| **Conjecture 6.3**, §6.1, p. 13 | For prime p>3, b(9p)=14 (p≡1 mod 9); 4 (p≡2,5 mod 9); 11 (p≡4,7 mod 9). | **S–L**, same Dietzel paper. **Source omission:** the displayed 2017 conjecture does not specify p≡8 mod 9, which is possible for primes >3; Dietzel's classification supplies b(9p)=4 also for p≡8 mod 9. |
| **Conjecture 6.4**, §6.1, p. 13 | For primes p<q with q not congruent to 1 mod p, b(p²q)=4. | **Already settled in GV17 itself**, immediately after Conjecture 6.4: explicitly credits Agata Smoktunowicz [37]; later recovered/generalized by Dietzel [Corollaries 3–4](https://arxiv.org/abs/1801.06911). It should **not** be called still open in 2017. |
| **Conjecture 6.6**, §6.2, p. 13 | Let q(4m) count classical left braces with multiplicative generalized quaternion group Q4m, m>2. Predicted q=2 for m odd, 7 for m≡0 mod 8, 9 for m≡4 mod 8, 6 for m≡2 or 6 mod 8. | **S–L** by Byott–Ferri, [*J. Algebra* 665 (2025), 72–102, Theorem 13.1](https://arxiv.org/pdf/2402.12547); [journal DOI](https://doi.org/10.1016/j.jalgebra.2024.11.011). Rump 2020 earlier proved the large power-of-two case. |
| **Question 6.7**, §6.2, p. 13 | Determine which finite abelian additive groups occur in quaternion left braces. | **S–L** Byott–Ferri, [Theorem 13.1 and Table 2, p. 23 of arXiv version](https://arxiv.org/pdf/2402.12547), classification of all possible additive types. |
| **Question 6.8**, §6.2, p. 14 | For each candidate abelian A of order 4m, count quaternion braces having additive group A. | **S–L**, Byott–Ferri, [Table 2, p. 23](https://arxiv.org/pdf/2402.12547), per-additive-group counts. |
| **Conjecture 6.9**, §6.2, p. 14 | Exactly seven isomorphism classes of quaternion left braces of order 2^k for k>4. | **S–L** Rump, *Classification of the affine structures of generalized quaternion groups*, *J. Group Theory* **23** (2020), 847–869; see [Byott–Ferri 2025, p. 2 and Theorem 11.1](https://arxiv.org/pdf/2402.12547). Also follows from its Theorem 13.1. |

For quaternion additive types the published Table 2 is more reliable than extrapolating the five families guessed from the small 2017 data. E.g. for 2^k with k≥5, the additive groups C_(2^k) (one brace) and C_2×C_(2^(k−1)) (six) exhaust the seven classes; the exceptional orders 4, 8 and 16 are tabulated separately by Byott–Ferri. Beware of the order-8 exceptional convention Q8 vs generalized Q4m with m=2.

### Vendramin (2019): all 50 problems, mapped to later work

Locations are the **2019 journal's printed pages**, not the shorter arXiv preprint's displayed page numbering. Rephrasings here are summaries, not verbatim transcriptions. References [AMV22], [AB20], [AB22], [BF25], [NIL24], [DMFT26] and others are expanded in the evidence register.

| No. / page | Problem in paraphrase | 2026 status, scope, evidence |
|---|---|---|
| **2.1 / 18** | Explicitly describe free cycle sets. | **O/U.** No complete explicit construction verified in this survey; do not confuse with free braces or free commutative skew braces [LET25]. |
| **2.2 / 18–19** | Construct all small cycle sets. | **P–L.** [AMV22] counts non-degenerate involutive solutions at sizes 9 (321,931) and 10 (4,895,272); no claim about all larger sizes. |
| **2.3 / 19** | Enumerate small square-free cycle sets. | **P–L.** [AMV22], finite-size constraint enumerations and subclasses; remains parametrically open. |
| **2.4 / 19** | Enumerate small indecomposable cycle sets. | **P–L.** [AMV22] and Dietzel–Properzi–Trappeniers [DPT25] classify prime-square cardinalities; general task remains. |
| **2.5 / 19** | Asymptotics for numbers of cycle sets. | **O/U.** No matching general asymptotic theorem established in the checked sources. |
| **2.6 / 19** | Enumerate small injective non-involutive YBE solutions. | **P–L.** [AMV22] gives all non-involutive solutions of size 8 (422,449,480), containing the injective examples; separate injective-only counts not verified. |
| **2.7 / 19** | Enumerate all small non-degenerate YBE solutions. | **P–L.** [AMV22], all non-involutive size 8, involutive sizes 9 and 10; larger sizes not covered. |
| **2.8 / 20** | Classify finite simple involutive solutions. | **P–L.** Cedó–Okniński [CO25] gives new infinite families and criteria for simplicity, not a universal classification. |
| **2.9 / 20** | Construct small simple involutive examples. | **P–L.** Examples/families exist [CO25]; no complete small-size enumeration verified. |
| **2.10 / 20** | Detect simplicity via the structure left brace G(X,r). | **P–L.** [CO25] gives structural criteria for particular families, not a general criterion. |
| **2.11 / 20** | Characterize torsion in the multiplicative structure group of a solution. | **O/U.** Source already notes non-involutive torsion examples; no iff criterion located. |
| **2.12 / 20** | Construct free (skew) left braces. | **P–L.** Letourmy [LET25] explicitly constructs the *commutative* free skew brace; that is weaker than arbitrary free skew braces. Other universal constructions not audited. |
| **2.13 / 22** | Construct all classical braces of order 32. | **S–L.** [BNY20, Table 1] b(32)=25,281, via improved holomorph algorithm. |
| **2.14 / 22** | Classify skew braces of prime-power order p^n. | **P–L.** Cases n≤3 classified in sources cited by Vendramin (Nejabati Zenouz, *J. Algebra* 2019); broader n still open; b(64) completed [BEP24]. |
| **2.15 / 22** | Verbatim: “Let p and q be different prime numbers. Construct all skew left braces of size pq.” | **S–L.** Acri–Bonatto [AB20], *Commun. Algebra* 48 (2020), 1872–1881, classifies all; for p>q, 1 if p not≡1 mod q, 2q+2 otherwise. |
| **2.16 / 23** | Classify all skew braces of order p²q, distinct primes. | **S–L.** Acri–Bonatto [AB22], Part I abelian type (*Algebra Colloq.* 29(2) (2022), 297–320), Part II non-abelian type (*J. Algebra Appl.* 21 (2022), 2250062); Part II explicitly completes enumeration including q=2 previously studied by Crespo. |
| **2.17 / 23** | Estimate counts b(n), s(n) asymptotically. | **O/U.** [BNY20] provides many finite tables and conjectures, not a general asymptotic. |
| **2.18 / 23** | Compute automorphism groups of p-power skew braces. | **P–L.** p³ Heisenberg-type cases from Nejabati Zenouz (Vendramin references [52–53]); general p^n open. |
| **2.19 / 23–24** | Produce counterexamples to Gateva-Ivanova's square-free claim. | **S for existence, P for requested new examples.** The 2019 paper already names counterexamples and open variants. [AMV22] permits richer searches. |
| **2.20 / 24** | Find Gateva-Ivanova pairs (brace plus restricted solution). | **O/U.** Potential small-database search; no complete independent witness verified here. |
| **2.21 / 25** | Whether structure group of injective non-involutive solution is left-orderable. | **O/U.** No definitive general theorem/counterexample located. |
| **2.22 / 25** | Unique-product property for irretractable involutive solutions. | **O/U.** No definitive answer established here. |
| **2.23 / 25** | Understand non-involutive multipermutation solutions. | **P–L.** Work on retractability and p-nilpotency, e.g. Acri–Lutowski–Vendramin (*IJAC* 30 (2020), 91–115), but broad research programme. |
| **2.24 / 26** | For classical left brace, does associativity of star imply two-sidedness? | **O/U.** Vendramin records yes when additive group has no 2-torsion and a negative answer for *skew* braces; those do NOT resolve the stated classical even-torsion case. |
| **2.25 / 26** | Classify finite simple skew braces. | **P–L.** Multiple new families (e.g. [CO25]), no full classification. |
| **2.26 / 26** | Develop skew-brace representation theory. | **P/U.** Open-ended programme; no comprehensive classification asserted. |
| **2.27 / 26** | Classify skew braces with multiplicative group infinite cyclic. | **O/U.** The nontrivial dihedral-additive example in Vendramin 2019 is not evidence of uniqueness. |
| **2.28 / 27** | Prove quaternion count q(4m) formula. | **S–L.** [BF25, Theorem 13.1]. |
| **2.29 / 27** | Which abelian additive groups support quaternion braces? | **S–L.** [BF25, Table 2]. |
| **2.30 / 27** | Seven quaternion braces at order 2^k for k>4? | **S–L.** Rump 2020, extended by [BF25]. |
| **2.31 / 28** | Minimal order of soluble non-IYB finite group. | **O/U.** Bachiller established existence; minimality not verified. |
| **2.32 / 28** | Every class-two finite nilpotent group an IYB group? | **S–L, pre-2019.** Yes: Ault–Watters (*Amer. Math. Monthly* 80 (1973), 48–52), class-two group as adjoint of finite nilpotent ring; see [AGTA 4 (2017), p. 134 discussion](https://www.advgrouptheory.com/journal/Volumes/4/ADV%20Perspectives%20in%20Group%20Theory%20-%20an%20open%20space.pdf). |
| **2.33 / 28** | Every class-two finite nilpotent group multiplicative group of a two-sided brace? | **S–L, pre-2019**, same Ault–Watters finite nilpotent ring construction gives *two-sided* brace. |
| **2.34 / 28** | Which finite nilpotent groups are multiplicative groups of left/two-sided braces? | **P–L.** Includes class two as above; [CO25-IYB] extends sufficient conditions but not full classification. |
| **2.35 / 28** | Non-IYB finite group with all Sylow subgroups IYB? | **S–L (very recent preprint).** Lü Gong, [arXiv:2611.13792](https://arxiv.org/abs/2611.13792), submitted 10 November 2026, constructs even supersoluble and odd-order supersoluble examples. No independent verification of pre-Lie trace proof; not peer reviewed. |
| **2.36 / 28** | Study knot invariants from skew left braces. | **P–L.** General programme with biquandle invariants; no finite completion criterion. |
| **2.37 / 28** | Strengthen such knot invariants via brace homology. | **O/U.** No definitive construction/comparison verified. |
| **2.38 / 29** | Does every finite IYB group admit a right-nilpotent left-brace realization? | **O/U.** No general proof found in checked literature. |
| **2.39 / 29** | Simple two-sided skew braces of nilpotent additive type? | **O/U.** No verified general answer or example. |
| **2.40 / 29** | Must finite prime skew brace of nilpotent type be simple? | **S(negative), already 2019.** Cedó–Jespers–Okniński's prime non-simple *left* brace also refutes the skew-brace claim; Vendramin 2019 directly says this after Problem 2.41. |
| **2.41 / 29** | Must every finite prime left brace be simple? | **S(negative), already 2019.** Same counterexample, cited in Vendramin §2 as [27, §5]. |
| **2.42 / 29** | Exist prime two-sided skew braces of nilpotent additive type? | **O/U.** Distinct from the refuted 2.40–2.41; no example verified. |
| **2.43 / 29** | Finite strongly-nil skew brace ⇒ strongly nilpotent? | **S(negative)–L.** [NIL24] builds finite strong-nil brace not right nilpotent. |
| **2.44 / 30** | Finite right-nil skew brace ⇒ right nilpotent? | **S(negative)–L.** Same [NIL24] example: strong-nil implies right-nil, hence counters both; see definitions at Vendramin pp. 29–30. |
| **2.45 / 30** | A meaningful skew-brace analogue of Köthe's conjecture? | **O/U**, open-ended formulation; no canonical finalized conjecture verified. |
| **2.46 / 30** | Soluble additive, insoluble multiplicative skew brace? | **S(affirmative)–L, preprint.** Di Matteo–Ferrara–Trombetti [DMFT26], July 2026, example with multiplicative quotient PSL₂(7), counterexample to Byott's conjecture. No machine-readable multiplication table independently checked here. |
| **2.47 / 30** | Insoluble additive, nilpotent multiplicative skew brace? | **P/U.** For **finite** groups impossible by standard finite factorization/solubility restrictions; original problem did not impose finiteness, and the infinite case was not resolved in this review. |
| **2.48 / 30** | Does left-orderability of multiplicative group imply left-orderable additive group? | **S(negative), already 2019.** Vendramin reports Nasybullov counterexample and a published independent one in his reference [28]. |
| **2.49 / 31** | Does every indecomposable involutive solution arise from a one-generated brace orbit in the specified form? | **O/U.** No definitive proof/counterexample verified. |
| **2.50 / 31** | Develop dynamical extensions for linear cycle sets. | **P/U.** Broad construction problem; no universal completed theory established here. |

**Caution about P2.35:** the 2026 preprint was released only five days before this memo's cutoff. This is a literature-status report, not independent validation of that highly recent argument.

### Small-order data: what is actually known (and what is not)

- In [GV17, Table 5.3, printed p. 12](https://arxiv.org/pdf/1511.03171), b(32), b(64), b(81), b(96) were missing, not zero.
- [BNY20, §3 Table 1, printed p. 4](https://arxiv.org/pdf/1907.08978): **b(32)=25,281**, **s(32)=1,223,061**; **b(81)=804**, **s(81)=8,436**; **b(96)=195,971**, but **s(96)=?** in that table. **b(64)=?** and **s(64)=?** there. The article also gives more numbers with exceptions up to 868; exceptions must not be silently converted to complete counts.
- [BEP24, Theorem 1.1 and Corollary 1.2](https://doi.org/10.1007/s11587-023-00772-2) closes **b(64)=15,095,601** with additive C₂²×C₄² contribution **10,326,821**; their [public data repository](https://github.com/RamonEstebanRomero/braces64) provides archives and a GAP reconstruction method (not downloaded or checked here).
- The GAP [YangBaxter package, v0.10.7, released 2025-07-14](https://gap-packages.github.io/YangBaxter/) says its database covers (skew) braces through size 150 *with exceptions* and cycle sets below size 9. Do not infer a complete order-64 skew-brace dataset from that tagline; consult the package's exact coverage and README. In the GAP manual [SmallSkewbrace](https://gap-packages.github.io/YangBaxter/doc/chap1.html) and [SmallBrace](https://gap-packages.github.io/YangBaxter/doc/chap1.html) access catalogued examples. GAP could not be run in the present container.
- [AMV22, *Math. Comp.* 91 (2022), 1469–1481, abstract](https://doi.org/10.1090/mcom/3696): involutive solutions of sizes 9 and 10 number **321,931** and **4,895,272**; non-involutive solutions of size 8 number **422,449,480**. These are **solution** counts, not b(n) or s(n).
- OEIS and MathOverflow: searched for the b(n)/s(n) sequences and discussions. **No OEIS sequence ID specific to these quantities was reliably confirmed**; therefore none is cited or populated. [MathOverflow discussion](https://mathoverflow.net/questions/320328/examples-of-yang-baxter-monoids) explains brace/YBE constructions but does not settle these counts. This is a coverage gap, not evidence of absence.
- Bibliographic identity cross-check: [BNY20](https://doi.org/10.1142/S0218196720500216) is also indexed as **OpenAlex W2964149704** ([record](https://openalex.org/W2964149704)); original journal volume 30(4), pp. 839–851. Bibliographic database identity is not a verification of the numerical results.

### References used for status changes, with pinpoint result locations

- **[BNY20]** V. Bardakov, M. Neshchadim, M. Yadav, [*Computing skew left braces of small orders*](https://arxiv.org/pdf/1907.08978), *Internat. J. Algebra Comput.* 30 (2020), 839–851; **Algorithm 2.3; §3 Table 1** (new counts); [DOI](https://doi.org/10.1142/S0218196720500216).
- **[BEP24]** A. Ballester-Bolinches, R. Esteban-Romero, V. Pérez-Calabuig, [*Enumeration of left braces with additive group C₂²×C₄²*](https://doi.org/10.1007/s11587-023-00772-2), *Ricerche di Matematica* 73 (2024), 2679–2685, published online 2023; **Theorem 1.1, Corollary 1.2 and Tables 1–3**.
- **[DI21]** C. Dietzel, [*Braces of order p²q*](https://arxiv.org/abs/1801.06911), *J. Algebra Appl.* 20 (2021), 2150140; **introductory restatement of GV17 Conjectures 6.2–6.4, Corollaries 3–4**; [DOI](https://doi.org/10.1142/S0219498821501401).
- **[BF25]** N. Byott, F. Ferri, [*On the number of quaternion and dihedral braces and Hopf–Galois structures*](https://arxiv.org/pdf/2402.12547), *J. Algebra* 665 (2025), 72–102; **Theorem 11.1, Theorem 13.1, Table 2 (arXiv p. 23)**; [DOI](https://doi.org/10.1016/j.jalgebra.2024.11.011).
- **[RUM20]** W. Rump, *Classification of the affine structures of generalized quaternion groups*, *J. Group Theory* 23 (2020), 847–869; **result quoted in [BF25 p. 2]**. Exact theorem number not checked in the original journal PDF.
- **[AB20]** E. Acri, M. Bonatto, [*Skew braces of size pq*](https://doi.org/10.1080/00927872.2019.1709480), *Communications in Algebra* 48 (2020), 1872–1881; **abstract and classification theorem**.
- **[AB22]** E. Acri, M. Bonatto, [*Skew braces of size p²q I: abelian type*](https://arxiv.org/abs/2004.04291), *Algebra Colloq.* 29 (2022), 297–320, [DOI](https://doi.org/10.1142/S1005386722000244), and [*II: non-abelian type*](https://arxiv.org/abs/2004.04232), *J. Algebra Appl.* 21 (2022), 2250062; **introductions and classification theorems**.
- **[AMV22]** Ö. Akgün, M. Mereb, L. Vendramin, [*Enumeration of set-theoretic solutions to the Yang–Baxter equation*](https://doi.org/10.1090/mcom/3696), *Math. Comp.* 91 (2022), 1469–1481; **abstract, Theorems 1.1–1.4**.
- **[DPT25]** C. Dietzel, S. Properzi, S. Trappeniers, [*Indecomposable involutive set-theoretical solutions ... of size p²*](https://doi.org/10.1080/00927872.2024.2405024), *Commun. Algebra* 53 (2025), 1238–1256; **classification in paper abstract**.
- **[CO25]** F. Cedó, J. Okniński, [*New simple solutions of the Yang–Baxter equation and their permutation groups*](https://arxiv.org/abs/2401.12904), *J. Pure Appl. Algebra* 229 (2025), 108025; **simplicity criteria and constructed families**.
- **[CO25-IYB]** F. Cedó, J. Okniński, [*New classes of IYB groups*](https://arxiv.org/abs/2502.14805), 2025; **abstract**: positive sufficient conditions for groups with class-two Sylow subgroups.
- **[LET25]** T. Letourmy, [*Free commutative skew braces*](https://arxiv.org/abs/2506.19765), 2025; **main theorem in abstract**; the commutativity qualifier matters.
- **[NIL24]** A. Ballester-Bolinches, M. Ferrara, V. Pérez-Calabuig, M. Trombetti, [*A note on right-nil and strong-nil skew braces*](https://arxiv.org/pdf/2310.11123), published online 18 Dec. 2024, *Proc. Royal Soc. Edinburgh A* 156(5) (Oct. 2026), 2302–2310; **abstract and constructed counterexamples**.
- **[DMFT26]** M. Di Matteo, M. Ferrara, M. Trombetti, [*A Counterexample to Byott's Conjecture for Finite Skew Braces*](https://arxiv.org/abs/2607.22795), posted 24 July 2026; **abstract** reports insoluble circle group with PSL₂(7) quotient.
- **[GONG26]** Lü Gong, [*A congruence-group counterexample to Kourovka Problem 21.7*](https://arxiv.org/abs/2611.13792), posted 10 Nov. 2026; **abstract** gives supersoluble non-IYB groups with IYB Sylow subgroups; very recent preprint.
- **[CGRV25]** T. Crespo, D. Gil-Muñoz, A. Rio, M. Vela, [*Determining skew left braces of size np*](https://doi.org/10.1080/00927872.2025.2499066), *Commun. Algebra* 53 (2025), 4817–4843; **abstract and classification under stated coprimality/uniqueness hypotheses**, proving the 12p conjecture. It does **not** classify all np without hypotheses.

## Evidence

### Exact reproducibility test carried out here — **C (limited)**

Files in this directory:
- **enumerate_cyclic.py** enumerates all subsets of order n of Hol(C_n), checks subgroup closure, regularity by the orbit of 0, quotients by Aut(C_n)-conjugacy, outputs explicit affine subgroup representatives and circle tables in machine-readable JSON Lines. Target: **n=2,3,4 only**.
- **enumeration.log** is its complete deterministic stdout; counts of regular subgroups and isomorphism classes: n=2 **(1,1)**; n=3 **(1,1)**; n=4 **(2,2)**. Counts concern **only additive cyclic groups C_n**, NOT b(n) in general. For n=4, total b(4)=4 includes noncyclic additive groups, so no contradiction.
- **check_witnesses.py** is a separately written multiplication-table checker of group identity, Latin rows, associativity, all brace identities, and non-isomorphism under additive units. It deliberately does **not** repeat subgroup enumeration and therefore only verifies witnesses, not exhaustive search completeness.
- **checker.log** records three PASS lines. All programs use only Python 3 standard library; executed under Python 3.13.5. Commands:

    python3 status/enumerate_cyclic.py > status/enumeration.log
    python3 status/check_witnesses.py < status/enumeration.log > status/checker.log
    sha256sum -c status/SHA256SUMS

- **SHA256SUMS** contains SHA-256 values of every other file in status/. Every pushed file including SHA256SUMS is fetched back from the exact feature branch and compared separately for byte equality and SHA-256; the manifest is deliberately non-self-hashing. The connector read-back audit is recorded in the PR body (not an extra status file) to avoid circular hashes. Results cannot be inferred merely from Git blob SHA-1.

The regular-subgroup ↔ brace construction is a standard theorem from [GV17 §4](https://arxiv.org/pdf/1511.03171) and [BF25 p. 2](https://arxiv.org/pdf/2402.12547), not established from first principles by this tiny script. Here it serves as an independently checkable implementation smoke test.

### Source evidence versus new lab results

**L claims**: conclusions come from specified printed theorems, corollaries, abstracts or tables. No independent formal proof checking, GAP enumeration replay, or verification of uploaded authors' original code was done. **C claim**: only the cyclic-group smoke test has local code/output and a separate verifier. **U claim**: source-search inconclusive, and “open” is provisional rather than a proof that no paper exists. Literature surveyed through public arXiv, journal publisher pages, MathOverflow and OEIS search, plus the GAP YangBaxter website; no paid calls.

## Not covered

1. **The requested full verbatim transcription** of eight 2017 items and fifty 2019 items is not reproduced; refer to the linked §6 and §2 primary PDFs by number and printed page. The summaries above are not quotes.
2. **No replay of BNY20, BEP24, Byott–Ferri, or 2026 preprint proofs**, and no independent validation of their very large published counts. **No new large-order enumeration** is claimed.
3. **GAP unavailable** in the execution container; the YangBaxter dataset was not loaded. Local network access to arXiv from the container was unavailable, so sources were consulted through public page/PDF retrieval instead; this does not supply reproducible local paper snapshots.
4. **No confirmed OEIS A-number** for b(n) or s(n), no systematic Semantic Scholar citation graph traversal. An OpenAlex work ID was cross-checked for BNY20 only. Likewise, MathOverflow search yielded no independent proof of the listed large counts.
5. **Specific statuses marked O/U** need a specialist citation chase and can change; positive/negative preprints from July and November 2026 should be treated as **reported**, not peer-reviewed.
6. **No complete written proof** supplied for a novel theorem; the software test is finite and small. Separate checker confirms witness validity/non-isomorphism but cannot certify enumerator completeness independently of source inspection.

## Next steps

Five tightly scoped options, each with a concrete *first step* and a falsifiable deliverable, not a promise of a new theorem:

1. **Order-64/96 skew-brace gap audit and additive-type lower bounds.** [BNY20 Table 1] has s(64) and s(96) missing. First step: obtain an exact coverage matrix from GAP YangBaxter v0.10.7 and contemporary datasets by additive SmallGroup ID; pick **one tractable nonabelian additive group of order 64 or 96**, enumerate its Hol(A) regular subgroups up to Aut(A), and publish counts plus an orbit-stabilizer sum, output and a separate table checker. Do not claim the whole order solved.
2. **Independent replay of a published nontrivial additive-type count.** First step: choose a small 32/64 additive type, fetch its published witness archive from [braces64](https://github.com/RamonEstebanRomero/braces64), implement a second canonicalization path based on explicit group actions, and compare complete SHA-256-indexed representative sets; seek discrepancies before searching new orders.
3. **Search Problem 2.24's even-torsion classical case.** First step: enumerate all classical left braces on each abelian group of order ≤16; test associativity of star and two-sidedness independently; if a negative case appears, emit its two Cayley tables and a standalone checker. If none appears, state the finite bound only, not a proof of the conjecture.
4. **Check Problem 2.35's very recent supersoluble example without replaying the entire proof.** First step: transcribe the explicit p=31 group presentation and construct finite quotient diagnostics with standard Python/GAP group operations, checking Sylow orders and that the alleged obstruction occurs as stated; log any computational obstruction separately from the published theoretical non-IYB claim.
5. **Formalize the finite holomorph-to-brace bridge.** First step: prove in Lean or another free proof assistant that a regular subgroup of Hol(A) induces an associative circle law satisfying the skew brace identity for finite A. A complete proof plus a tiny two-group example would strengthen the independent checking infrastructure.

**Priority recommendation:** (1) coverage audit followed by **one** additive-type tranche, and (3) a theorem-or-witness search with a fully separate table checker. Neither should be represented as a result before its complete proof or code, stdout, checksums and counterchecking are committed.
