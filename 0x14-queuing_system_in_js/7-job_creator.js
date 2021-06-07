const kue = require('kue');
const queue = kue.createQueue();

const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
  ];

for (let i of jobs) {
    const push_notification_code_2 = queue.create(jobs)
    .save( function(err) { if (!err) console.log(push_notification_code_2.id)})
    push_notification_code_2.on('complete', function(result) { console.log(`Notification job created: ${push_notification_code_2.id}`)}
    ).on('failed', function(errorMessage) { console.log(`Notification job ${push_notification_code_2.id} failed: ${errorMessage}`)}
    ).on('progress', function(progress) { console.log(`Notification job ${push_notification_code_2.id} ${progress} complete`) })
}
