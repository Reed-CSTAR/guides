# FTP

**FTP** (an initialism of **F**ile **T**ransfer **P**rotocol) can be used to
send files between computers.

<div style="text-align: center">
<a href="https://xkcd.com/949">

![xkcd 949, depicting a common situation in which a frequent computer-toucher
is entirely unable to send files between two computers.](./ftp-xkcd.png)

</a>
</div>

FTP requires that the person or computer that you're meaning to send files to
is running an FTP server. For an example of such a case, consider
people.reed.edu. The remainder of this guide assumes that you have a file named
`index.html` in the current working directory that you'd like to upload to people.reed.edu to set up your website.

## Using FTP on Linux and MacOS

You have an FTP client built in. Connect to a server over **SFTP** (the "S"
stands for "Secure") like in the following:

```bash
$ sftp <your-username>@people.reed.edu
<your-username>@sftp.reed.edu's password:
```

After logging in with your usual credentials, you get a stripped down command
prompt. You can use `ls` and `pwd` to get your bearings:

```
Connected to sftp.reed.edu.
sftp> ls
html
sftp> pwd
Remote working directory: /reed.edu/home/y/o/your-username
```

`cd` works as per usual, e.g.:

```
> cd html
sftp> pwd
Remote working directory: /reed.edu/home/y/o/your-username/html
```

Now, you have a few extra commands: `get` will download files, and `put` will upload them. If you have a file named `index.html`,

```
> put index.html
```

will upload it to the server.

## Using FTP on Windows

This section is TODO.
