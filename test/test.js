
const assert = require('assert')
const fs = require('fs')
const path = require('path')
const rpath = path.resolve(__dirname, '../package.json')
const pkgStr = fs.readFileSync(rpath)
const oldPkg = JSON.parse(pkgStr.toString())
const {exec} = require('shelljs')

describe('version fixer', function() {
  it('default', function(done) {


    exec('./bin/vfp ./')

    setTimeout(function() {
      var newPkg = JSON.parse(fs.readFileSync(rpath).toString())
      fs.writeFileSync(rpath, pkgStr)
      assert(newPkg.devDependencies.mocha !== oldPkg.devDependencies.mocha)
      done()
    }, 300)

  })

  it('with prefix ^', function(done) {

    exec('./bin/vfp -p=^ ./')

    setTimeout(function() {
      var newPkg = JSON.parse(fs.readFileSync(rpath).toString())
      fs.writeFileSync(rpath, pkgStr)
      assert(newPkg.devDependencies.mocha === oldPkg.devDependencies.mocha && newPkg.devDependencies.mocha.indexOf('^') === 0)
      done()
    }, 300)

  })

  it('with prefix *', function(done) {

    exec('./bin/vfp -p=* ./')

    setTimeout(function() {
      var newPkg = JSON.parse(fs.readFileSync(rpath).toString())
      fs.writeFileSync(rpath, pkgStr)
      assert(newPkg.devDependencies.mocha !== oldPkg.devDependencies.mocha && newPkg.devDependencies.mocha === '*')
      done()
    }, 500)

  })

})
