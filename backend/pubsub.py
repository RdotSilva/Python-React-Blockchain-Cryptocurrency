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
pubnub = PubNub(pnconfig)

TEST_CHANNEL = "TEST_CHANNEL"

pubnub.subscribe().channels([TEST_CHANNEL]).execute()


class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f"\n-- Incoming message_object: {message_object}")


pubnub.add_listener(Listener())


class PubSub:
    """
    Handles the publish/subscribe layer of the application.
    Provides communication between the nodes of the blockchain network.
    """

    # TODO: Move methods into PubSub class


def main():
    # Add temporary sleep to avoid race condition between publish and subscribe
    time.sleep(1)
    pubnub.publish().channel(TEST_CHANNEL).message({"foo": "bar"}).sync()


if __name__ == "__main__":
    main()
