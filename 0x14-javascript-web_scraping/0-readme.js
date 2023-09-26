#!/usr/bin/node
// Shebang line specifying the interpreter

const fs = require('fs');
// Import the 'fs' module to work with the file system

if (process.argv.length > 2) {
  // Check if command-line arguments are provided (excluding 'node' and the script filename)
  
  fs.readFile(process.argv[2], (err, data) => {
    // Read the file specified by the first command-line argument (process.argv[2])
    
    if (err) {
      // Handle any errors that may occur during file reading
      console.log(err);
    } else {
      // If there are no errors, display the contents of the file as a UTF-8 string
      console.log(data.toString('utf-8'));
    }
  });
}
