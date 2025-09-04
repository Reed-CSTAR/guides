#!/usr/bin/env python3

import json, sys

def fixupsection(sect):
    if 'Chapter' not in sect:
        return sect

    content = sect['Chapter']['content']
    
    in_code_fence = False
    new_content = ""
    for line in content.split('\n'):
        if line.startswith('```'):
            in_code_fence = not in_code_fence

        # Hacky quick fix to keep this script from messing up tables and code
        # blocks. We'll use a proper markdown parser eventually.
        if not line.startswith('|') \
           and not in_code_fence:
            line = line.replace('---', '&mdash;')

        new_content += f'{line}\n'

    sect['Chapter']['content'] = new_content
    sect['Chapter']['sub_items'] = [fixupsection(sect) for sect in sect['Chapter']['sub_items']]

    return sect

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'supports': sys.exit(0)

    context, book = json.load(sys.stdin)

    book['sections'] = [fixupsection(sect) for sect in book['sections']]
    json.dump(book, sys.stdout)
