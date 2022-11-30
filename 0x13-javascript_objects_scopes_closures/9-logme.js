#!/usr/bin/node

let count = 0;
function counter () {
  return count;
}
exports.logMe = function (item) {
  console.log(counter() + ': ' + item);
  count++;
};
