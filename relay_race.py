import random

from exceptions import SafeRelayException, RiskyRelayException


class RelayRace:

    def __init__(self, sportsmen_list, baton):
        self.sportsmen_list = sportsmen_list
        self.baton = baton

    def make_safe_relay(self):
        for s in self.sportsmen_list:
            if random.random() < 0.8:
                index = self.sportsmen_list.index(s)
                if index < len(self.sportsmen_list) - 1:
                    print(f'{s.name} takes baton and passes it to {self.sportsmen_list[index + 1].name}')
                else:
                    print(f'{s.name} takes baton')
            else:
                raise SafeRelayException

    def make_risky_relay(self):
        for s in self.sportsmen_list:
            if random.random() < 0.8:
                index = self.sportsmen_list.index(s)
                if index < len(self.sportsmen_list) - 1:
                    print(f'{s.name} catches baton and throw it to {self.sportsmen_list[index + 1].name}')
                else:
                    print(f'{s.name} catches baton')
            else:
                raise RiskyRelayException

