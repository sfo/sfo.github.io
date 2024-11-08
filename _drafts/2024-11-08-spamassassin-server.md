## Configure mbsync

[Source 1](https://jonathanh.co.uk/blog/mutt-setup/)

[Source 2](https://brian-thompson.medium.com/setting-up-isync-mbsync-on-linux-e9fe10c692c0)

While the official documentation of the IT department requests `user\<LOGIN>` to be used as username, for mbsync, I only need my actual login, without a domain prefix.

Again, Microsoft software is incapable of handling stuff right, leading to the following error when syncing:
```shell
$ mbsync --pull work
IMAP command 'UID FETCH 27396 (BODY.PEEK[])' returned an error: UID FETCH 27396 (BOD* 5 FETCH (BODY[] {10039}
```

To fix this problem, I have to limit the number of parallel connections via the setting `PipelineDepth 1` ([source](https://kdecherf.com/blog/2017/05/01/mbsync-and-office-365/)).

Finally, the `~/.mbsyncrc` config looks like:
```
IMAPAccount work
Host msx.company.com
Port 993
User "<USER>"
Pass "<PASSWORD>"
SSLType IMAPS
AuthMechs LOGIN
PipelineDepth 1

IMAPStore work-remote
Account work

MaildirStore work-local
Subfolders Verbatim
Path ~/.mail/work/
Inbox ~/.mail/work/INBOX

Channel work
Far :work-remote:
Near :work-local:
Patterns *
Create Near
SyncState *
Sync All
```

After running `mkdir -p ~/.mail/work ; mbsync --pull work`, the initial sync of mails downloads everything to the local machine.
