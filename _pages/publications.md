---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: false
---
**Page under construction! 7/21/2020**

You can also find my publications on [DBLP](https://dblp.org/pers/hd/g/Grubb:Alicia_M=).

**The following are select publications:**

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

