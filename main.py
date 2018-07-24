from scramble import scramble
from sys import stdout
import argparse


parser = argparse.ArgumentParser(prog='Sarcmlebr', usage='Given a file or some text, it scramble the middle letters of the words and prints the output to stdout')
parser.add_argument('--text', help='Text to scramble', type=str, default=None)
parser.add_argument('--file', help='File to scramble', type=str, default=None)
args =  parser.parse_args()

if args.text is None and args.file is None:
    print('Please specify either the --file or --text argument !')
    exit(202)

if args.text is not None and args.file is not None:
    print('Please specify either the --file or --text argument, not both !')
    exit(202)


if args.text is not None:
    original_text = args.text
else:
    with open(args.file, 'r', encoding='utf-8') as f:
        original_text = f.read()

stdout.buffer.write(scramble(original_text).encode('utf8'))
stdout.buffer.write(str('\n').encode('utf8'))
stdout.flush()
