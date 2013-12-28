#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2013 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 27 December 2013 13:12 PST (-0800)
"""

from __future__ import absolute_import
import sys

from phyluce.cli import sub_fetch_uce_contigs
from phyluce.cli import sub_fetch_uce_counts
from phyluce.cli import sub_fetch_uce_fastas


descr = "Fetch (AKA get) UCE contigs from assembled data."


def configure_parser(sub_parsers):
    if len(sys.argv) == 2:
        sys.argv.append("-h")
    p = sub_parsers.add_parser(
        'fetch',
        description=descr,
        help=descr
    )

    sub_parsers = p.add_subparsers(
        metavar = "command",
        dest = "cmd",
    )

    sub_fetch_uce_contigs.configure_parser(sub_parsers)
    sub_fetch_uce_counts.configure_parser(sub_parsers)
    sub_fetch_uce_fastas.configure_parser(sub_parsers)
