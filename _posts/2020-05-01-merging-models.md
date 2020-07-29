---
title: 'Thesis: Model Merging and Layout'
date: 2020-05-01
excerpt: Yilin Lucy Wang
collection: projects
permalink: /posts/2020-05-01-merging-models
---

**Automatically Merging Evolving Goal Models**  
**_Senior Honors Thesis by Yilin Lucy Wang_**

Lucy completed her seniors honors thesis with Prof. Grubb and received highest honors!
This thesis (see abstract below) came out of the work she started as a SURF student in the summer of 2019. 
Lucy's thesis proposal was accepted to the ACM Student Research Competition at the 
51st ACM Technical Symposium on Computer Science Education (SIGCSE'20). Unfortunitely,
due to COVID-19, SIGCSE'20 was cancelled and Lucy was unable to present her work, but her 
abstract does appear in the [SIGCSE Proceedings](https://doi.org/10.1145/3328778.3372705).

A chapter of Lucy's thesis formed the basis for the RE@Next paper she co-authored with Prof. Grubb, entitled [Towards a General Solution for Layout of Visual Goal Models with Actors](https://amgrubb.github.io/publication/2020-Towards-a-General-Solution-for-Layout-of-Visual-Goal-Models-with-Actors).

>_Thesis Abstract:_ Goal models help stakeholders make trade-off decisions in the early stages of project development. 
While these approaches have significant analysis capabilities, 
they have yet to see broad industrial adoption, with the construction of scalable large realistic goal models acting as a significant barrier. Recent work suggests creating models piecemeal, and then merging them together. This merge algorithm has only been demonstrated manually and is time consuming due to unnecessary repetition, as well as deferring all decisions to the user. We aim to automate the majority of the merge algorithm. We divide this project into two parts: (1) merging the content of goal models, and (2) automatically creating a visual representation of the merged model.  
We extend prior work on evolving goal models by considering both untimed and timed models in our merge. Using a motivating example, we discuss how we handle conflicts between node names and types as well as conflicts across multiple time scales. We improve the original algorithm by simplifying evolving functions described over multiple intervals, where possible, and prove the correctness of these changes.  
For the visual representation, we present and implement an automatic layout algorithm.
Over the last decade, researchers have used _force-directed algorithms_, specifically GraphViz, to layout goal models and have called for improved layout algorithms to better accommodate the unique challenges presented by actor-based models.
We extend a force-directed algorithm to include goal-model heuristics, and 
independently arrived at a domain-specific version of a generic layout algorithm for _undirected compound graphs_.
For initial validation of the effectiveness and scalability of our algorithm, we implement our approach in BloomingLeaf, a goal model analysis tool.  
Initial results are promising; yet, further collaboration and validation across the various goal modeling approaches (e.g., GRL, iStar, Tropos) is required before we can recommend our approach to be adopted in tooling. 

