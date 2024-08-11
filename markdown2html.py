#!/usr/bin/python3
"""Markdown to HTML"""
import sys
import os


def headingParse(line):
    """Parse heading markdown lines to appropriate HTML."""
    if line.startswith("# "):
        return("<h1>{}</h1>".format(line[2:]))
    elif line.startswith("## "):
        return("<h2>{}</h2>".format(line[3:]))
    elif line.startswith("### "):
        return("<h3>{}</h3>".format(line[4:]))
    elif line.startswith("#### "):
        return("<h4>{}</h4>".format(line[5:]))
    elif line.startswith("##### "):
        return("<h5>{}</h5>".format(line[6:]))
    elif line.startswith("###### "):
        return("<h6>{}</h6>".format(line[7:]))
    else:
        return

def listParse(line):
    """Parse list markdown to appropriate HTML."""
    if line.startswith("- "):
        return("<ul>\n<li>{}</li>\n</ul>".format(line[2:]))
    elif line.startswith("* "):
        return("<ul>\n<li>{}</li>\n</ul>".format(line[2:]))
    else:
        return
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]

    if not os.path.exists(inputFileName):
        print("Missing {}".format(inputFileName), file=sys.stderr)
        exit(1)
    else:
        with open(inputFileName, 'r') as file:
            with open(outputFileName, 'a') as outFile:
                for line in file:
                    outFile.write(headingParse(line.strip())+"\n")
                    if line.startswith("- ") or line.startswith("* "):
                        while line.startswith("- ") or line.startswith("* "):
                            (listParse(line.strip())+"\n")
                            line = next(file)