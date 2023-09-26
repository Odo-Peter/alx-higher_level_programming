#!/usr/bin/node
const req = require('request');
req(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const user = {};
    const obj = JSON.parse(body);
    for (const key of obj) {
      if (key.completed === true) {
        if (!(key.userId in user)) {
          user[key.userId] = 1;
        } else {
          user[key.userId]++;
        }
      }
    }
    console.log(user);
  }
});
