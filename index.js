const { prepare, latToFit } = require('./fitenkage.js')

const kage = prepare()
// const svg = latToFit(kage, 'dC', 'target')
const svg = latToFit(kage, process.argv[3], 'target')

// const { SVG } = require('@svgdotjs/svg.js')

// SVG(svg)

var fs = require('fs')

fs.writeFile(process.argv[2], svg, function(err) {
    if (err != null) {
        console.log(err)
    }
})