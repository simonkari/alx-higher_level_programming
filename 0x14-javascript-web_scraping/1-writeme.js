#!/usr/bin/node
// Shebang line specifying the interpreter

const fs = require('fs');
// Import the 'fs' module to work with the file system

if (process.argv.length > 3) {
  // Check if both a filename (process.argv[2]) and content (process.argv[3]) are provided

  fs.writeFile(process.argv[2], process.argv[3], err => {
    // Write the content (process.argv[3]) to the file specified by the filename (process.argv[2])

    if (err) {
      // Handle any errors that may occur during file writing
      console.log(err);
    }
  });
}
