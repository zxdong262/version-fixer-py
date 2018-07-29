# version-fixer-py
[![Build Status](https://travis-ci.org/zxdong262/version-fixer-py.svg?branch=test)](https://travis-ci.org/zxdong262/version-fixer-py)
batch modify package.json dependencies version[linux/macos only]

## install
```bash
# make sure you have python installed
npm i -g version-fixer-py

# or
git clone git@github.com:zxdong262/version-fixer-py.git
# then add path/to/version-fixer-py/bin to your system path
```

## use
```bash
# makesure `python` command works
npm i -g version-fixer-py
cd your project_folder
vfp
# or hanle multi project
vfp path/to/your/project1 path/to/your/project2
# with version
version-fixer -p=^ path/to/your/project1 path/to/your/project2
# make all version to '*'
version-fixer -p=* path/to/your/project1 path/to/your/project2
```

## test
```bash
git clone https://github.com/zxdong262/version-fixer.git
cd version-fixer
npm i
mocha
```

## License
MIT