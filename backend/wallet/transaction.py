import uuid


class Transaction:
    """
    Document an exchange in currency from a sender to one of more recipients.
    """

    def __init__(self, sender_wallet, recipient, amount):
        self.id = str(uuid.uuid4())[0:8]
        self.output = self.create_output(sender_wallet, recipient, amount)

    def create_output(self, sender_wallet, recipient, amount):
        """
        Structure the output data for the transaction.
        """

        # TODO: Write logic for edgecase if amount exceeds the amount that current sender_wallet owns

        output = {}
        output[recipient] = amount
        output[sender_wallet.address] = sender_wallet.balance - amount

        return output
