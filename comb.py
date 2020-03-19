from pprint import pprint
from copy import deepcopy
from functools import reduce

colors = ["W", "U", "B", "R", "G"]


def get_shards():
    shards = []
    for i, c in enumerate(colors):
        j = i-1
        k = (i+1) % len(colors)
        shard = colors[j] + c + colors[k]
        shards.append(shard)
    return shards


def get_guilds():
    combs = []
    for i, c1 in enumerate(colors):
        for j, c2 in enumerate(colors):
            if i < j:
                combs.append(c1 + c2)
    return combs

def get_wedges():
    wedges = []
    for i, c in enumerate(colors):
        j = (i+2)%len(colors)
        k = (j+2)%len(colors)
        wedge = c + colors[j] + colors[k]
        wedges.append(wedge)
    return wedges

def get_nephilim():
    nephilims = []
    for i in range(len(colors)):
        four = deepcopy(colors)
        four.pop(i)
        nephilim = reduce((lambda x, y: x + y), four)
        nephilims.append(nephilim)
    return nephilims

def get_shards_and_wedges():
    return get_shards() + get_wedges()

if __name__ == '__main__':
    guilds = get_guilds()
    pprint(guilds)
    print "# of Guilds: %i" % len(guilds)

    shards = get_shards()
    pprint(shards)
    print "# of Shards: %i" % len(shards)

    wedges = get_wedges()
    pprint(wedges)
    print "# of Wedges: %i" % len(wedges)

    nephilim = get_nephilim()
    pprint(nephilim)
    print "# of nephilims: %i" % len(nephilim)

    snw = get_shards_and_wedges()
    pprint(snw)
    print "# of three color combos: %i" % len(snw)