---
title: 'Porting BloomingLeaf to Local Node.js Server'
date: 2019-09-01
permalink: /posts/2019-09-01-local-bloomingleaf
---

**Porting BloomingLeaf to Local Node.js Server**  
**_2019 SURF Project by Omema Ibrahim and Lucy Wang_**

BloomingLeaf is an analysis and modeling tool that allows stakeholders to model goals and intentions. The tool helps users understand model evolution and tradeoffs by evaluating how intentions change over time. Prior work looked at creating models piecemeal, by constructing models of individual actors over different time periods and then merging them together. 

BloomingLeaf was hosted as a web-based tool, which created problems for users with limited internet connections and those concerned with data privacy. In exploring the merge algorithm, we also discovered issues with passing several models over the internet and decided to create a local-only version of BloomingLeaf. This had the advantage of allowing us to test features locally without a constant need to update the web-server. We adapted BloomingLeaf to work as a local Node.js server.  

See our [GitHub page](https://github.com/amgrubb/BloomingLeaf/blob/develop/NODE-README.md) for our instructions on how to use BloomingLeaf locally with your own Node.js server.

