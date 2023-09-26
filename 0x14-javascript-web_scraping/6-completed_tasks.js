#!/usr/bin/node
const request = require('request');

// API URL
const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

// Make a GET request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('API Request Failed with Status Code:', response.statusCode);
    return;
  }

  // Parse the JSON response
  const todos = JSON.parse(body);

  // Create an object to store the count of completed tasks by user ID
  const completedTasksByUserId = {};

  // Loop through the todos to count completed tasks
  todos.forEach((todo) => {
    if (todo.completed) {
      const userId = todo.userId;
      if (completedTasksByUserId[userId]) {
        completedTasksByUserId[userId]++;
      } else {
        completedTasksByUserId[userId] = 1;
      }
    }
  });

  // Print users with completed tasks
  for (const userId in completedTasksByUserId) {
    console.log(`User ID ${userId}: ${completedTasksByUserId[userId]} completed tasks`);
  }
});
