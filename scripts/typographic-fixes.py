#!/usr/bin/env python3

import json, sys

def fixupsection(sect):
    if 'Chapter' not in sect:
        return sect

    sect['Chapter']['content'] = sect['Chapter']['content'].replace('---', '&mdash;')

    return sect

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'supports': sys.exit(0)

    context, book = json.load(sys.stdin)

    book['sections'] = [fixupsection(sect) for sect in book['sections']]
    json.dump(book, sys.stdout)
