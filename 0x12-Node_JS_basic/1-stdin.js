process.stdin.resume();
console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('data', (welcomeName) => {
  process.stdout.write(`Your name is: ${welcomeName}`);
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing \n');
});
