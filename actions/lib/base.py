
from st2common.runners.base_action import Action


class BaseClass(Action):

    def __init__(self, client) -> None:
        self.client = client