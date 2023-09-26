#!/usr/bin/node
const fs = require('fs');

function writeStringToFile(filePath, content) {
    fs.writeFile(filePath, content, 'utf-8', (err) => {
        if (err) {
            console.error(`An error occurred while writing to ${filePath}: ${err}`);
        } else {
            console.log(`Successfully wrote the string to ${filePath}`);
        }
    });
}

if (process.argv.length !== 4) {
    console.log('Usage: node script.js <file_path> <string_to_write>');
} else {
    const filePath = process.argv[2];
    const content = process.argv[3];
    writeStringToFile(filePath, content);
}
