#!/usr/bin/env python
# Purpose: say 'Hello, name!'

import argparse 

parser = argparse.ArgumentParser(description="Say hello")
parser.add_argument('name',help='name to greet')
args = parser.parse_args()
print('Hello, ' + args.name + '!') 
