# Navigation

You're probably used to files and folders as they show up on your desktop. You
can drag them around, put them in other folders, and so forth. As it turns out, the
command line gives you access to the exact same thing.

The simplest command that interacts with your files is `pwd`. This stands for
"print working directory," and if you run it, you'll see your current working
directory:

```bash
$ pwd
/home/user
```
> Your output may be different if you're on MacOS, but it should have a similar
> form.

This is a very important concept: Every shell always has a **working
directory** and you can always check what it is with `pwd`. A working directory
is itself not too strange a concept: If you open up your files app, you'll see
you're looking at some files. You can click on a directory to see the files and
folders in that folder, and keep going however long you'd like. It's the same
thing here. To see everything that's in your current directory, run `ls`:

```bash
$ ls
Desktop Documents Downloads go Mail Music Pictures Public Templates Videos
```

> This is just some possible output. You might have some or none of these
> folders on your own computer.

Just like in your <abbr title="Graphical user interface, as opposed to the
command line interface (CLI) that you're currently using.">GUI</abbr> files app,
you can change your working directory. To do so, use the `cd` command:

```bash
$ cd Documents
```

You'll notice that nothing happened. However, run `pwd` again and you'll see
you're somewhere else:

```bash
$ pwd
/home/<your-username>/Documents
```

As before, you can run `ls` to see all your documents:

```bash
$ ls
essay.txt cstar-guide.html shoelaces.pdf
```

> Again, this is just example output. Yours is (presumably!) not quite the same.

The so-called **parent directory** of your working directory is referred to with
`..`. This means that after you `cd` into `Documents`, you can get out just as
easily:

```bash
$ pwd
/home/<your-username>/Documents
$ cd ..
$ pwd
/home/<your-username>
$ cd Documents
$ pwd
/home/<your-username>/Documents
```

`ls` is a command you'll be using a lot, so it's worth spending a little bit of
time on it. Just like with `echo`, `ls` can take arguments. Try using the `-l`
argument for a *long listing:*

```bash
$ ls -l
-rw-r--r--. 1 user group    0 Jan 24 12:13  essay.txt
-rw-r--r--. 1 user group   45 Jan 28 19:00  cstar-guide.html
-rw-r--r--. 1 user group 100M Jul 22  2024  shoelaces.pdf
```

> An argument that begins with a `-` is usually called a **flag.**

Reading the output right-to-left, you'll see that we have the filenames just as
before. Then, we have the time the files were last modified, preceded by their
size. In this example, `essay.txt` is entirely empty. `cstar-guide.html` takes
up 45 bytes of space, and the M in the `100M` taken by `shoelaces.pdf` stands for
megabytes. We'll come back to the rest of the output later, in the section on
file permissions.

The `echo` command can actually be used to create files. Try, for instance, the
following:

<div class="warning">
Make sure you don't already have a file named `a.txt` in your current
working directory. This command will overwrite that file!
</div>

```bash
$ echo "Hello!" > a.txt
```

This `>` is called a redirect, and takes the output of the command (which would
normally just be "Hello!") and writes it to a file instead.

Now, if you run `ls` again, you'll see the same output as before, with one
addition:

```bash
$ ls
a.txt essay.txt cstar-guide.html shoelaces.pdf
```

Now that you have that file saved to your disk, the `cat` command will let you
see the contents:

```bash
$ cat a.txt
Hello!
```

The greatest sin of the command line environment is that `cat` has nothing to do
with actual cats, and instead is an abbreviation of concatenate. You can pass
two or more filenames as arguments to `cat`, and you'll be able to see them
both, one after the other:

```bash
$ echo "Goodbye!" > b.txt
$ cat a.txt b.txt
Hello!
Goodbye!
```

Redirections work on every command, `cat` included. Try this:

```bash
$ cat a.txt b.txt > c.txt
```

Now, `c.txt` has the same content as `a.txt` and `b.txt` combined, and if you
`cat` it, you'll see what you expect:

```bash
$ cat c.txt
Hello!
Goodbye!
```

By the way, you can't just `cat` any arbitrary file. Consider, for example,
`shoelaces.pdf`. This thing is 100M, and, being a PDF, it probably has all sorts
of information about formatting, page size, and so forth that just isn't
expressed as plain text. It's usually inadvisable to `cat` these to your
terminal, unless of course you're redirecting the output to a file.

> If you want, you can look for a binary file like an image or a PDF with `ls`
> and `cd`. Then, `cat` it. You'll see a stream of nonsense pour over your
> terminal window. Press <kbd>Ctrl+C</kbd> to interrupt the command. You
> probably won't see your usual prompt anymore. Nevertheless, type `reset` and
> press <kbd>Enter</kbd>. It'll take a couple seconds, but your shell will come
> back just as before.

You probably want to get rid of `a.txt`, `b.txt`, and `c.txt` now. You can do
that from the command line as well:

```bash
$ rm a.txt b.txt c.txt
```

Maybe you want to look for any other `.txt` files just in case you missed some.
This can be achieved with a *glob:*

```bash
$ ls *.txt
essay.txt
```

> Your output might be empty if you have no files that match this string. Try
> playing around with other globs. For instance, `*a*` matches any file with an
> `a` in the name.

Now that you know how to create and remove files, it's good to do the same for
directories. The `mkdir` command does the first:

```bash
$ mkdir test-directory
```

And rm does the second:

```bash
$ rm -r test-directory
```

Notice the `-r` flag. This causes a **recursive removal.** That is, you're not
just removing the directory you specify (here, that's `test-directory`), but
also all the files and folders inside. Be very careful with this command. Unlike
the normal files app, there's no trash can to restore from!

Now that you can make and remove files and folders, you've already mastered
about half of the command line. Next up are some niceties in line editing.
