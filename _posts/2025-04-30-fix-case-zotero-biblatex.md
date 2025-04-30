---
title: Fix case for titles when exporting from Zotero to BibLaTeX
categories:
  - Blog
tags:
  - bibtex
  - latex
  - zotero
  - publication
---

While writing up another paper, I stumbled upon an issue with some of the entries in the list of references.
Specificially, I want to cite some automatic speech recognition (ASR) models hosted at [Hugging Face](https://huggingface.co).
These models got some rather strange titles, which confuse the automatic casing of titles when exporting those from [Zotero](https://www.zotero.org) using the [Better BibTeX](https://github.com/retorquere/zotero-better-bibtex) extension.
Instead of all lowercase, the titles of the models look like this in the list of references:

![png](/assets/2025-04-30-fix-case-zotero-biblatex/screenshot_reference_case_wrong.png)

One way to fix this issue would be to turn off the option to apply title-casing to titles when exporting the library.
This however would mess up all the other entries or require me to manually set the casing explicitly.
Furthermore, in Zotero all titles should be set to sentence-case to let the citation style or exporter do the proper formatting automatically, which would also break when using title-case.
Better BibTeX even warns about this when it encounters entries that do not have titles in sentence-case:

```bibtex
% == BibLateX quality report for vanDoorn2023:
% ? Title looks like it was stored in title-case in Zotero
```

Standard case protection for BibTeX does not help to fix this issue.
Changing the title from `whisper-large-v3-atcosim` to `{whisper-large-v3-atcosim}` in Zotero has no effect but messing up the display of titles in the GUI.
Furthermore, the exported entry now includes curly braces literally as part of the title:

```bibtex
@software{vanDoorn2023,
  title = {\{whisper-Large-v3-Atcosim\}},
  author = {family=Doorn, given=Jan, prefix=van, useprefix=true},
  date = {2023},
  doi = {10.57967/hf/1387},
  version = {99a8cc0}
}
```

After some research, I found Zotero provides some possibilities for [rich text formatting](https://www.zotero.org/support/kb/rich_text_bibliography) of titles.
Among those, there is a way to prevent capitalization rules being applied to certain words or phrases in the title.
Specifically, the title has to be changed to `<span class="nocase">whisper-large-v3-atcosim</span>`.
With this, the item now gets exported properly as:

```bibtex
@software{vanDoorn2023,
  title = {{{whisper-large-v3-atcosim}}},
  author = {family=Doorn, given=Jan, prefix=van, useprefix=true},
  date = {2023},
  doi = {10.57967/hf/1387},
  version = {99a8cc0}
}
```

After fixing the title in Zotero and exporting the library via Better BibTeX, even with automatic title casing enabled, the result looks like this:

![png](/assets/2025-04-30-fix-case-zotero-biblatex/screenshot_reference_case_correct.png)