#!/usr/bin/node
const req = require('request');
req(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let counter = 0;
    const obj = JSON.parse(body).results;
    for (const key of obj) {
      for (const c of key.characters) {
        if (c.search('/18/') > 0) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
