# Line Editing

As you might have noticed, using the command line can involve repeating yourself
a lot. Bash itself actually helps you avoid most of the manual repetition by
keeping track of your **command history.** You can see this for yourself:
There's a file in your home directory called `.bash_history` on Linux and WSL or
`.zsh_history` on MacOS which stores all the commands you've run in a given
**terminal session.**

Close your terminal window and open a new one. Then, look for this file:

```shell
$ ls -h
```

Because this filename starts with a `.`, your history file is actually a
**hidden file,** and you need the *-h* flag in `ls` to see it. Now, once you
know if you have `.bash_history` or `.zsh_history`, check what's in it:

```shell
$ cat .bash_history # or .zsh_history!
```

By the way, you almost certainly have some other hidden files in this directory.
Recall that the command for seeing those is `ls -h`, but you've already run it.
Press the up arrow to cycle through your previous commands. First you'll see
`cat .bash_history`, then `ls -h`. Bash will let you get through your entire
history this way! Play around with the command line a little bit. Scroll up,
modify a command, and run it. To modify a command, your normal keyboard
shortcuts won't all work. You can likely use the arrow keys to move your cursor
over the line, but there are some other, more shell-specific shortcuts that you
may want to use.

| Shortcut          | Action                                                |
|-------------------|-------------------------------------------------------|
| <kbd>Ctrl+H</kbd> | Delete the last character.                            |
| <kbd>Ctrl+W</kbd> | Delete the last word.                                 |
| <kbd>Ctrl+A</kbd> | Go to the start of the line.                          |
| <kbd>Ctrl+E</kbd> | Go to the end of the line.                            |
| <kbd>Ctrl+F</kbd> | Go to the next character.                             |
| <kbd>Ctrl+B</kbd> | Go to the last character.                             |
| <kbd>Alt+F</kbd>  | Go to the next word.                                  |
| <kbd>Alt+B</kbd>  | Go to the last word.                                  |
| <kbd>↑</kbd>      | Go to the previous (less recent) item in the history. |
| <kbd>↓</kbd>      | Go to the next (more recent) item in the history.     |

> Most of these shortcuts are taken from a very old, decrepit piece of software
> called **Emacs.** You can see key bindings that look like this pretty much
> everywhere if you know where to look.

One last convenience: You can use <kbd>Ctrl+R</kbd> to search through your
command history. You'll see something like this:

```
(reverse i-search)`':
```

Typing will match through your history in real time. You can use <kbd>↑</kbd>
and <kbd>↓</kbd> to look through the matches, and edit the result just like
normal.
