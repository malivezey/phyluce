#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2013 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 27 December 2013 14:12 PST (-0800)
"""


from __future__ import absolute_import

from phyluce.fetch import uce_fastas
from phyluce.common import FullPaths, is_dir, is_file, get_names_from_config


descr = "Given a database, count list, and contigs file, " + \
        "output UCE loci in FASTA format."

def configure_parser(sub_parsers):
    sp = sub_parsers.add_parser(
        'uce-fastas',
        description=descr,
        help=descr
    )

    sp.add_argument(
        '--contigs',
        required=True,
        action=FullPaths,
        type=is_dir,
        help='The directory containing the assembled contigs in which you searched for UCE loci.',
    )
    sp.add_argument(
        '--locus-db',
        required=True,
        action=FullPaths,
        type=is_file,
        help='The SQL database file holding probe matches to targeted loci (usually "lastz/probe.matches.sqlite").'
    )
    sp.add_argument(
        '--match-count-output',
        required=True,
        action=FullPaths,
        type=is_file,
        help='The output file containing taxa and loci in complete/incomplete matrices generated by get_match_counts.py.'
    )
    sp.add_argument(
        '--incomplete-matrix',
        action=FullPaths,
        default=False,
        help='The path to the outfile for incomplete-matrix records.  Required when processing an incomplete data matrix.',
    )
    sp.add_argument(
        '--output',
        required=True,
        action=FullPaths,
        help='The path to the output FASTA file you want to create.'
    )
    sp.add_argument(
        "--verbosity",
        type=str,
        choices=["INFO", "WARN", "CRITICAL"],
        default="INFO",
        help="""The logging level to use."""
    )
    sp.add_argument(
        "--log-path",
        action=FullPaths,
        type=is_dir,
        default=None,
        help="""The path to a directory to hold logs."""
    )
    sp.add_argument(
        '--extend-locus-db',
        type=is_file,
        action=FullPaths,
        help='An SQLlite database file holding probe matches to other targeted loci.'
    )
    sp.add_argument(
        '--extend-locus-contigs',
        type=is_dir,
        action=FullPaths,
        help='A directory holding the assembled contigs (from genomes or another study) referenced by --extend-locus-db.'
    )
    sp.set_defaults(func=get_uce_fastas)

def get_uce_fastas(args, parser):
    uce_fastas.main(args, parser)
