import uuid


class Transaction:
    """
    Document an exchange in currency from a sender to one of more recipients.
    """

    def __init__(self, sender_wallet, recipient, amount):
        self.id = str(uuid.uuid4())[0:8]
        self.output = self.create_output(sender_wallet, recipient, amount)
