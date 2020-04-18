import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-86294336-8164-11ea-8dff-bafe0457d467'
pnconfig.publish_key = 'pub-c-c626ee51-0936-4550-80f1-53d81a58709b'
pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'

pubnub.subscribe().channels([TEST_CHANNEL]).execute()

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Incoming message_object: {message_object}')

pubnub.add_listener(Listener())


def main():
    time.sleep(1)
    pubnub.publish().channel(TEST_CHANNEL).message({'foo': 'bar'}).sync()

if __name__ == '__main__':
    main()
