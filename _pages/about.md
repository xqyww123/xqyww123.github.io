---
permalink: /
title: "Qiyuan Xu"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am an [Isabelle](https://isabelle.in.tum.de/) hacker and a PhD candidate at Nanyang Technological University, supervised by [Conrad Watt](https://conrad-watt.github.io/). 
Aimming to diminish the gap between verification for functional correctness and broad industry applications, my research interest focuses on program logics, program verification, automated theorem proving, and neural theorem proving.

My current projects involve two directions:

## Neural Theorem Proving for Real-world Proof Engineering

Isabelle infrastructures for machine learning:
- [Isabelle REPL](https://github.com/xqyww123/Isa-REPL), a socket-based Isabelle REPL server for clusters.
- [MiniLang](https://github.com/xqyww123/Isa-Mini), a minimal proof lanugage of Isabelle designed for LLM.
- [MLML](https://github.com/xqyww123/MLML), a machine learning framework for NTP over Isabelle.

Sledgehammer wrapper / interfaces:
- [Auto Sledgehammer](https://github.com/xqyww123/auto_sledgehammer)

Drafts under review:
- A Minimal Proof Language for Neural Theorem Proving over Isabelle/HOL. *Qiyuan Xu, Renxi Wang, Haonan Li, David Sanan, Conrad Watt*. [online draft](/files/MiniLang.pdf)

## An automated program verification platform over Isabelle

- Based on a first-order [fictional separation logic](https://cs.au.dk/~birke/papers/sharing-conf.pdf)
- Focusing on automation, equiped with our [algebraic-based automation algorithms](https://dl.acm.org/doi/abs/10.1145/3704903) for generically reasoning about a wide amount of data structures.
- Certified programming that provides instant symbolic execution and a development environment  intergrated within Isabelle/Isar.
- For sequential, terminating programs, but still capable for critical industrial applications like smart contracts.
- [Github available](https://github.com/xqyww123/phi-system)

**Publications**

- Generically Automating Separation Logic by Functors, Homomorphisms, and Modules. *Qiyuan Xu, David Sanan, Zhe Hou, Xiaokun Luan, Conrad Watt, Yang Liu*, [POPL'25](https://dl.acm.org/doi/abs/10.1145/3704903)


