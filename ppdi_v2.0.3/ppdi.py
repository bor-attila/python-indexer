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
        help='Minden mappa indexelése.Minden mappa meg fog jelenni a generált HTML oldalon.'
    )

    parser.add_argument(
        '-d',
        '--disabler',
        default=".",
        help='Megadja az elrejteni kivánt mappák prefixét.'
    )

    parser.add_argument(
        '-s',
        '--styledir',
        default="style",
        help='A Dropbox tárhelyen lévő stilus mappa amely tartalmazza a CSS stiluslapot és a háttérképet.'
    )

    parser.add_argument(
        '-o',
        '--openbrowser',
        default=False,
        action="store_true",
        help='A generálás után a gyökérmappában lévő index.html-t automatikusan megnyitja böngészőben.'
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