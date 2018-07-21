
import sys
import os
import json
from collections import OrderedDict

def main(argv):
  prefix = ''
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
    print(
      '''usage: vfp [dir]

  batch modify package.json dependencies version[linux/macos only]

  options:
    -p=prefix update the version number with prefix, "*" will replace version number with "*"
    -h --help output usage information
      '''
    )
    return

  if len(cwds) < 1:
    cwds = [cwd]
  else:
    cwds = list(map(lambda x: os.path.abspath(x), cwds))

  def writeFile(p, txt):
    '''write file'''
    try:
      file = open(p, 'w')
      file.write(txt)
      file.close()

    except:
      print('error when read:', p)

  def readJson(p):
    '''read json'''
    try:
      file = open(p, 'r')
      txt = file.read()
      pkg = json.loads(txt, object_pairs_hook=OrderedDict)
      file.close()
      return OrderedDict(pkg)

    except:
      print('error when read:', p)
      return False

  def pkgHandle(dependencies, targetPkg, varr, rpath, dep):
    keys = dependencies.keys()
    for key in keys:
      pkgInfo = {}
      p = rpath + '/node_modules/' + key + '/package.json'
      pkgInfo = readJson(p)
      if pkgInfo != False:
        varr.append({
          'name': pkgInfo[u'name'],
          'version': pkgInfo[u'version'],
          'type': dep
        })
    return varr

  def handler(p):
    '''hanlde package.json for each path'''
    pkgPath = p + '/package.json'
    print('target:', pkgPath)
    targetPkg = readJson(pkgPath)
    if targetPkg == False:
      return
    varr = []
    deps = ['dependencies', 'devDependencies']
    for dep in deps:
      if targetPkg.get(dep) == None:
        continue
      pkgHandle(targetPkg[dep], targetPkg, varr, p, dep)

    for obj in varr:
      type = obj['type']
      version = obj['version']
      name = obj['name']
      v = '*' if prefix == '*' else prefix + version
      print(str(name), targetPkg[type][name], '-->', v)
      targetPkg[type][name] = v

    pkgNew = json.dumps(targetPkg, indent=2) + '\n'
    writeFile(
      pkgPath,
      pkgNew
    )

    print('done:', pkgPath)

  for p in cwds:
    handler(p)

if __name__ == '__main__':
  main(sys.argv)
