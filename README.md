# version-fixer-py
batch modify package.json dependencies version[linux only]

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
npm i -g version-fixer-py
cd your project_folder
vfp
# or
vfp path/to/your/project
# with version
version-fixer -p=^ path/to/your/project
# make all version to '*'
version-fixer -p=* path/to/your/project
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