
import sys
import os

def main(argv):
  prefx = ''
  cwd = os.path.abspath(os.getcwd())
  cwds = []
  requestHelp = False
  for i in range(len(argv)):
    arg = argv[i]
    if i == 0:
      continue
    elif arg.find('-p=') > -1:
      prefix = arg[3:]
    elif arg.find('-h') > -1 or arg.find('--help') > -1:
      requestHelp = True
    elif arg.find('-') != 0:
      cwds.append(arg)


  if requestHelp == True:
    return print(
      '''usage: vfp [dir]

  batch modify package.json dependencies version[linux/macos only]

  options:
    -p=prefix update the version number with prefix, "*" will replace version number with "*"
    -h --help output usage information
      '''
    )

  if len(cwds) < 1:
    cwds = [cwd]
  else:
    cwds = map(lambda x: os.path.abspath(cwds), cwds)

  def handler(p):
    '''hanlde folder'''

    

if __name__ == '__main__':
  main(sys.argv)
