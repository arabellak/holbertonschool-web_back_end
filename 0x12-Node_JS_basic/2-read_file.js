const fs = require('fs');

function countStudents(path) {
  try {
    let data = fs.readFileSync(path, 'utf8').toString().split('\n');
    data = data.slice(1, data.length - 1);
    console.log(`Number of students: ${data.length}`);
    const fieldClass = {};
    for (const row of data) {
      const firstName = row.split(',');
      if (!fieldClass[firstName[3]]) fieldClass[firstName[3]] = [];
      fieldClass[firstName[3]].push(firstName[0]);
    }
    for (const field in fieldClass) {
      if (field) console.log(`Number of students in ${field}: ${fieldClass[field].length}. List: ${fieldClass[field].join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
