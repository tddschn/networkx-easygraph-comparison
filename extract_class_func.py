#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-07-05
Purpose: Why not?
"""

import argparse
from pathlib import Path
import re


def extract(
    source: str, remove_private: bool = False, remove_test: bool = False
) -> list[str]:
    output_lines = []
    for line in source.splitlines():
        if ':' in line:
            matching_without_file_path = line.split(':')[1].strip()
        else:
            matching_without_file_path = line.strip()
        matching_without_file_path = matching_without_file_path.removeprefix('class')
        matching_without_file_path = matching_without_file_path.removeprefix('def')
        matching_without_file_path = matching_without_file_path.strip()
        if (
            remove_test
            and re.match(
                r'^(base.*|py)?test[_s]?.*', matching_without_file_path, re.IGNORECASE
            )
            or '_test_' in matching_without_file_path
            or matching_without_file_path.endswith('Tests')
            or matching_without_file_path.endswith('TestBase')
        ):
            continue
        if remove_private and matching_without_file_path.startswith('_'):
            continue
        output_lines.append(matching_without_file_path)
    return output_lines


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Why not?', formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('source', metavar='FILE', help='file to process', type=Path)
    parser.add_argument('-s', '--sort', action='store_true', help='sort lines')
    parser.add_argument('-u', '--unique', action='store_true', help='dedupe the lines')
    parser.add_argument('-o', '--output', help='output file', type=Path)
    parser.add_argument(
        '-i', '--in-place', action='store_true', help='overwrite the file'
    )
    parser.add_argument(
        '-rmp',
        '--remove-private',
        action='store_true',
        help='remove symbols starting with _',
    )
    parser.add_argument(
        '-rmt',
        '--remove-test',
        action='store_true',
        help='remove test classes and functions',
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    source: Path = args.source
    output: Path = args.output
    if not output and args.in_place:
        output = source
    output_lines = extract(
        source.read_text(),
        remove_private=args.remove_private,
        remove_test=args.remove_test,
    )
    if args.unique:
        output_lines = list(set(output_lines))
    if args.sort:
        output_lines.sort()
    output.write_text('\n'.join(output_lines))
    print(f'Processed {str(source)}, saved to {str(output)}')


if __name__ == '__main__':
    main()
