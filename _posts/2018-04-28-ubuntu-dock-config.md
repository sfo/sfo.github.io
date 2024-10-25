---
title: "Customizing the Ubuntu Dock"
categories:
  - Blog
tags:
  - linux
  - ubuntu
  - configuration
---

Just installed Ubuntu 18.04 LTS. Here I will collect the changes I made to customize it to fit my needs. This post will be updated on irregular base.

<!--more-->

## Behavior for Click on Dock Icon

By default, when clicking an application's icon on the dash, either nothing happens at all (in case only one window belongs to that application) or a preview for every window is shown. This behavior can be changed by calling `gsettings` with the appropriate options:
{% highlight bash %}
gsettings set org.gnome.shell.extensions.dash-to-dock click-action '<mode>'
{% endhighlight %}
where `<mode>` is one of the following:
+ `previews`
  - The default behavior as described above.
+ `minimize`
  - Minimize all the windows of an application, if one of it is on top, bring it to front, otheriwse.
+ `skip`
  - Bring application to the front. If it already is the top window, do nothing.
+ `launch`
  - Launch another instance of the application.
+ `cycle-windows`
  - If there are multiple windows for an application (e.g. browser), cycle through all of them.
+ `minimize-or-overview`
  - Minimize window if on top, otherwise open desktop overview (like pressing the `Meta` key).
+ `quit`
  - Close all instances of the application. If no window is open, start application.

[Source](https://askubuntu.com/a/966522/331777)

## Alt-Tab through Windows on currenty Desktop only

Tabbing through windows using `Alt`+`Tab` cycles through all open windows, no matter to which virtual desktop they belong. For me, it's better to switch between windows on the current workspace only. This can be achieved using the following command:
{% highlight bash %}
gsettings set org.gnome.shell.app-switcher current-workspace-only true
{% endhighlight %}

[Source](https://coderwall.com/p/m5mhoq/gnome-3-how-to-alt-tab-windows-on-current-workspace-only)
