---
title: Configuration of Thunderbird / Betterbird
categories:
  - Blog
tags:
  - thunderbird
  - e-mail
  - configuration
---

For some reason that I cannot remember, I transitioned from Thunderbird to Betterbird.
Ususally, I install it via Flatpak.

Here, I will list some settings that I find useful, so I can reproduce those over various installations.

## Default Sorting and Threading of Messages

In the config editor (`Menu > Settings > General > Config Editor ...`), make sure the following settings are made:

```
mailnews.default_news_sort_order  2
mailnews.default_news_sort_type  21
mailnews.default_news_view_flags  1
mailnews.default_sort_order       2
mailnews.default_sort_type       18
mailnews.default_view_flags       1
```

Since these settings affect new (not yet indexed) folders, only, one has to apply the view configuration to one folder, then switch to _Table View_ (if currently in card view), use the right-most column to select `Apply current view to... > Folder and its children...` and select an appropriate parent folder.
If required, switch back to _Card View_ again.

<details>
  <summary>
    Other possible values for the settings mentioned abouve, are:
  </summary>

### Sort Order

|value|sort order|
|-----|----------|
|1|Ascending|
|2|Descending|

### Sort Type

|value|sort type|
|-----|---------|
|17|None|
|18|Date|
|19|Subject|
|20|Author|
|21|ID (Order Received)|
|22|Thread|
|23|Priority|
|24|Status|
|25|Size|
|26|Flagged|
|27|Unread|
|28|Recipient|
|29|Location|
|30|Label|
|31|Junk Status|
|32|Attachments|
|33|Account|
|34|Custom|
|35|Received|

### View Flags

|value|view|
|-----|----|
|0|Unthreaded|
|1|Threaded|

</details>
