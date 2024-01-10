#!/usr/bin/node
// executes x times a function
exports.callMeMoby = function (x, theFunction) {
  while (x > 0) {
    theFunction.call();
    x--;
  }
};
