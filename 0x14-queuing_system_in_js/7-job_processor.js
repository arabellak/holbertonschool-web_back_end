const kue = require('kue');

const queue = kue.createQueue();

const blacklistedPhoneNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  if (phoneNumber in blacklistedPhoneNumbers) throw Error(`Phone number ${phoneNumber} is blacklisted`);
  job.progress(50, 100);
  console.log(`Sending notifications to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code_2', (job, done) => {
  sendNotification(jon.data.phoneNumber, job.data.message, job, done);
});
