#!/usr/bin/node
exports.esrever = function (list) {
  let revlist = [];
  for (let i = 2; i < list.length; i++) {
    revlist = list[i];
  }
  return revlist;
};
