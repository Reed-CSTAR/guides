# Basics

Bash operates under some fairly foreign principles when compared to the rest of
the software you might use on a daily basis. It doesn't work how you expect —
<kbd>Ctrl+C</kbd> doesn't copy and <kbd>Ctrl+V</kbd> doesn't paste, for instance
— but it's got plenty of conventions that are carried through into other tools
you might end up using, so it's worth taking the time to play around a bit. Try
entering this into your shell:

```shell
$ echo "Hello!"
Hello!
```

> [!NOTE]
> Only type the text after the `$`. Then, press enter, and you should see the
> same output on your screen as you see in the text above.
>
> The `$` here represents your **prompt.** It might look a little different in
> your terminal, but it probably ends in a `$`, so that's the character most
> commonly used to represent it in documentation.

`echo` simply repeats whatever you give it. Despite what it looks like, there's
actually a lot going on here. Try the next two commands:

```shell
$ echo "Hello," "world!"
Hello, world!
$ echo "Hello, world!"
Hello, world!
```

These two commands are different, but they produce the same result. This comes
down to two very important concepts in Bash that you'll come into contact with
again and again: **commands** and **arguments.** In the above, we can say that
**you ran the command** `echo "Hello!"`, but we can also say that **the command
you ran** was `echo`, and the **argument** was `Hello!`. This is the difference
between `echo "Hello," "world!"` and `echo "Hello, world!"`. The first has just
two arguments, and the second has just one. The command `echo` just happens to
display all of its arguments together, putting a space in between them.

By the way, the quotes are strictly optional. All of the commands below have the
same output. Try them!

```shell
$ echo "Hello," "world!"
Hello, world!
$ echo Hello, "world!"
Hello, world!
$ echo "Hello, world!"
Hello, world!
$ echo Hello, world!
Hello, world!
```

Even though these are all the same, it's generally considered good practice to
quote arguments. To see why this is, try this command, and guess what the output
might be:

<!-- Syntax highlighting intentionally disabled here. The grayed out comment is
  -- a bit too much of a hint. -->
```
$ echo Sorry. All the microchips are gone. I got #hungry.
```

You'll notice that the final `#hungry` doesn't display! What's going on here? It
turns out that bash treats everything in a line after the `#` character to be a
comment: It's entirely ignored. You can use this to write out prose descriptions
of what your commands do:

```shell
$ echo "Hello" # Print a greeting to the display.
```

This command has three parts: There's the command itself (`echo`), the argument
(`Hello`), and the comment (everything after the `#`). What if you really want
to echo a `#`, though? Quoting will help you here:

```shell
$ echo "Sorry. All the microchips are gone. I got #hungry."
Sorry. All the microchips are gone. I got #hungry.
```

These ideas of arguments, comments, and commands make up very much of the
command line that you'll be interacting with, but you'll be using some more
commands than just `echo`. Go on to [navigation](./navigation.html) for some
more useful techniques.
