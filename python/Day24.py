#!/usr/bin/python3

from collections import *
import aoc_utils

delta = {
            "nw": (0, 1),
            "ne": (1, 0),
            "e": (1, -1),
            "se": (0, -1),
            "sw": (-1, 0),
            "w": (-1, 1)
        }

def parse(s):
    x, y = 0, 0
    i = 0
    while i < len(s):
        if s[i] == "n" or s[i] == "s":
            d = delta[s[i:i+2]]
            i += 2
        else:
            d = delta[s[i]]
            i += 1
        x += d[0]
        y += d[1]
    return x, y


def parsing_test():
    # should return ref. tile i.e. (0, 0)
    print(parse("nwwswee"))
    # should print (3, -3)
    print(parse("esenee"))


def adjacent_tiles(c):
    for d in delta.values():
        yield (c[0] + d[0], c[1] + d[1])


def count_black_tiles(tiles):
    black_tiles = 0
    for tile, flips in tiles.items():
        if flips % 2 == 1:
            black_tiles += 1
    return black_tiles


from copy import deepcopy

def cellular_automata(tiles):
    new_tiles = deepcopy(tiles)

    # abusing the defaultdict functionality
    # initialise all the adjacent tiles that could change value on this round
    for tile in new_tiles.keys():
        for adj_tile in adjacent_tiles(tile):
            if tiles[adj_tile] == None: pass

    for tile, flips in tiles.items():
        adjacent_black_tiles = 0
        for adj_tile in adjacent_tiles(tile):
            if tiles.get(adj_tile, 0) % 2 == 1:
                adjacent_black_tiles += 1

        if flips % 2 == 1:
            if adjacent_black_tiles == 0 or adjacent_black_tiles > 2:
                new_tiles[tile] += 1
        else:
            if adjacent_black_tiles == 2:
                new_tiles[tile] += 1

    return new_tiles


if __name__ == "__main__":

    tiles = defaultdict(int)
    for line in aoc_utils.input().readlines():
        tiles[parse(line.strip())] += 1

    print(count_black_tiles(tiles))

    for _ in range(100):
        tiles = cellular_automata(tiles)

    print(count_black_tiles(tiles))
