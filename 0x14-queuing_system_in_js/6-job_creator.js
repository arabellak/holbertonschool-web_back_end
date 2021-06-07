const kue = require('kue');
const queue = kue.createQueue();


let jobData = {
    phoneNumber: string,
    message: string,
}

let push_notification_code = queue.create(
    {jobData}
    ).save( function(err) {
        if(!err) console.log(`Notification job created: ${push_notification_code.id}`)
    }
)

push_notification_code.on('failed', function(errorMessage){
    console.log('Notification job failed');
}).on('complete', function(result){
    console.log('Notification job completed');
})
