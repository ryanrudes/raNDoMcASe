class SyntaxError(Exception):
  pass

class nOPE(Exception):
  pass

import sys
from termcolor import colored

try:
  filename = sys.argv[1]
  if filename.split(".")[-1] != "raNDoM":
    raise nOPE("iNvaLId fILE eXtENsiOn!")
except:
  print ("""Traceback (most recent call last):
  File "/usr/local/bin/raNDoMcASe_cOmPiLeR.py", line 26, in <module>
    filename = sys.argv[1]
  MissingFilepathError: dO yOU KnoW dA wAY?!?""")

  sys.exit(0)

code = open(filename, "r").read()
print (colored("raNDoMcASe: ", "red") + colored(code, "blue"))

yeets = [caps1('y') + caps2('e') + caps3('e') + caps4('t') for caps1 in [str.upper, str.lower] for caps2 in [str.upper, str.lower] for caps3 in [str.upper, str.lower] for caps4 in [str.upper, str.lower]]
oofs = [caps1('o') + caps2('o') + caps3('f') for caps1 in [str.upper, str.lower] for caps2 in [str.upper, str.lower] for caps3 in [str.upper, str.lower]]

for keyword in yeets:
  code = code.replace(keyword, '>')

for keyword in oofs:
  code = code.replace(keyword, '<')

code = code.replace(' ', '').replace('\t', '').replace('\n', '')

while '(' in code:
  idx_1 = code.index('(')
  code_1 = code[:idx_1]
  idx_2 = code.index(')')
  code_2 = code[idx_2 + 1:]
  code = code_1 + code_2

for c in set(code):
  if c.islower():
    code = code.replace(c, '-')
  elif c.isupper():
    code = code.replace(c, '+')

while '*' in code:
  idx_1 = code.index('*')
  code_1 = code[idx_1 + 1:]
  idx_2 = code_1.index('*')
  code = code[:idx_1] + '[' + code_1[:idx_2] + ']' + code_1[idx_2 + 1:]

def evaluate(code):
  data = [0] * 10
  pointer = 0
  i = 0

  while i < len(code):
    c = code[i]
    if c == '>':
      pointer += 1
    elif c == '<':
      pointer -= 1
    elif c == '+':
      data[pointer] = data[pointer] + 1
    elif c == '-':
      data[pointer] = data[pointer] - 1
    elif c == '.':
      sys.stdout.write(chr(data[pointer]))
    elif c == ',':
      data[pointer] = ord(input())
    elif c == '[':
      if data[pointer] == 0:
        i = code[i + 1:].index(']') + i + 2
    elif c == ']':
      if data[pointer]:
        i = code[:i].rfind('[')

    i += 1
  

print (colored("\nBrain****: ", "red") + colored(code, "blue"))

print (colored("\nOutput:", "red"))
evaluate(code)