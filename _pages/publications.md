---
layout: archive
title: "Select Publications"
permalink: /publications/
author_profile: true
---
**Page under construction! 7/21/2020**

You can also find my publications on [DBLP](https://dblp.org/pers/hd/g/Grubb:Alicia_M=).

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

