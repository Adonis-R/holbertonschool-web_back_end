const http = require('http');
const countStudents = require('./3-read_file_async');

const HOSTNAME = '127.0.0.1';
const PORT = 1245;
const DATABASE = process.argv[2];

const app = http.createServer(async (req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
    try {
      const { students, csStudents, sweStudents } = await countStudents(DATABASE);
      res.write(`Number of students: ${students.length}\n`);
      res.write(`Number of students in CS: ${csStudents.length}. List: ${csStudents.join(', ')}\n`);
      res.write(`Number of students in SWE: ${sweStudents.length}. List: ${sweStudents.join(', ')}`);
      res.end();
    } catch (error) {
      res.end(error.message);
    }
  } else {
    res.writeHead(404);
    res.end('Invalid request');
  }
});

app.listen(PORT, HOSTNAME);
module.exports = app;
