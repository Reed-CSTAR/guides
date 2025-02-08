# File Permissions

We'll take another look at the output of `ls -l`:

```shell
$ ls -l
drwxr-xr-x. 1 user group 451M Jul 22  2024  Documents
-rw-r--r--. 1 user group    0 Jan 24 12:13  essay.txt
-rw-r--r--. 1 user group   45 Jan 28 19:00  cstar-guide.html
-rw-r--r--. 1 user group 100M Jul 22  2024  shoelaces.pdf
```

When you run this, you likely won't see `user` or `group`. Instead, you'll
likely see your computer username in that first column and something like it in
the next. These are the names of a **user** and of a **group,** respectively. In
all likelihood, these are the names of *your* user and *your* group.

The systems we're using — Linux, MacOS, or WSL on Windows — all descend from an
operating system called [UNIX](https://en.wikipedia.org/wiki/UNIX), which
achieved success in part due to its **multi-user** support. On our personal
computers, we don't generally use multi-user features all that frequently or
explicitly, but they're baked in to the computer so much that, in fact, every
single file is **owned by** one of many **users,** and, simultaneously, one of
many **groups.**

If you want to know what your user is called, you can always run `whoami`:

```shell
$ whoami
atalii
```

> [!NOTE]
> This is just my personal username. Yours will be different!

Similarly, `groups` can tell you what groups you're a member of:

```shell
$ groups
atalii wheel input
```

> [!NOTE]
> Again, this is just the output on my machine. You'll probably be a member of
> some different groups. You don't need to worry about what each one is for
> right now.

This is the basis for the **UNIX permission model:** Every file has three sets of
permissions. First, the owning user can read the file, write the file, or
execute the file. Then, a different set of permissions (one, none, or all of
reading, writing, and executing) apply to a user who is not the owner but is in
the owning group. Then, there's a third set of permissions for everyone else.

This is actually what you see in the leftmost column of the long listing. The
first letter (above, this is either `-` or `d`) indicates the kind of file this
is. `-` indicates that it's just a normal file, and `d` indicates it's a
directory. Then, there are three characters describing what the owning user can
do. The first of these three indicates whether or not the
owner can read the file (`r` if they can, `-` if they can't), the second (`r` or
`-`) indicates whether they can write to the file, and the third (`x` or `-`)
indicates whether or not they can execute this file. We have another group of
the same three that describe permissions for members of the owning group, and a
final group of three that describe permissions for everyone else.

If this feels a bit abstract, we can actually see these permissions working with
a few commands. You can create a file with the `touch` command:

```shell
$ touch perm-example.txt
```

> [!NOTE]
> This command has no output. One of the recurring themes in CLIs is that if
> they don't complain, you're probably safe to assume that nothing's gone wrong.
> You can run `echo $?` to see the **exit code** of the process, which will
> always be 0 if it's successful.

Now, look at how `perm-example.txt` has been created:

```shell
$ ls -l perm-example.txt
-rw-r--r--. 1 atalii users 0 Feb  6 08:29 perm-example.txt
```

We can see that in this case, the owning user is `atalii`, and the owning group
is `users`. `atalii` has the `rw-` perms associated: They can read from and
write to the file. Anyone in the users group can read the file but do nothing
else, as indicated by `r--`. And, with the same `r--` repeated, anyone outside
the owning group can only read the file.

Let's take a closer look at what exactly this all means. To be able to read from
a file means you're allowed to look at the contents, which, in this case, are
empty:

```shell
$ cat perm-example.txt
```

To be able to write to a file means you're able to modify its contents. Try
this:

```shell
$ echo "I can write to this file!" >> perm-example.txt
```

> [!NOTE]
> Notice that we use `>>` here instead of `>` as we used previously. The
> difference is that `>` will always **overwrite** a file, replacing the
> contents with whatever it wants. By contrast, `>>` **appends** to the file,
> leaving alone whatever was there previously.

Now, if you read it again, you'll see that line of text:

```shell
$ cat perm-example.txt
I can write to this file!
```

Execution may, unfortunately, be a bit more mistifying. We'll explore what it
means for a file to be executable in more detail when we talk about compiling
code or, in this chapter, [writing scripts](./scripting.html). For now, it's
enough to say that lots of the commands we've been using (`cat`, `ls`, `touch`,
and so forth) are actually files on disk just like everything else. Because we
can run them as commands, then, we know they're executable.

There's one last meaning to "executability" that should concern you, and that's
executability for directories. If you'll recall the example at the beginning, my
documents folder can be read, written, and executed by me, while it can only be
written and executed by anyone else. Here, execution does not actually mean
execution. Instead, it means that a user with executable permissions on the
directory can `cd` into it.

This permission system would only be so useful if you couldn't change
permissions. Fortunately, you can use the `chmod` command to change permissions.
While there's some more advanced usages we won't cover here, the basics are
good to know. Before we discuss exactly what this command does, try it out:

```shell
$ chmod ugo-r perm-example.txt
```

Now, if you try to read perm-example.txt, you should see an error:

```shell
$ cat perm-example.txt
cat: perm-example.txt: Permission denied
```

If you check perms with `ls -l`, you'll get a good idea of what that `chmod`
command did:

```shell
$ ls -l perm-example.txt
--w-------. 1 atalii atalii 0 Feb  6 08:29 perm-example.txt
```

You'll see that you only have write permissions to the file. You can actually
test that if you'd like:

```shell
$ echo "test" > perm-example.txt
```

Remember, you don't have read permissions on this test file, so if you try to
`cat` it, you'll get that same error. Instead, you have to give yourself read
permissions:

```shell
$ chmod u+r perm-example.txt
$ cat perm-example.txt
test
```

Hopefully you can start guessing at what the arguments to `chmod` do. You can
give or take permissions with `+` or `-`. These permissions can be `r`, `w`, or
`x`. So, for instance, to give everyone executable permissions, you can run
`chmod +x` on a file. If you want only the owning **u**ser to get those
executable permissions, however, run `chmod u+x`. You can put any combination of
`r`, `w`, or `x` on the right hand side, and any combination of `u`, `g`, or `o`
on the left hand side, for the owning **u**ser, the owning **g**roup, or
**o**ther users.

`chmod` can be run on a file by the owning user, but it can also be run on
any file by the **root user:** This is a special system account meant for use in
modifying and administering the system, so it (or somebody logged in as this
root user) can change permissions, read, write, and modify nearly any file.

Let's say that we've decided that perm-example.txt is an incredibly important
file for the functioning of your computer, and we therefore want to make it
accessible only to the specially-privileged root user. This requires two new
commands: `chown`, and `sudo`.

```shell
$ sudo chown root:root perm-example.txt
$ ls -l perm-example.txt
-rw-------. 1 root root 5 Feb  6 09:18 perm-example.txt
```

`sudo` will probably give you a very scary prompt and ask for for your password.
Once you confirm that you are indeed the user you're logged in as, `sudo` will
pretend you're root to run the real command, which is `chown root:root
perm-example.txt`. As the name suggests, this **ch**anges **own**ership of the
file `perm-example.txt` to be owned by the root user and the root group, and, as
we can see from the output of `ls -l`, only root can read and write.

Once you decide you no longer need this file, you can remove it, but only as the
root user. So, you'll have to use `sudo` again:

```shell
$ sudo rm perm-example.txt
```

> [!CAUTION]
> The note before about being careful with rm goes double for sudo rm. If you
> make a mistake, you can use this command to really break some things.

With this and some practice, you're well on your way to being comfortable on the
command line. Next up are some topics in configuration before covering a small
amount about scripting.
