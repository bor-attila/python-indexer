# -*- coding: utf-8 -*-
from dropbox import ppdi as p
import argparse
import sys

def main(argv):

    parser = argparse.ArgumentParser(description='Generate pretty HTML pages from dropbox content')

    parser.add_argument(
        '-l',
        '--lang',
        default="en_US",
        help='Selected language in LanguageCode_Country format. eg: en_US'
    )

    parser.add_argument(
        '-a',
        '--all',
        default=True,
        action="store_false",
        help='Indexing of folders.Each folder will appear on the generated HTML page.'
    )

    parser.add_argument(
        '-d',
        '--disabler',
        default=".",
        help='It sets the prefix of the folders which are to be excluded from indexing.'
    )

    parser.add_argument(
        '-s',
        '--styledir',
        default="style",
        help='The style directory in the Dropbox which contains the CSS stylesheet.'
    )

    parser.add_argument(
        '-o',
        '--openbrowser',
        default=False,
        action="store_true",
        help='It automatically opens the index.html from the root directory'
    )

    parser.add_argument(
        '-q',
        '--quiet',
        default=False,
        action="store_true",
        help='No output'
    )

    args = parser.parse_args()

    settings = {
        "lang"             : args.lang,
        "hidesomeitem"     : args.all,
        "hider"            : args.disabler,
        "styledir"         : args.styledir,
        "openafterindex"   : args.openbrowser,
        "quiet"            : args.quiet
    }

    ppdi = p.Indexer(settings)
    ppdi.start_build()

if __name__ == "__main__":
    main(sys.argv[1:])