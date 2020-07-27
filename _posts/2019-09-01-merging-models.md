---
title: 'Model Merging and Layout'
date: 2019-09-01
permalink: /posts/2019-09-01-merging-models
---

Lucy Wang Senior Thesis
===

For her senior thesis, Lucy expanded upon this work and wrote [Towards a General Solution for Layout of Visual Goal Models with Actors.](https://amgrubb.github.io/publication/2020-Towards-a-General-Solution-for-Layout-of-Visual-Goal-Models-with-Actors)


Summary from Summer 2019
===
Towards Merging Models over Different Time Intervals
---
Omema Ibrahim and Lucy Wang 
---
BloomingLeaf is an analysis and modeling tool that allows stakeholders to model goals and intentions. The tool helps users understand model evolution and tradeoffs by evaluating how intentions change over time. Prior work looked at creating models piecemeal, by constructing models of individual actors over different time periods and then merging them together. Grubb proposed an algorithm for merging goal models and showed a potential application; but, did not implement the proposed semi-automated algorithm. In this project, we explored the problem domain of this merge algorithm and developed underlying tooling.

To fully implement the algorithm, we needed to merge both the visual syntax and underlying semantics of both un-timed and evolving goal models. We worked on the merging of timed functions. In this project, all functions are step-wise atomic functions over disjoint neighboring intervals, where the atomic functions are constant, increase, decrease, and stochastic. Consider the functions in Figure 1, Model A is an increasing function over the interval [tA1, tA2) and Model B is a constant function over the interval [tB1, tB2). The purpose of our algorithm is to specify Model AB.

Specifying the resulting Model AB depends on the underlying timeline over which each model is defined. For example, in Figure 1, if tA2 < tB1 then there exists an unspecified gap in the function. If tA2 > tB1 then there exists an overlap in the function which may result in a conflict.
Finally, if tA2 = tB1 then the two functions align. In Figure 1, Model AB assumes the case where tA2 = tB1 with the new interval [tA1, tB2). We focused on the tA2 = tB1 case in this research project.

With this timeline, we investigated how the two functions should be merged. We found that Model A and Model B can be merged into either an increase function followed by a constant function, or an increase function with a single time point specified. We proved (by contradiction) the soundness of our assertion. We implemented the first case of the merge algorithm (tA2 = tB1). Future work will finish the implementation for the two other cases and create a web interface for the merge algorithm.

<img src="/images/surf-1.png"
     alt="figure 1 as described above, shows three graphs, the first with a slope increasing from 0, the second constant at a positive value, and the third, both previous graphs combined."
     />

This article is under construction
---