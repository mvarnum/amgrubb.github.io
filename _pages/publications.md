---
layout: archive
title: "Select Publications"
permalink: /publications/
author_profile: true
---

See full list on [DBLP](https://dblp.org/pers/hd/g/Grubb:Alicia_M=) or [Google Scholar](https://scholar.google.com/citations?user=br2VoDkAAAAJ&hl=en&authuser=1).


\* denotes authors who conducted research as undergraduate while at Smith College.  
† denotes authors who conducted research as undergraduate while at the University of Toronto.

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-project.html %}
{% endfor %}

