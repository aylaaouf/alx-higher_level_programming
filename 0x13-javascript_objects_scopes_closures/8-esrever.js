#!/usr/bin/node
exports.esrever = function (list) {
  const revlist = [];
  for (let i = 2; i < list.length; i++) {
    revlist.push(list[i]);
  }
  return revlist;
};

