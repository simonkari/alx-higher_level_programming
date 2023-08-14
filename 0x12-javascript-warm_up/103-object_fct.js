#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  if (x <= 0) return;  // No need to execute the loop if x is not positive

  const batchSize = 10;  // Adjust batch size as needed
  const fullBatches = Math.floor(x / batchSize);
  const remainingCalls = x % batchSize;

  for (let i = 0; i < fullBatches; i++) {
    for (let j = 0; j < batchSize; j++) {
      theFunction();
    }
  }

  for (let i = 0; i < remainingCalls; i++) {
    theFunction();
  }
};
