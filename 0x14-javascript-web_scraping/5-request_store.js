#!/usr/bin/node
const req = require('request');
const fs = require('fs');
const argv = process.argv;
const url = argv[2];
const file = argv[3];
req(url, function (error, res, body) {
  if (error) {
    console.error('error:', error);
  } else {
    fs.writeFile(file, body, 'utf8', function (err) {
      if (err) return console.log(err);
    });
  }
});
