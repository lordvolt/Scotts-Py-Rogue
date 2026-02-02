from typing import Tuple

import numpy as np  # type: ignore

# Tile graphics structured type compatible with Console.tiles_rgb.
graphic_dt = np.dtype(
    [
        ("ch", np.int32),  # Unicode codepoint.
        ("fg", "3B"),  # 3 unsigned bytes, for RGB colors.
        ("bg", "3B"),
    ]
)

# Tile struct used for statically defined tile data.
tile_dt = np.dtype(
    [
        ("walkable", np.bool),  # True if this tile can be walked over.
        ("transparent", np.bool),  # True if this tile doesn't block FOV.
        ("dark", graphic_dt),  # Graphics for when this tile is not in FOV.
        ("light", graphic_dt),  # Graphics for when the tile is in FOV.
    ]
)

"""
roomtype_dt = np.dtype(
    [
        ("enabled", np.bool), # TRUE if used. FALSE will be ignored by room generator
        ("room_title", str),
        ("min_width", np.int8), # Roomtype Min/Max will override game defaults
        ("max_width", np_int8),
        ("min_height", np.int8),
        ("max_height", np_int8),
        
    ]
)
"""

def new_tile(
    *,  # Enforce the use of keywords, so that parameter order doesn't matter.
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining individual tile types """
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)


# SHROUD represents unexplored, unseen tiles
SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

"""
def new_roomtype(
    *,
    enabled: int=0,
    room_title: str="",
    min_width: int=4,
    max_width: int=8,
    min_height: int=4,
    max_height: int=8,
    
) -> np.ndarray:
    return np.array((enabled,room_title,min_width,max_width,min_height,max_height), dtype=roomtype_dt)

"""

"""
floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (20, 20, 20)),
)
wall = new_tile(
    walkable=False, transparent=False, dark=(ord("#"), (64, 64, 64), (60, 60, 60)),
)
"""

floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), (255, 255, 255), (10, 10, 10)),
    light=(ord(" "), (255, 255, 255), (20, 20, 20)),
)
wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord("▓"), (20, 20, 20), (0, 0, 100)),
    light=(ord("▓"), (100, 100, 100), (130, 110, 50)),
)
down_stairs = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord("↓"), (0, 0, 100), (50, 50, 150)),
    light=(ord("↓"), (255, 255, 255), (20, 0, 20)),
)
up_stairs = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord("↑"), (0, 0, 100), (50, 50, 150)),
    light=(ord("↑"), (255, 255, 255), (20, 0, 20)),
)


"""
roomtype_basic = new_roomtype(enabled=1,room_title="")
roomtype_crypt = new_roomtype(enabled=1,room_title=" The Crypt ")
roomtype_treasure = new_roomtype(enabled=1,room_title=" Treasure Room ")
roomtypes=(roomtype_basic,roomtype_crypt,roomtype_treasure)
"""