from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration

# Imports from config file, you need to create this and add your pubnub details
from config import PUBLISH_KEY, SUBSCRIBE_KEY

# Set up pnconfig and pubnub
pnconfig = PNConfiguration()
pnconfig.subscribe_key = SUBSCRIBE_KEY
pconfig.publish_key = PUBLISH_KEY
pubnub = PubNub(pnconfig)

TEST_CHANNEL = "TEST_CHANNEL"

pubnub.subscribe().channels([TEST_CHANNEL]).execute()


def main():
    pubnub.publish().channel(TEST_CHANNEL).message({"foo": "bar"}).sync()


if __name__ == "__main__":
    main()
