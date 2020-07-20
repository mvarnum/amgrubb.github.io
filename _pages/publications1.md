---
layout: archive
title: "Publications1"
permalink: /publications1/
author_profile: true
---

You can also find my publications on [DBLP](https://dblp.org/pers/hd/g/Grubb:Alicia_M=).

**The following are select publications:**

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications1 reversed %}
  {% include archive-single.html %}
{% endfor %}

**Page under construction!**