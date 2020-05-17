import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

from backend.blockchain.block import Block

# Imports from config file, you need to create this and add your pubnub details
from config import PUBLISH_KEY, SUBSCRIBE_KEY

# Set up pnconfig and pubnub
pnconfig = PNConfiguration()
pnconfig.subscribe_key = SUBSCRIBE_KEY
pnconfig.publish_key = PUBLISH_KEY

CHANNELS = {"TEST": "TEST", "BLOCK": "BLOCK"}


class Listener(SubscribeCallback):
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def message(self, pubnub, message_object):
        print(
            f"\n-- Channel: {message_object.channel} | Message: {message_object.message}"
        )

        if message_object.channel == CHANNELS["BLOCK"]:
            block = Block.from_json(message_object.message)
            potential_chain = self.blockchain.chain[:]
            potential_chain.append(block)

            try:
                self.blockchain.replace_chain(potential_chain)
                print("\n -- Successfully replaced the local chain")
            except Exception as e:
                print(f"\n -- Did not replace chain: {e}")


class PubSub:
    """
    Handles the publish/subscribe layer of the application.
    Provides communication between the nodes of the blockchain network.
    """

    def __init__(self, blockchain):
        self.pubnub = pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        pubnub.add_listener(Listener(blockchain))

    def publish(self, channel, message):
        """
        Publish the message object to the channel.

        """
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self, block):
        """
        Broadcast a block object to all nodes.
        """
        self.publish(CHANNELS["BLOCK"], block.to_json())


def main():
    pubsub = PubSub()

    # Add temporary sleep to avoid race condition between publish and subscribe
    time.sleep(1)

    pubsub.publish(CHANNELS["TEST"], {"foo": "bar"})


if __name__ == "__main__":
    main()
