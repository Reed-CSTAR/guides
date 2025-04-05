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

```
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
