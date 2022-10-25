
from actions.lib.base import BaseClass


class MyEchoAction(BaseClass):

    def __init__(self, config=None) -> None:
        super().__init__(config)

    def run(self, message):
        """
		"""
        print("My message: {0}".format(message))
        print("My object from BaseClass: {0}".format(self.client))
        return (True, message)