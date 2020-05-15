import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

# Imports from config file, you need to create this and add your pubnub details
from config import PUBLISH_KEY, SUBSCRIBE_KEY

# Set up pnconfig and pubnub
pnconfig = PNConfiguration()
pnconfig.subscribe_key = SUBSCRIBE_KEY
pnconfig.publish_key = PUBLISH_KEY

TEST_CHANNEL = "TEST_CHANNEL"
BLOCK_CHANNEL = "BLOCK_CHANNEL"

CHANNELS = {"TEST": "TEST", "BLOCK": "BLOCK"}


class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(
            f"\n-- Channel: {message_object.channel} | Message: {message_object.message}"
        )


class PubSub:
    """
    Handles the publish/subscribe layer of the application.
    Provides communication between the nodes of the blockchain network.
    """

    def __init__(self):
        self.pubnub = pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels([CHANNELS.values()]).execute()
        pubnub.add_listener(Listener())

    def publish(self, channel, message):
        """
        Publish the message object to the channel.

        """
        self.pubnub.publish().channel(channel).message(message).sync()


def main():
    pubsub = PubSub()

    # Add temporary sleep to avoid race condition between publish and subscribe
    time.sleep(1)

    pubsub.publish(TEST_CHANNEL, {"foo": "bar"})


if __name__ == "__main__":
    main()
