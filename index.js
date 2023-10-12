const { prepare, latToFit } = require('./fitenkage.js')

const kage = prepare()
// const svg = latToFit(kage, 'snv', 'target')
const svg = latToFit(kage, process.argv[2], 'target')
var fs = require('fs')

fs.writeFile(process.argv[3], svg, function(err) {
    if (err != null) {
        console.log(err)
    }
})