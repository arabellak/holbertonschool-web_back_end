console.log('Welcome to Holberton School, what is your name?');
process.stdin.on('data', function(dat) {
    console.log(`Your name is: ${dat}`);
})


