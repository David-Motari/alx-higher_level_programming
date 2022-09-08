#!/usr/bin/node

const fs = require('fs');

const data1 = fs.readFileSync(process.argv[2], 'utf8', function (err, result) { if (err) console.log('error', err); });
const data2 = fs.readFileSync(process.argv[3], 'utf8', function (err, result) { if (err) console.log('error', err); });

const data3 = data1.concat(data2);

fs.writeFile(process.argv[4], data3, 'utf8', function (err, result) { if (err) console.log('error', err); });
