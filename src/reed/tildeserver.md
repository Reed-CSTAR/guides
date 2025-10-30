# people.reed.edu

people.reed.edu provides static web hosting for Reed students and faculty.
Check some faculty websites for examples of how it can be used:

- Jim has a [pesronal website with some class materials.](http://people.reed.edu/~jimfix/)
- David hosts [the 113 textbook.](https://people.reed.edu/~davidp/113/resources/113full_text.pdf)

You can edit and access people.reed.edu via [FTP](../shell/ftp.md). You can
connect with your Reed ID and usual (Kerberos) password[^official-doc], and,
assuming that your Reed username is `your-username`, your website will be
located in `/home/y/o/your-username/html`. If you `put` an `index.html` file,
it'll show up at `https://people.reed.edu/~your-username` (note the prefixing
tilde!).

[^official-doc]: See also CUS's [info page.](https://www.reed.edu/it/help/sftp.html)
