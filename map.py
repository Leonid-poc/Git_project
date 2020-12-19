from setting import *
MAP = [
    'QQQQQQQQQQ',
    'Q........Q',
    'Q........Q',
    'Q..QQQQ..Q',
    'Q..QQqQ..Q',
    'Q..QQQQ..Q',
    'Q........Q',
    'Q........Q',
    'Q........Q',
    'QQQQQQQQQQ'
]
world_map = set()
TILE_X, TILE_Y = WIDTH_SCREEN // len(MAP[0]), HIGHT_SCREEN // len(MAP)
for i, row in enumerate(MAP):
    for j, char in enumerate(row):
        if char.upper() == 'Q':
            world_map.add((j * TILE_X, i * TILE_Y))
world_map = world_map.copy()
