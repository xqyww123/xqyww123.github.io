---
title: "Why the Proof Fails in Different Versions of Theorem Provers: An Empirical Study of Compatibility Issues in Isabelle"
collection: publications
category: conferences
permalink: /publication/fse25
excerpt: 'A software engineering work for proof repair over Isabelle.'
date: 2025-06-19
venue: 'FSE'
#slidesurl: '/files/Genericall_Automating_SL___Slides.pdf'
paperurl: '/files/3715787.pdf'
bibtexurl: '/files/fse25.bib'
citation: 'Xiaokun Luan, David Sanan, Zhe Hou, Qiyuan Xu, Chengwei Liu, Yufan Cai, Meng Sun'
---
Proof assistants are software tools for formal modeling and verification of software, hardware, design, and mathematical proofs. Due to the growing complexity and scale of formal proofs, compatibility issues frequently arise when using different versions of proof assistants. These issues result in broken proofs, disrupting the maintenance of formalized theories and hindering the broader dissemination of results within the community. Although existing works have proposed techniques to address specific types of compatibility issues, the overall characteristics of these issues remain largely unexplored. To address this gap, we conduct the first extensive empirical study to characterize compatibility issues, using Isabelle as a case study. We develop a regression testing framework to automatically collect compatibility issues from the Archive of Formal Proofs, the largest repository of formal proofs in Isabelle. By analyzing 12,079 collected issues, we identify their types and symptoms and further investigate their root causes. We also extract updated proofs that address these issues to understand the applied resolution strategies. Our study provides an in-depth understanding of compatibility issues in proof assistants, offering insights that support the development of effective techniques to mitigate these issues.

[ACM Digit library](https://dl.acm.org/doi/10.1145/3715787)
