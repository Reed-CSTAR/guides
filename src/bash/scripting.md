# Scripting

The first and most important rule for writing Bash scripts is that you
shouldn't. However, some concepts of Bash scripts matter a lot in most any
interaction with the shell. Let's start simple by describing variables:

```console
$ echo $HOME
/home/atalii
$ echo $PATH
"/bin:/sbin:/usr/bin:/usr/local/bin:...
```

Here, you've asked Bash to give you the values of two variables, `$HOME`, and
`$PATH`. You might recognize `$HOME` as the path of your home directory (it's
what'll show up if you run `pwd` in a new terminal), but `$PATH` is new: Instead
of being one path, it's actually a `:` separated list of paths. You probably see
the string `bin` in here quite a bit: This is because `PATH` lists the locations
of certain kinds of binary files, or, as you may already know them, executables.
For instance, you can run:

```console
$ which cat
/usr/bin/cat
```

and you'll see that the `cat` command is actually a file located in `/usr/bin`.
Check the output of the `echo` command above, and you'll likely see that
`/usr/bin` is in your `$PATH`.

> [!NOTE]
> Some systems will have `cat` at `/bin/cat`, or maybe `/sbin/cat`. If your
> output is slightly different, that's okay. The same principle applies.

Were `$PATH` just a static list of paths, it wouldn't be so useful. However, you
can put whatever directory you want in there.

We'll demonstrate this by creating a command of our own. Using a text editor of
your choice, make a file in your home directory named `foo.sh` with the
following contents:

```bash
#!/usr/bin/env bash

echo foo
```

The line that begins with a `#!` is called a **shebang,** and tells the
operating system that it can run this script with bash. Now, make it executable:

```console
$ chmod +x home.sh
```

If this command succeeds (and it should!), you'll be able to run it:

```console
$ ./foo.sh
foo
```

Note that we're referring to the file by qualifying its path with that of the
current directory. We can't just use `foo.sh` without the `./`, otherwise Bash
won't know that this is a file in the current directory. Instead, it'll look
through `$PATH`, find nothing named `foo.sh`, and complain:

```console
$ foo.sh
bash: foo.sh: command not found
```

However, we can set `$PATH` to include the directory in which `foo.sh` lives, and
thereby let Bash run it just like any other command.

```console
$ export PATH="$PATH:$HOME"
$ foo.sh
foo
```

The first command here is the one that does the work. It **sets** the `$PATH`
variable equal to the value of `$PATH` followed by a colon, in turn followed by
the value of `$HOME`, thus adding `$HOME` to list. Now, you can run every
executable in your home directory just like anything else.

> [!WARNING]
> Adding your `$HOME` directory to `$PATH` would make a lot of people angry and
> be widely regarded as a bad move. Part of the concern is security: While it
> takes elevated permissions to put an executable in `/bin`, `/usr/bin`, or the
> like, you only need your permission to put something in `$HOME`: If your user
> is compromised, or you download a suspicious file and put it in `$HOME` for
> later, you might end up running something malicious on accident.
>
> More practically, though, it's just regarded as kind of a messy practice.
> Binaries are best off being put in places well-marked for them: e.g., `/bin`.
>
> If you don't like this: Don't worry, your changes above only matter in
> your current shell session: Close your terminal or open a new one and
> your path will be back to normal.

Regardless, there are some nuances in the command above to examine. Start by
creating a dummy variable to experiment with:

```console
$ export FOO="bar"
```

If you're really enthusiastic about foo, you might even want two of them:

```console
$ echo "$FOO $FOO"
bar bar
```

This is basically the same kind of concatenation operation we did with `$PATH`,
but notice the following doesn't work:

```console
$ echo '$FOO $FOO'
$FOO $FOO
```

Like with comments, you can use single quotes to avoid **interpolating
variables.** In double quotes, Bash will read `$` as letting it know that the
following characters are the name of a variable: In single quotes, however, `$`
is just another character.

> [!NOTE]
>
> By convention, variables in Bash are written in `UPPER_CASE`.

For some reason, let's say you really like `$FOO` and want to save it:

```console
$ export MY_FAV_VAR="My favorite variable is: $FOO."
$ echo "MY_FAV_VAR"
My favorite variable is: bar
```

Note that the kind of interpolation bash does is very flexible: Wherever double
quotes can appear, you can use and manipulate variables.

Scripting in Bash is a very finnicky topic: Variables are really just the tip of
the iceberg. Much like many other programming languages, you can use loops,
functions, and conditional statements. For an example of some more involved
scripting, check out a hidden file in your home directory called `~/.bashrc`:
This is run every time you open your shell, and is usually populated with some
interesting knobs you can turn by editing the file and opening a new shell (or
by sourcing `~/.bashrc` with the `.` command).

Ideally, you're now comfortable in the shell and have a good grasp of the kinds
of things it can do: If not, don't worry! As always throughout this guide,
experience is the best way to learn. Everything will become easier with
repetition, practice, and conversations with other computer-touchers. Enjoy!
