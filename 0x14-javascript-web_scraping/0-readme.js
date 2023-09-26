#!/usr/bin/node
const fs = require('fs').promises;

async function main() {
  try {
    const data = await fs.readFile(process.argv[2], 'utf-8');
    console.log(data);
  } catch (err) {
    console.error(err);
  }
}

if (process.argv[2]) {
  main();
} else {
  console.error('Usage: node script.js <file-path>');
}
