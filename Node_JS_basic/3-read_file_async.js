const fs = require('fs');

const countStudents = async (path) => {
  let data = '';

  try {
    data = await fs.promises.readFile(path, 'utf-8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  const dataSet = data.split('\n').slice(1);
  const normalized = dataSet.map((line) => line.split(','))
    .filter((student) => student.length === 4);

  const students = normalized.map((student) => ({
    firstname: student[0],
    lastname: student[1],
    age: student[2],
    field: student[3],
  }));

  const csStudents = students.filter((s) => s.field === 'CS')
    .map((s) => s.firstname);
  const sweStudents = students.filter((s) => s.field === 'SWE')
    .map((s) => s.firstname);

  console.log(`Number of students: ${students.length}`);
  console.log(`Number of students in CS: ${csStudents.length}. List: ${csStudents.join(', ')}`);
  console.log(`Number of students in SWE: ${sweStudents.length}. List: ${sweStudents.join(', ')}`);

  return { students, csStudents, sweStudents };
};

module.exports = countStudents;
