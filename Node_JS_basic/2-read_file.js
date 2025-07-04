const fs = require('fs');

function countStudents(fileName) {
  const studentsByField = {};
  const fieldsCount = {};
  let totalStudents = 0;

  try {
    // Read the CSV file
    const content = fs.readFileSync(fileName, 'utf-8');
    const lines = content.trim().split('\n');

    // Process the content of the file
    for (let i = 1; i < lines.length; i += 1) { // Start at 1 to skip the header
      if (lines[i]) {
        totalStudents += 1;
        const [firstName, , , field] = lines[i].split(',');

        // Add the student to the list of students for the field
        if (!studentsByField[field]) {
          studentsByField[field] = [];
        }
        studentsByField[field].push(firstName);

        // Count the number of students in the field
        if (fieldsCount[field]) {
          fieldsCount[field] += 1;
        } else {
          fieldsCount[field] = 1;
        }
      }
    }

    // Print the number of students
    console.log(`Number of students: ${totalStudents}`);

    // Print the number of students in each field
    for (const [field, count] of Object.entries(fieldsCount)) {
      console.log(`Number of students in ${field}: ${count}. List: ${studentsByField[field].join(', ')}`);
    }
  } catch (error) {
    // Error reading the file
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
