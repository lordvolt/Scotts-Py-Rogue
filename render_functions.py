from __future__ import annotations

from typing import Tuple, TYPE_CHECKING

import color

if TYPE_CHECKING:
    from tcod import Console
    from engine import Engine
    from game_map import GameMap


def get_names_at_location(x: int, y: int, game_map: GameMap) -> str:

    ### needed to make this work....
    x = int(x)
    y = int(y)
    # ADDED FOR DEBUGGING
    # print(f"Mouse X:{x} Y:{y}")
    
    if not game_map.in_bounds(x, y) or not game_map.visible[x, y]:
        return ""
    

    
    names = ", ".join(
        entity.longname for entity in game_map.entities if entity.x == x and entity.y == y
    )

    return names.capitalize()



def render_healthbar(
    console: Console, current_value: int, maximum_value: int, total_width: int, location: Tuple[int, int]
) -> None:
    x, y = location
    bar_width = int(float(current_value) / maximum_value * total_width)

    console.draw_rect(x=x, y=y, width=total_width, height=1, ch=1, bg=color.health_bar_empty)

    if bar_width > 0:
        console.draw_rect(
            x=x, y=y, width=bar_width, height=1, ch=1, bg=color.health_bar_filled
        )

    console.print(
        x=x, y=y, string=f"HP: {current_value}/{maximum_value}", fg=color.health_bar_text
    )

def render_manabar(
    console: Console, current_value: int, maximum_value: int, total_width: int, location: Tuple[int, int]
) -> None:
    x, y = location
    bar_width = int(float(current_value) / maximum_value * total_width)

    console.draw_rect(x=x, y=y, width=total_width, height=1, ch=1, bg=color.mana_bar_empty)

    if bar_width > 0:
        console.draw_rect(
            x=x, y=y, width=bar_width, height=1, ch=1, bg=color.mana_bar_filled
        )

    console.print(
        x=x, y=y, string=f"Mana: {current_value}/{maximum_value}", fg=color.mana_bar_text
    )


def render_dungeon_level(
    console: Console, dungeon_level: int, location: Tuple[int, int]
) -> None:
    """
    Render the level the player is currently on, at the given location.
    """
    x, y = location

    console.print(x=x, y=y, string=f"Dungeon Floor: {dungeon_level}")

def render_player_level(
    console: Console, player_level: int, player_xp: int, player_xpnext: int, location: Tuple[int, int]
) -> None:
    """
    Render the XP Level of the player, at the given location.
    """
    x, y = location

    console.print(x=x, y=y, string=f"XP Lvl: {player_level} ({player_xp}/{player_xpnext})")

def render_help_box(
    console: Console, location: Tuple[int, int], width: width, height: height,
) -> None:
    """
    Render the help box, at the given location.
    """
    x, y = location
    console.draw_frame(x=x, y=y, width=width, height=height, bg=color.black, fg=color.lightgrey, decoration="╔═╗║ ║╚═╝")
    console.print(x=x+2, y=y, width=width-4, height=1, string=" Controls ")
    console.print(x=x+2, y=y+1, string="Arrow Keys, NumPad")
    console.print(x=x+2, y=y+2, string="SPC to Interact/Grab/↕")
    console.print(x=x+2, y=y+3, string="C Char - I Inv - D Drop")
    console.print(x=x+2, y=y+4, string="V Log - Q Save & Quit")
    
    
def render_separator(
    console: Console, location: Tuple[int, int], width: width,
) -> None:
    """
    Render a separator bar
    """
    x, y = location
    console.draw_rect(x=x, y=y, width=width, height=1, ch=ord('═'), fg=color.gold, bg=color.black)

def render_names_at_mouse_location(
    console: Console, x: int, y: int, engine: Engine
) -> None:
    mouse_x, mouse_y = engine.mouse_location

    names_at_mouse_location = get_names_at_location(
        x=mouse_x, y=mouse_y, game_map=engine.game_map
    )

    console.print(x=x, y=y, string=names_at_mouse_location)