#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Check if there is at least one command line argument
if (process.argv.length > 2) {
  // Make an HTTP GET request to the URL specified as the first command line argument (process.argv[2])
  request(process.argv[2], (err, res, body) => {
    // Create an object to store the aggregate count of completed tasks by user ID
    const aggregate = {};

    // Check for errors during the HTTP request
    if (err) {
      console.error(err);
      return;
    }

    // Parse the JSON response from the API and iterate through its elements
    JSON.parse(body).forEach(element => {
      // Check if the task is completed
      if (element.completed) {
        // Initialize the count for the user if it doesn't exist
        if (!aggregate[element.userId]) {
          aggregate[element.userId] = 0;
        }
        // Increment the count of completed tasks for the user
        aggregate[element.userId]++;
      }
    });

    // Print the aggregate count of completed tasks by user ID
    console.log(aggregate);
  });
}
