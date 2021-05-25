const fs = require('fs');

function countStudents(path) {
  const promise = (res, rej) => {
    fs.readFile(path, (err, data) => {
      if (err) rej(Error('Cannot load the database'));
      if (data) {
        let numberStudents = data.toString().split('\n');
        numberStudents = numberStudents.slice(1, numberStudents.length - 1);
        console.log(`Number of students: ${numberStudents.length}`);
        const fieldClass = {};
        for (const row of numberStudents) {
          const student = row.split(',');
          if (!fieldClass[student[3]]) fieldClass[student[3]] = [];
          fieldClass[student[3]].push(student[0]);
        }
        for (const field in fieldClass) {
          if (field) console.log(`Number of students in ${field}: ${fieldClass[field].length}. List: ${fieldClass[field].join(', ')}`);
        }
      }
      res();
    });
  };
  return new Promise(promise);
}

module.exports = countStudents;
