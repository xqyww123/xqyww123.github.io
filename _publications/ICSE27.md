---
title: "Theorem Proving Agent over Abstract Syntax Tree of Redesigned Language"
collection: publications
category: conferences
permalink: /publication/icse27
excerpt: "The extension of the Minilang work into a proof agent operating directly on the abstract syntax tree, achieving high efficiency: compared with Amazon's Isabelle Agent, it cuts API cost by 2.3–4.7x and token consumption by 2.9–6.9x, while solving far more problems on the harder verification benchmark"
date: 2027-04-25
venue: 'ICSE'
prompt: 'Accepted in'
paperurl: 'https://arxiv.org/pdf/2607.16372'
bibtexurl: '/files/icse27.bib'
citation: 'Qiyuan Xu, Joshua Ong Jun Leang, Renxi Wang, Wenda Li, Haonan Li, Luke Ong, Conrad Watt'
---
Interactive theorem proving (ITP) underpins program verification and formalized mathematics, but its manual effort limits scalability. LLM-based proof agents promise to ease this effort, but their heavy token consumption and API cost remain a major obstacle. We trace this cost to a shared root: current agents operate on serialized concrete syntax, emitting proofs as source text and recovering proof states through separate, line-number-based queries, so every edit shifts later lines and forces repeated relocation of errors and states. This same dependence on concrete syntax also blocks adoption of Minilang, a recent proof language that reaches SOTA on LLM-based proving but is too new for LLMs' training corpora. We address both problems by lifting the agent off source text and onto the abstract syntax tree (AST): the model supplies proofs as JSON representations of Minilang's AST — native to tool-calling LLMs — and drives the prover through a tree-edit model that fuses proof operations and states into one proof tree, so each operation carries its own subgoal's state, readable directly off the tree. We realize this design in *Agent over AST* (AoA). Against Amazon's Isabelle Agent on miniF2F and NTP4VC-Pearl common success sets, AoA cuts API cost by 2.3–4.7x (normalized input-cache accounting), uses 2.9–6.9x fewer tokens and 3.9–8.9x fewer tool calls, and finishes 1.4–2.0x faster — while also solving far more problems on the harder verification benchmark.

[arXiv](https://arxiv.org/abs/2607.16372)
