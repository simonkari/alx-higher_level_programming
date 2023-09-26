#!/usr/bin/node
const fs = require('fs');
const request = require('request');

if (process.argv.length === 4) {
  const url = process.argv[2];
  const filePath = process.argv[3];

  // Make a GET request to the specified URL
  request.get({ url, encoding: 'utf-8' }, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      // Write the response body to the specified file with UTF-8 encoding
      fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
        if (err) {
          console.error(`Error writing to file: ${err}`);
        } else {
          console.log(`Contents of ${url} saved to ${filePath}`);
        }
      });
    } else {
      console.error(`Error fetching URL: ${error || 'Status code ' + response.statusCode}`);
    }
  });
} else {
  console.error('Usage: node scriptName.js <URL> <FilePath>');
}
