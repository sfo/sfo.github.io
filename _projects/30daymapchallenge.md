---
title: 30 Day Map Challenge
classes: wide
entries_layout: grid
sidebar:
  nav: "projects"
header:
  teaser: /assets/images/30daymapchallenge.png
---

## Background
The core idea is to create a map at every day of November, each targeting a specific theme.
Maps may be created using any tool or technique one is comfortable with.
Or you take that chance to learn something new and employ some technology you never used before.


{% assign entries_layout = page.entries_layout | default: 'list' %}

## Maps 2024
<div class="entries-{{ entries_layout }}">
  {% assign posts = site.posts | reverse %}
  {% for post in posts %}
    {% capture year %}{{post.date | date: "%Y"}}{% endcapture %}
    {% if year == "2024" and post.tags contains page.slug %}
      {% include archive-single.html type=entries_layout %}
    {% endif %}
  {% endfor %}
</div>