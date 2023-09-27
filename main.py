from baton import Baton
from relay_race import RelayRace
from sportsman import Sportsman


sportsman1 = Sportsman('Zeus')
sportsman2 = Sportsman('George')
sportsman3 = Sportsman('John')
sportsman4 = Sportsman('Pedro')
sportsman5 = Sportsman('Ethan')

sportsmen_list = [sportsman1, sportsman2, sportsman3, sportsman4, sportsman5]

baton1 = Baton()

relay_race1 = RelayRace(sportsmen_list, baton1)
# relay_race1.make_safe_relay()
relay_race1.make_risky_relay()
