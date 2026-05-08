## The Problem

Once again, MS Word messed up the redo-History by using non-standard keyboard shortcuts.
Just like for basic formatting, where it uses localized shortcuts like `CTRL` + `SHIFT` + `F` for bold text ("F" is for the German word "fett"), it also does not adhere to the common `CTRL`+`Z` / `CTRL`+`SHIFT`+`Z` combination for undo / redo!
Instead, when you press `CTRL`+`SHIFT`+`Z`, instead of _redo_, word simply deletes the redo-History!

To prevent this stupid behaviour, one should change the shortcuts immediately after installation.

## Change Word Keyboard Shortcuts

To change Word's keyboard shortcuts to something senseful, go to _File_ -> _Options_ -> _Customize Ribbon_ -> _Customize (Keyboard shortcuts)_.
Now, from the left list (_Categories_), select the _Home_ tab.
On the right (_Commands_), search for _EditRedo_ and assign the correct shortcut, which will automatically delete all other assignments to whatever strange command it belongs.
Do the same for:
- _File_ -> _FileSaveAs_ -> `CTRL` + `SHIFT` + `S`
