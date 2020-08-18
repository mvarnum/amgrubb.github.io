---
title: 'Exploring Uncertainties in COVID-19 Modeling'
date: 2020-08-20
excerpt: Kate M. B. Spencer and Megan H. Varnum
collection: projects
permalink: /posts/2020-08-20-covid-uncertainties
layout: archive
---

**Exploring Uncertainties in COVID-19 Modeling**  
**_2020 SURF Abstract by Kate Spencer and Megan Varnum_**

Goal Modeling is used in early phases of projects to evaluate tradeoffs with stakeholders. These models consist of intentions, such as goals, tasks and resources, and are encapsulated in actors that represent stakeholders. These intentions are then connected with links, such as ‘++’, ‘--’, ‘and’, and ‘or’. For example, [our attached figure] shows the actor Emma, who is a student deciding how to have dinner and has the goal of ‘make dinner’.

In the spring of 2019, we observed the wide use of models to understand the evolving COVID-19 global pandemic. For example, Bayesian models were used to describe the spread of the virus. We aimed to understand how our goal modeling tools and analysis could be used to make tradeoff decisions in the context of this pandemic. Our SURF project focused on creating a case study of individual decisions in the early stages of the COVID-19 pandemic. Previous case studies were analyzed retroactively, and this crisis provides a unique opportunity to make relevant models and validate our technique as the pandemic progresses. We initially created a collection of goal models based on personas that reflected different stakeholder views of COVID-19. The personas varied in compliance with COVID-19 guidelines, and values, and were based on reactions to publicized models on the pandemic progression in Quebec, Canada.

The development of our case study enabled our collaboration with the Famelis lab at the Université de Montréal to explore modeling and resolving uncertainties in requirements. 
As a proof of concept, we focused on the Emma model (see figure) and evaluated the inherent uncertainties in our model using DRUIDE (Design and Requirements Uncertainty Integrated Development Environment). Specifically, we describe uncertainty about modeling and what we could and could not represent in this model, as opposed to any uncertainty an actor may have about their decisions. For example, a modeler may ask, “should we separate contracting and transmitting COVID-19?”, or “how can we model Emma’s use of a mask?”. We then localize these questions in our model. For example, we can add a decision to the model giving the modeler the option of adding a resource labeled “mask”. DRUIDE gave us a formal language (via a metamodel) to identify modeling uncertainty and localize it on the model, which allows us to concretize the uncertainty into decisions which can be acted on. 

Our team then connected our DRUIDE enabled goal model of Emma with a Bayesian model that describes the spread of COVID-19, allowing us to understand how decisions in one model impacts the other. We also found similar design uncertainties across models. Finally, we worked to implement these features in MMINT, an Eclipse-based mega modeling extension for Interactive Model Management.


<img src="/images/surf-2.png"
     alt="goal model"
     />

