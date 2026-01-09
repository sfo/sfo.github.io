---
title: Studtistics
classes: wide
entries_layout: grid
sidebar:
  nav: "projects"
header:
  teaser: /assets/images/studtistics.png
---

## Background

Here, I will collect posts that are related to one of my biggest hobbies: Lego bricks.
Most of these posts will target statistics topics to objectivy the (often very negative and subjective) discussion around these colorful building blocks.
Even though I will focus on bricks made by the company LEGO, I am not afraid to use and mention other brands as well.

{% assign entries_layout = page.entries_layout | default: 'list' %}

## Statistics of Bricks

<div class="entries-{{ entries_layout }}">
  {% assign posts = site.posts | reverse %}
  {% for post in posts %}
    {% capture year %}{{post.date | date: "%Y"}}{% endcapture %}
    {% if post.tags contains page.slug %}
      {% include archive-single.html type=entries_layout %}
    {% endif %}
  {% endfor %}
</div>
