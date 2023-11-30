#!/usr/bin/env python3
#
# A random Korean name generator
# Statistically plausible random Korean name generator
#
# https://github.com/naltang/korean-name-generator
#
# written by Chang Park naltang@yahoo.com
#

import argparse
import random

# CSV file format:
#
#   A text file of utf-8 encoding.
#   Any line starts with '#' is considered as a comment.
#   One line contains at least two fields.
#   Each field must be delimited by a comma.
#
#   [NAME],[COUNT],[OPTION]
#
#   The first field [NAME] is a name string.
#   The second field [COUNT] is an integer.
#   The third field [OPTION] is a string.

def read_csv(filename_in):
    csv = []
    f = open(filename_in, "rt", encoding="utf-8")
    for line in f:
        line = line.strip()
        if line.startswith("#"):
            continue
        fields = line.split(",")
        if len(fields) < 2:
            continue
        name = fields[0].strip()
        count = int(fields[1].strip())
        option = ""
        if len(fields) > 2:
            option = fields[2].strip()
        csv.append([name, count, option])
    f.close()
    return csv

def generate(filename_family, filename_given, sex="whatever", count=1, delimiter="\n"):
    csv_family = read_csv(filename_family)
    family_populations = [row[0] for row in csv_family]
    family_weights = [row[1] for row in csv_family]

    csv_given = read_csv(filename_given)
    given_populations = [row[0] for row in csv_given if sex=="whatever" or sex==row[2]]
    given_weights = [row[1] for row in csv_given if sex=="whatever" or sex==row[2]]

    family_choices = random.choices(family_populations, family_weights, k=count)
    given_choices = random.choices(given_populations, given_weights, k=count)

    names = [family + given for family, given in zip(family_choices, given_choices)]
    print(delimiter.join(names))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description="Statistically plausible random Korean name generator",
            epilog="https://github.com/naltang/korean-name-generator")
    parser.add_argument ("-f", "--family-names",
            default="family-names.csv",
            help="family names population CSV file, default=family-names.csv")
    parser.add_argument ("-g", "--given-names",
            default="given-names.csv",
            help="given names population CSV file, default=given-names.csv")
    parser.add_argument ("-c", "--count",
            type=int,
            default=1,
            help="number of names to generate, default=1")
    parser.add_argument ("-s", "--sex",
            default="whatever",
            help="sex of names to generate, default=whatever")
    parser.add_argument ("-d", "--delimiter",
            default="\n",
            help="use DELIMITER for name delimiter, default=\\n")
    args = parser.parse_args()
    generate(args.family_names, args.given_names, sex=args.sex, count=args.count, delimiter=args.delimiter)
