# 1. export bibliography from Zotero:
# -> sort list of own publications by year
# -> select all items
# -> right click -> create bibliography from items
# -> style: IEEE, language: English, output: Bibliography, format: html
#
# 2. format html file using vim:
# - %s/\[\d\+\]/\&mdash;/
# - %s/S. Förster/<b>S. Förster<\/b>/
# - g/<span/d
#
# 3. insert preamble
# ```
# ----
# title: Research
# permalink: /research/
# classes: wide
# ----
# <style>
#   .csl-entry {
#     margin-bottom: 1em;
#   }
# </style>
# ```
