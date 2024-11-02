---
title: 30 Day Map Challenge
classes: wide
sidebar:
  nav: "projects"
header:
  teaser: /assets/images/30daymapchallenge.png
---

## Background
The core idea is to create a map at every day of November, each targeting a specific theme.
Maps may be created using any tool or technique one is comfortable with.
Or you take that chance to learn something new and employ some technology you never used before.

## Maps 2024

{% for post in site.posts %}
    {% if post.tags contains page.slug %}
  - <a href="{{post.url}}">{{post.title}}</a>
    {% endif %}
{% endfor %}
