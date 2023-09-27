class SafeRelayException(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Player slipped and fell"

    def __str__(self):
        return self.message


class RiskyRelayException(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Player didn't get the baton"

    def __str__(self):
        return self.message
