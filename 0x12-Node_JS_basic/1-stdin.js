process.stdin.resume();
console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('readable', () => {
  const welcomeName = process.stdin.read();
  if (welcomeName !== null) {
    process.stdout.write(`Your name is: ${welcomeName}`);
  }
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing \n');
});
