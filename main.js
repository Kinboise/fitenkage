// const { prepare, latToFit } = require('./fitenkage.js')
import { prepare, latToFit } from './fitenkage.js'

export function conv() {
    const kage = prepare()
    let lat = document.getElementById('lat').value
    let fit = latToFit(kage,lat)
    document.getElementById('fit').innerHTML = fit
}