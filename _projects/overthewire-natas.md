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


## Level 5

This time, we get exokicit information about the condition for entering the website:
> Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"

Since we do not yet have access to Level 5, from which we then could navigate to the page of level 4 (if there's a link at all), we somehow have to get the HTTP referrer correct.
For some browsers, there might exist referrer spoofing extensions.
However, I'll just do it in the terminal this time:
```shell
wget http://natas4.natas.labs.overthewire.org/ --user natas4 --password <LEVEL4_PASSWORD> --referer "http://natas5.natas.labs.overthewire.org/" -O -
```

This command sets the headers just right to receive a proper answer from the server, which is printed to stdout:
```html
<div id="content">

Access granted. The password for natas5 is [...]
<br/>
<div id="viewsource"><a href="index.php">Refresh page</a></div>
</div>
```


## Level 6

After entering the correct credentials, the page for level 5 loads properly but the message on the page claims that we are not logged in:
> Access disallowed. You are not logged in

Since there is no further link that could lead to something like a login page, we have to find a way to tell the website that we _are_ logged in.
One way to do so is via a session-cookie, which a website usually stores on a user's PC when they select somethin like "Stay logged in" or similar.
So let's see, if we can find a cookie.
For Google Chrome, you can open the developer tools via `F12`, navigate to the _Application_ tab and to _Cookies_ on the left hand side of the panel.
There, you will find one cookie for the level 5 page with name _loggedin_ and value _0_.
Change the value to _1_, reload the page and voilà... we are in, again!


## Level 7

The next website asks for yet another secret after login.
Fortunately, there is a link given to view the source code of the server-side implementation that checks out input.
Here, we can see that an additinal file is included that contains the expected value of _secret_.
Maybe, this file is not protected and can be viewed via our browser?
Let's navigate to <http://natas6.natas.labs.overthewire.org/includes/secret.inc> and bingo!
There we find the secret string that we have to paste into the form on the level 6 website to obtain the password for level 7.


## Level 8

The page of level 7 again gives us some links: _Home_, and _About_.
Each link performs a GET request for the base URL of level 7 with an additional parameter `page` that holds the target page's name.
Let's see what happens, if we provide a value other than `home` or `about`:
> Warning: include(test): failed to open stream: No such file or directory in /var/www/natas/natas7/index.php on line 21
>
> Warning: include(): Failed opening 'test' for inclusion (include_path='.:/usr/share/php') in /var/www/natas/natas7/index.php on line 21

Aha!
The code running on the server tries to include a file with the same name.
Hopefully, the developers did not implement any form of input validation.
From the [natas box introduction](https://overthewire.org/wargames/natas/) (and the level 7 source code), we know that all passwords are stored under `/etc/natas_webpass/natasX`.
Therefore, we cab now try to load the file `/etc/natas_webpass/nata8` by setting the `page` GET parameter accordingly: <http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8>.
And here we get it again, the password for the next level.


## Level 9

Here we find a similar form like on the level 6 website.
This time, the source code of the secret verification contains an encoded string.
However, we also can clearly see the method used for encoding the input.
Reversing the process should allow us to decode the given string.
```php
function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}
```

The reverse of which would be:
```php
base64_decode(strrev(hex2bin($encodedSecret)));
```
[Try it online!](https://onlinephp.io/c/9d669)


## Level 10

On the page of level 9 we are presented with an input field and a button that says _"Search"_.
Again, we also have a link to view the server code that handles the search request.
The most promising line is the following:
```php
passthru("grep -i $key dictionary.txt");
```

Since there is no validation of the user input, we can perform an injection attack to modify the command in a way that results in returning the password for level 10.
Specficially, we want to enter somthing like the following into the search field:
```
; cat /etc/natas_webpass/natas10;
```

This results in the following command line being executed on the server:
```shell
grep -i; cat /etc/natas_webpass/natas10; dictionary.txt
```

While the `grep` command is incomplete and will just output and error to stderr, the following `cat` prints the content of the password file to stdout, which becomes part of the website's source code.
Consequently, the browser renders the next password as a result of our search query.


## Level 11

The website of level 10 looks just like the previous one.
However, this time there is a little bit of input validation performed on the server side.
Specifically, the query is checked for the following characters, considered invalid: `|`, `;`, and `&`.
So we have no chance to end the `grep` command and start our own one.
Rather, we have to find a clever argument for it to force printing of the right password:
```shell
-E '.' /etc/natas_webpass/natas11
```

This searches for any character in the password file and print the results to stdout.
Furthermore, it dumps the whole keyword database, which we can just ignore.


## Level 12

[Try ot online](https://onlinephp.io/c/a9a03)