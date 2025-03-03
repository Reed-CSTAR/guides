# Useful Commands

The command line can make it fairly difficult to discover new tools. If you're
going to know that anything exists, you have to read about it somewhere. What
follows, then, is a list for your reference of a whole bunch of things you may
want to refer to.

Unless otherwise noted, these commands work in roughly the same way. They take
some input from a file specified as a command line argument, perform some
operation, and output the result to the console. If you're ever unsure how a
specific command works, try running it with `-h` to get a help message. If that
doesn't work, try `--help`. If *that* doesn't work, see the section on [getting
help](/).

Once you're done familiarizing yourself with the essentials, go on to learn some
[scripting techniques](./scripting.html).

## Essentials

| Command | Description |
|---------|----|
| `cd`    | Change the current working directory. |
| `ls`    | List the files in the current working directory. You can also give it a target directory to list from, e.g., `ls ./example`. |
| `ls -l` | List the files in the current working directory, but with a little more information. |
| `cat`   | Con**cat**enate files, or, with one argument, print a file to the console. |
| `head`  | Get the first couple lines of a file. |
| `tail`  | Get the last couple lines of a file. |
| `grep <pattern> <file>` | Output all lines in `file` that contain `<pattern>` |

## Some Stuff More

You'll run these less often, but it can still be good to know they exist.


| Command | Description |
|---------|----|
| `tail -f` | Watch a file and output new lines as they're written to it. This can be useful for things like logs that are written to by another process over time. |
| `wc -l` | Count the number of lines in stdin or from a file. |
| `wc -c` | Count the number of characters in stdin or from a file. |
| `wc -w` | Count the number of words in stdin or from a file. |

## Some Options

A lot of the above commands are very old (`cat`, e.g., descends from 1971), and
therefore has some characteristics you may or may not like. These are really
beyond the scope of the basics here, but if you find yourself curious, there are
some potentially preferable replacements for the old tools if you're looking to
play around a bit:

| Command   | Replacement |
|-----------|-------------|
| `cat`     | `bat`       |
| `cd`      | `zoxide`    |
| `find`    | `fd`        |
| `grep`    | `ripgrep`   |
| `ls`      | `eza`       |
| `nano`    | `micro`     |