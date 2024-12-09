#!/usr/bin/env python
# Purpose: say 'Hello, name!'

import argparse 

parser = argparse.ArgumentParser(description="Say hello")
parser.add_argument('-n', '--name', metavar='name', default='World', help='name to greet')
args = parser.parse_args()
print('Hello, ' + args.name + '!') 
