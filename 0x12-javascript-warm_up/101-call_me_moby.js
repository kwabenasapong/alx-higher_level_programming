#!/usr/bin/node
const callMeMoby = function (x, theFunction) {};

callMeMoby.prototype.log = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
exports.callMeMoby = callMeMoby(x, theFunction);
