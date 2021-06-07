const kue = require('kue');

const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
  if (!(Array.isArray(jobs))) throw Error('Jobs in not an array');
  jobs.forEach((element) => {
    const queueJobs = queue.create(push_notification_code_3).save((err) => {
      if (!err) console.log(`Notification job created: ${jobs.id}`);
    });
    jobs.concat();
  });
  jobs.on('complete', (result) => { console.log(`Notification job ${jobs.id} completed`); }).on('failed', (errorMessage) => { console.log(`Notification job ${jobs.id} failed: ${errorMessage}`); }).on('progress', (progress) => { console.log(`Notification job ${jobs.id} ${progress} complete`); });
}
