#!/usr/bin/python3
"""Markdown to HTML"""
import sys
import os

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
        exit(0)
