---
title: "Generically Automating Separation Logic by Functors, Homomorphisms, and Modules"
collection: publications
category: conferences
permalink: /publication/popl25
excerpt: 'Several generic abstract algebras for Separation Logic predicates are found, above which generic automations are built to reason about data structures and algorithms'
date: 2025-01-09
venue: 'POPL 25'
slidesurl: '/files/Genericall_Automating_SL___Slides.pdf'
paperurl: '/files/Generically_Automating_Separation_Logic_by_Functors__Homomorphisms_and_Modules.pdf'
bibtexurl: '/files/popl25.bib'
citation: 'Qiyuan Xu, David Sanan, Zhe Hou, Xiaokun Luan, Conrad Watt, Yang Liu'
---
Foundational verification considers the functional correctness of programming languages with formalized semantics and uses proof assistants (e.g., Coq, Isabelle) to certify proofs. The need for verifying complex programs compels it to involve expressive Separation Logics (SLs) that exceed the scopes of well-studied automated proof theories, e.g., symbolic heap. Consequently, automation of SL in foundational verification relies heavily on ad-hoc heuristics that lack a systematic meta-theory and face scalability issues. To mitigate the gap, we propose a theory to specify SL predicates using abstract algebras including functors, homomorphisms, and modules over rings. Based on this theory, we develop a generic SL automation algorithm to reason about any data structures that can be characterized by these algebras. In addition, we also present algorithms for automatically instantiating the algebraic models to real data structures. The instantiation works compositionally, reusing the algebraic models of component structures and preserving their data abstractions. Case studies on formalized imperative semantics show our algorithm can instantiate the algebraic models automatically for a variety of complex data structures. Experimental results indicate the automatically instantiated reasoners from our generic theory show similar results to the state-of-the-art systems made of specifically crafted reasoning rules. The presented theories, proofs, and the verification framework are formalized in Isabelle/HOL.

[ACM Digit library](https://dl.acm.org/doi/abs/10.1145/3704903)
