from random import shuffle
from collections import deque
from copy import deepcopy

class SecretSanta(object):
    """A Secret Santa game."""

    def __init__(self, names):
        """Create a new Secret Santa game using a list of names.

        ```
        names = [('Mrs. Claus', 'claus2@gmail.com'), ...]

        SecretSanta(names)
        ```
        """

        self.names = names

    def matchup(self):
        """Create the Secret Santa matches."""

        _names = deepcopy(self.names)
        _from = _names

        shuffle(_names)
        _to = deque(_names)

        exchanges = []

        for name in _from:
            if name != _to[0]:
                exchange = {'from': name,
                            'to': _to.popleft()}
                exchanges.append(exchange)
            else:
                exchange = {'from': name,
                            'to': _to.pop()}
                exchanges.append(exchange)
        return exchanges

