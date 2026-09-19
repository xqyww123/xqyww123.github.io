---
permalink: /
title: "Qiyuan Xu"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am an [Isabelle](https://isabelle.in.tum.de/) hacker and a PhD candidate at Nanyang Technological University, supervised by [Conrad Watt](https://conrad-watt.github.io/). 

I am one of the 10 researchers in the past decade who have first-authored papers at both ICLR and POPL. See details [here](/10authors).

Aimming to diminish the gap between verification for functional correctness and broad industry applications, my research interest focuses on program logics, program verification, automated theorem proving, and neural theorem proving.
My current projects involve two directions:

## Neural Theorem Proving for Program Verification over Rich Logics

In my [PhD thesis](https://doi.org/10.5281/zenodo.22053760), I predict that the combination of LLM agents and deductive verification over rich logics will ultimately achieve a breakthrough in program verification.

Associated works:
- [AoA](https://isabelle.zulipchat.com/#narrow/channel/202967-New-Members-.26-Projects/topic/The.20proof.20agent.20AoA.27s.20update.20channel/) Theorem Proving Agent over Abstract Syntax Tree of Redesigned Language. [preprint](https://arxiv.org/abs/2607.16372).
- [MiniLang](https://github.com/xqyww123/Isa-Mini), a minimal proof language of Isabelle designed for LLM, published in [OOPSLA'26](https://dl.acm.org/doi/10.1145/3798275)
- [IsaFinder](https://isabelle-semantics.qiyuan.me/), a semantic search engine for Isabelle/HOL and AFP.
- [MLML](https://github.com/xqyww123/MLML), a machine learning framework for NTP over Isabelle.


## An automated program verification platform over Isabelle

- Based on a first-order [fictional separation logic](https://cs.au.dk/~birke/papers/sharing-conf.pdf)
- Focusing on automation, equiped with our [algebraic-based automation algorithms](https://dl.acm.org/doi/abs/10.1145/3704903) for generically reasoning about a wide amount of data structures.
- Certified programming that provides instant symbolic execution and a development environment  intergrated within Isabelle/Isar.
- For sequential, terminating programs, but still capable for critical industrial applications like smart contracts.
- [Github available](https://github.com/xqyww123/phi-system)

Associated papers:

- Generically Automating Separation Logic by Functors, Homomorphisms, and Modules. *Qiyuan Xu, David Sanan, Zhe Hou, Xiaokun Luan, Conrad Watt, Yang Liu*, [POPL'25](https://dl.acm.org/doi/abs/10.1145/3704903)


