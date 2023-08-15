#!/usr/bin/node
// script that concats 2 files
const fs = require('fs');

async function concatenateFiles() {
  try {
    const file1Data = await fs.promises.readFile(process.argv[2]);
    const file2Data = await fs.promises.readFile(process.argv[3]);
    
    const concatenatedData = file1Data + file2Data;
    
    await fs.promises.writeFile(process.argv[4], concatenatedData);
    
    console.log('Files concatenated successfully.');
  } catch (err) {
    console.error('An error occurred:', err);
  }
}

concatenateFiles();
