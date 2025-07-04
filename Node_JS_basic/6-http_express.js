const express = require('express');

const app = express();

app.get('/', (req, res) => {
  res.end('Hello Holberton School!');
});

app.listen(process.env.PORT || 1245);

module.exports = app;
