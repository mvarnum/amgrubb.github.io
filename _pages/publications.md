---
layout: archive
title: "Select Publications"
permalink: /publications/
author_profile: true
---
**Page under construction! 7/21/2020**

See full list on [DBLP](https://dblp.org/pers/hd/g/Grubb:Alicia_M=) or [Google Scholar](https://scholar.google.com/citations?user=br2VoDkAAAAJ&hl=en&authuser=1).


\* denotes authors who conducted research as undergraduate while at Smith College.  
† denotes authors who conducted research as undergraduate while at the University of Toronto.


{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

