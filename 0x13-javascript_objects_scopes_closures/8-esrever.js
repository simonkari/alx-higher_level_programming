#!/usr/bin/node

exports.esrever = function (list) {
  const answer = [];
  for (let s = 0; s < list.length; s++) {
    answer.unshift(list[s]);
  }

  return answer;
};
