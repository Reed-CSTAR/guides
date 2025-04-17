# SSH

**SSH,** being an initialism for **S**ecure **SH**ell, is a set of **programs**
and **protocols** that allow a user to access a shell on a remote device.

> [!NOTE]
> Throughout this guide, we'll use an example machine named
> [Empanada](/reed/machines.html#the-dumplings), which is available by email
> request to [CSTAR](mailto:cstar@groups.reed.edu) for Reed students.

As a **protocol,** SSH is a standardized method for two computers to
communicate with each other. One computer, an SSH **server,** allows
**clients** to **authenticate** themselves and, once authenticated, run
commands on the server. Unless you're setting up a machine, you'll usually
interact with this protocol from the perspective of the client, so that's what
we'll cover here. The usual SSH flow will look something like below, where I
log in to one of the Reed computers from my own laptop:

```shell
atali@my-laptop:~$ hostname
my-laptop
atali@my-laptop:~$ ssh atali@empanada.reed.edu
atali@empanada:~$ hostname
empanada
atali@empanada:~$ exit # or press Ctrl+D
atali@my-laptop:~$ hostname
my-laptop
```

> [!NOTE]
> Some things here, like my hostname, are specific to my computer. Others,
> like, `empanada.reed.edu`, are only accessible on the Reed network. If you'd
> like to follow along, send an email to CSTAR to get access to [some
> machines](../../reed/machines.html).

Notice a new command: `hostname` tells you the name of the device your shell is
running in. Every machine is given one of these names, and it's helpful to have
a human-recognizable identifier for each computer. Then, the second new
command, `ssh`, logs in to `empanada.reed.edu` as the user `atali` and opens up
a shell. Once we're in the shell, we can see that this machine's hostname is
`empanada`, and we run the `exit` command to close this shell and get back into
the client. We then confirm that we're there with one last invocation of the
`hostname` command.

## Setting This up for Yourself

> [!NOTE]
> We recommend following along to get some practical experience. Contact CSTAR
> for access to some machines with an SSH server enabled.

Once an SSH server is aware of your existence, there are actually many ways to
authenticate to it. You'll probably only come across the two most common ones,
however:

1. **Password-based** authentication.
2. **Key-based** authentication.

These both work about as you'd expect. If the server is configured to accept
password-based auth (and some other requirements are met), SSH will prompt you
for your password:

```shell
atali@my-laptop:~$ ssh atali@empanada.reed.edu
atali@empanada.reed.edu's password:
atali@empanada:~$ # We're logged in!
```

When you type in your password, nothing will appear on screen. Once you've
typed it correctly, pressing enter sends it off to the server to be checked,
and, if correct, you'll find yourself logged in.

Despite being simple, password-based authentication is generally not preferred
to key-based authentication. This authentication method revolves around a **key
pair** that you generate on your own device. This consists of a **public key**
and a **private key** --- you keep the private key secret, but the server gets
your public key. Via some witchcraft, if another party has your public key,
they can confirm that you know your private key without ever knowing what that
private key precisely is. This is unfortunately a slightly more involved
process to set up, but leads to a more convenient and secure SSH login process
later.

We'll start by creating a keypair. On your SSH client machine, run `ssh-keygen`

```shell
$ ssh-keygen
Generating public/private ed25519 key pair.
Enter passphrase for "id_ed25519" (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in id_ed25519
Your public key has been saved in id_ed25519.pub
The key fingerprint is:
SHA256:QtXVxq6HOFptCucsULsI2bH3Tp0t4Xj6MO0BeThtfQI tali@thing-in-itself
The key's randomart image is:
+--[ED25519 256]--+
|        .. ..o   |
|       .  .   +  |
|      .     Eo   |
|     .. .  + o.  |
|     o.+S.=o=oo .|
|    o +.+ =X=+.o |
|     . + X=+O..  |
|      . +.=* o   |
|         oo.o    |
+----[SHA256]-----+
```

Fortunately, you only have to make one decision, and that's whether to protect
your private key with a password. In some circumstances, you may prefer this,
but it's also acceptable to leave it blank. Then, it gives you some
information about your key. Pay particularly close attention to the fact that
two new files have been created: `id_ed25519` and `id_ed25519.pub`.
`id_ed25519` is your private key, and `id_ed25519` is your public key. This
information is enough to set up key-based SSH authentication:

```shell
atali@my-laptop:~$ cat ~/.ssh/id_ed25519.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMPdyjTGPE4WBxR75SJrOHs60flkRqJIyiNr7GNC8OcV atali@my-laptop
atali@my-laptop:~$ ssh atali@empanada.reed.edu
atali@empanada.reed.edu's password:
atali@empanada:~$ echo 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMPdyjTGPE4WBxR75SJrOHs60flkRqJIyiNr7GNC8OcV tali@thing-in-itself' >> ~/.ssh/authorized_keys
atali@empanada:~$ exit
atali@my-laptop:~$ ssh atali@empanada.reed.edu
atali@empanada:~$ # Notice how you haven't been asked for a password: SSH is automatically using your key!
```

All you're doing is adding your SSH public key to a file of **authorized
keys,** which the SSH server can scan to let you in.

If this is confusing, don't worry. The best way to understand this is to do it.
If you want practice, email [CSTAR](mailto:cstar.groups.reed.edu) for access to
our machines.
