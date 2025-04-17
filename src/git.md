# Git

Git is a **version control system.** This allows you to access multiple
**versions** of the same directory on one disk. Git is immensely powerful,
but this page will only cover the basics. If you're looking for a more
in-depth reference, Julia Evans wrote a [very good
introduction](https://jvns.ca/blog/2024/04/25/new-zine--how-git-works-/),
which you can also find in Erica's office.

## Getting Started With Git

If you want to use version control on your own machine (e.g. a coding project
or homework), you can create a **repository,** or a collection of files that
git is able to keep track of and version. There are two relevant ways to
create a repository: Either you're workin with something that somebody's
already made, or you're starting an empty repository. In this first case,
you'll use `git clone`, and in the second, you'll use `git init.`

As an example of the first, you can get the sources for this book with this:

```shell
$ git clone https://github.com/reed-cstar/guides

Cloning into 'guides'...
remote: Enumerating objects: 211, done.
remote: Counting objects: 100% (118/118), done.
remote: Compressing objects: 100% (88/88), done.
remote: Total 211 (delta 54), reused 77 (delta 30), pack-reused 93 (from 1)
Receiving objects: 100% (211/211), 632.06 KiB | 11.92 MiB/s, done.
Resolving deltas: 100% (82/82), done.
```

If you made changes to a repository, and you would like to track and version
them, you can make a **commit**. A commit is the unit by which Git records
changes made to some files. Alongside the content of those changes (including
creations, deletions, and modifications), it also records the author, the
date, and also some optional further metadata regarding the changes.

Before you start **committing** code, you'll need to tell git who you are.
Git provides a clear interface for this with the **config** subcommand. Try
the following, replacing the quoted vale `Your Name` with your name, and
`your.email@example.com` with your email:

```shell
$ git config --global user.name 'Your Name'
$ git config --global user.email 'your.email@example.com'
```

Note the use of the `--global` flag: This instructs git to store a default
value for these settings across all repositores. If you leave it out, git
will associate your name and email only with the repository in your current
working directory, and future invocations of git will use this value to
override any global value that may or may not be set.

Now that git is sufficiently configured and you're in a repository, you can
make some changes to the files and add them to the **staging area** with the **add subcommand:**

```shell
$ git add ./path/to/modified/files
```

> [!NOTE]
>
> You'll often see `git add .`: If run from the root of your repository,
> this'll add all changes to the staging area.

With your changes added, the **commit subcommand** will allow you to add them
to version control:

```shell
$ git commit
```

> [!NOTE]
>
> If you aren't currently in in a repository, `git commit` will tell you with
> the only moderately cryptic error message:
> ```
> fatal: not a git repository (or any of the parent directories): .git
> ```

You'll see that git brings up a **text editor** wherein you can write a
commit message. Most likely, this'll be a text editor called `nano` --- git
will run whatever command you specify in the `$VISUAL` environment variable.
Regardless, writing some text, saving it, and exiting (via
<kbd>Ctrl</kbd>+<kbd>x</kbd> in Nano) will be enough to create a commit, and you'll be dropped back in your shell.
