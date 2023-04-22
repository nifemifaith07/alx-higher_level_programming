#!/usr/bin/node
export.callMeMoby = function (x, theFunction) {
  while (x > 0) {
    theFunction.call();
    ×--;
  }
};
