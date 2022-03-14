import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pn_config = PNConfiguration()
pn_config.subscribe_key = 'sub-c-2543353c-6fc8-11ec-97ad-065127b61789'
pn_config.publish_key = 'pub-c-d5f7f34a-bada-4552-bfce-09174bc4d062'
pubnub = PubNub(pn_config)

CHANNELS = {
    'TEST': 'TEST',
    'BLOCK': 'BLOCK'
}


class Listener(SubscribeCallback):
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def message(self, pubnub, message):
        print(f'\n - Channel: {message} | Message: {message.message}')

        if message.channel == CHANNELS['BLOCK']:
            block = message.message
            potential_chain = self.blockchain.chain[:]
            potential_chain.append(block)

            try:
                self.blockchain.replace_chain(potential_chain)
                print('\n -- Successfully replaced the local chain')
            except Exception as e:
                print(f'\n -- Did not replace chain: {e}')


pubnub.add_listener(Listener())


class PubSub():
    """
    handles the publish/subscribe layer of the application
    Provide communication between the nodes of the blockchain network
    """

    def __int__(self, blockchain):
        self.pubnub = PubNub(pn_config)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain))

    def publish(self, channel, message):
        """
        Publish the message object to the channel
        """
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self, block):
        """
        Broadcast a block object to all nodes
        :param block:
        :return:
        """


def main():
    pub_sub = PubSub()

    time.sleep(1)

    pub_sub.publish(CHANNELS['TEST'], {'foo': 'bar'})


if __name__ == '__main__':
    main()
