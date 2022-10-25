
from lib.base import BaseClass


class MyEchoAction(BaseClass):

    def run(self, message):
        """
		"""
        print("My message: {0}".format(message))
        print("My object from BaseClass: {0}".format(self.client))
        return (True, message)