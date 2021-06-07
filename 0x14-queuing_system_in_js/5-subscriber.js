import redis from 'redis';

const client = redis.createClient();
const subscriber = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

subscriber.on('message', (channel, message) => {
  console.log(`Subscriber received message in channel ${channel}: ${message}`);

  if (message === KILL_SERVER) {
    subscriber.unsubscribe();
    subscriber.quit();
    subscriber.quit();
  }
});

subscriber.subscribe('holberton school channel');
