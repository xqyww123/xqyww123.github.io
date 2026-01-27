---
title: "Neural Theorem Proving for Verification Conditions: A Real-World Benchmark"
collection: publications
category: conferences
permalink: /publication/iclr26
excerpt: A benchmark aimed at applying Neural Theorem Proving to VC proving, a key bottleneck in the program verification industry
date: 2026-04-23
venue: 'ICLR'
#slidesurl: '/files/Genericall_Automating_SL___Slides.pdf'
paperurl: '/files/NTP4VC.pdf'
bibtexurl: '/files/iclr26.bib'
citation: 'Qiyuan Xu, Xiaokun Luan, Renxi Wang, Joshua Ong Jun Leang, Peixin Wang, Haonan Li, Wenda Li, Conrad Watt'
---
Theorem proving is fundamental to program verification, where the automated proof of Verification Conditions (VCs) remains a primary bottleneck. Real-world program verification frequently encounters hard VCs that existing Automated Theorem Provers (ATPs) cannot prove, leading to a critical need for extensive manual proofs that burden practical application. While Neural Theorem Proving (NTP) has achieved significant success in mathematical competitions, demonstrating the potential of machine learning approaches to formal reasoning, its application to program verification--particularly VC proving--remains largely unexplored. 
Despite existing work on annotation synthesis and verification-related theorem proving, no benchmark has specifically targeted this fundamental bottleneck: automated VC proving.
This work introduces Neural Theorem Proving for Verification Conditions (NTP4VC), presenting the first real-world multi-language benchmark for this task. From real-world projects such as Linux and Contiki-OS kernel, our benchmark leverages industrial pipelines (Why3 and Frama-C) to generate semantically equivalent test cases across formal languages of Isabelle, Lean, and Rocq. We evaluate large language models (LLMs), both general-purpose and those fine-tuned for theorem proving, on NTP4VC. Results indicate that although LLMs show promise in VC proving, significant challenges remain for program verification, highlighting a large gap and opportunity for future research.
[Open Review](https://openreview.net/forum?id=MfDyickxQA)
