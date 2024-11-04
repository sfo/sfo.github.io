---
title: Over the Wire - Level Natas
# classes: wide
toc: true
toc_sticky: true
sidebar:
  nav: "projects"
header:
  teaser: /assets/images/overthewire.png
---

## Level 0

This is the entry level into the challenge.
There is nothing to find here.
Instead, the password for level 0 is given right on the page itself.


## Level 1

The password for level one can be found on the page located at <http://natas0.natas.labs.overthewire.org/>, using username and password from level 0.

When navigating to the website, it says:
> You can find the password for the next level on this page.

Maybe, the password text has the same color as the background it's rendered on.
So, let's select all text on the page via `CTRL`+`A`, since this would highlight it anyway.
However, this does not reveal anything.

The next most obvious one would be that the password cannot be find exactly _on_ the page but in its source.
Open the website source code view via `CTRL`+`U` (works at least in Google Chrome).
Aha.
Here we got it.
There is a comment in the code that says:
```html
<!--The password for natas1 is [...] -->
```

With this, let's move on to level 2.


## Level 2

The [website of level 1](http://natas1.natas.labs.overthewire.org/) says:
> You can find the password for the next level on this page, but rightclicking has been blocked!

Since I did not use right-click for the previous level, this one is rather easy to solve:
Again, open source view via `CTRL`+`U` and you get the password right away:
```html
<!--The password for natas2 is [...] -->
```


## Level 3

Here, we get a meaningless message
> There is nothing on this page

A look on the source code reveals that there is actually an additional image of 1x1 pixel.
Downloading and examining this file (i.e. its metadata), does not reveal anything.
Maybe, there are more files to download?
So let's navigate to <http://natas2.natas.labs.overthewire.org/files/>, where we find another file called `users.txt`.
This file contains a list of username-password combinations, including the one for the next level:
```
[...]
natas3:[...]
[...]
```

## Level 4

The source code of <http://natas3.natas.labs.overthewire.org/> reveals a nice hint:
```html
<div id="content">
There is nothing on this page
<!-- No more information leaks!! Not even Google will find it this time... -->
</div>
```

How can one prevent Google from finding specific information on the website?
Right, by specifying some rules in a file called `robots.txt`.
Let's see, if this one exists and what it tells us:
```
User-agent: *
Disallow: /s3cr3t/
```

Every crawler is asked to exclude the path `/s3cr3t/` from its search index.
This sounds very promising.
So let's be a bad crawler and check this path, nevertheless.

Here, we find a file called `users.txt` again, which holds the password for level 4.
