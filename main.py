
import sys
import os

def main(argv):
  prefx = ''
  path = os.path.abspath(os.getcwd())
  print(path, 'nn')
  for i in range(argv.length):
    arg = argv[i]
    if i == 0:
      continue
    elif arg.index('-p=') > -1:
      prefix = arg[3:]
    elif arg != ''
      path = os.path.abspath(arg)
    


if __name__ == '__main__':
  main(sys.argv)
