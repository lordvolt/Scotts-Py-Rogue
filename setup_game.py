"""Handle the loading and initialization of game sessions."""
from __future__ import annotations

import os
import copy
import lzma
import pickle
import traceback
from typing import Optional

import tcod

import color
from engine import Engine
import entity_factories
from game_map import GameWorld
import input_handlers

import globalvars

# Load the background image and remove the alpha channel.
background_image = tcod.image.load(globalvars.GAME_MAINMENU_BG)[:, :, :3]


def new_game() -> Engine:
    """Return a brand new game session as an Engine instance."""
    map_width = globalvars.GAME_MAPWIDTH
    map_height = globalvars.GAME_MAPHEIGHT

    room_max_size = globalvars.GAME_ROOM_MAXSIZE
    room_min_size = globalvars.GAME_ROOM_MINSIZE
    max_rooms = globalvars.GAME_ROOM_MAXROOMS

    player = copy.deepcopy(entity_factories.player)

    engine = Engine(player=player)

    engine.game_world = GameWorld(
        engine=engine,
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
    )

    engine.game_world.generate_floor()
    engine.update_fov()

    engine.message_log.add_message(
        globalvars.GAME_LOG_WELCOMETEXT, color.welcome_text
    )

    initialitems = {
        "dagger": entity_factories.dagger, 
        "leather_armor": entity_factories.leather_armor,
        "health_potion": entity_factories.health_potion,
    }
    iitemscopy = {}

    

    for ikey, ivalue in initialitems.items():
        iitemscopy[ikey] = copy.deepcopy(ivalue)
        iitemscopy[ikey].parent = player.inventory
        player.inventory.items.append(iitemscopy[ikey])
        if iitemscopy[ikey].equippable:
            player.equipment.toggle_equip(iitemscopy[ikey], add_message=False)

    """
    dagger = copy.deepcopy(entity_factories.dagger)
    leather_armor = copy.deepcopy(entity_factories.leather_armor)

    dagger.parent = player.inventory
    leather_armor.parent = player.inventory

    player.inventory.items.append(dagger)
    player.equipment.toggle_equip(dagger, add_message=False)

    player.inventory.items.append(leather_armor)
    player.equipment.toggle_equip(leather_armor, add_message=False)
    """

    return engine

def load_game(filename: str) -> Engine:
    """Load an Engine instance from a file."""
    with open(filename, "rb") as f:
        engine = pickle.loads(lzma.decompress(f.read()))
    assert isinstance(engine, Engine)
    return engine

class MainMenu(input_handlers.BaseEventHandler):
    """Handle the main menu rendering and input."""

    def on_render(self, console: tcod.Console) -> None:
        """Render the main menu on a background image."""
        console.draw_semigraphics(background_image, 0, 0)

        console.print(
            console.width // 2,
            console.height // 2 - 4,
            globalvars.GAME_TITLE, 
            fg=color.menu_title,
            alignment=tcod.CENTER,
        )
        console.print(
            console.width // 2,
            console.height - 2,
            globalvars.GAME_TITLEBAR + " " + globalvars.GAME_COPYRIGHT,
            fg=color.menu_title,
            alignment=tcod.CENTER,
        )

        menu_width = 24

        if (os.path.exists("savegame.sav")):
            for i, text in enumerate(
                    ["[N] Play a new game", "[C] Continue last game", "[Q] Quit"]
                ):

                console.print(
                    console.width // 2,
                    console.height // 2 - 2 + i,
                    text.ljust(menu_width),
                    fg=color.menu_text,
                    bg=color.black,
                    alignment=tcod.CENTER,
                    bg_blend=tcod.BKGND_ALPHA(64),
                )
        else:
            for i, text in enumerate(
                    ["[N] Play a new game", "[Q] Quit"]
                ):

                console.print(
                    console.width // 2,
                    console.height // 2 - 2 + i,
                    text.ljust(menu_width),
                    fg=color.menu_text,
                    bg=color.black,
                    alignment=tcod.CENTER,
                    bg_blend=tcod.BKGND_ALPHA(64),
                )

    def ev_keydown(
        self, event: tcod.event.KeyDown
    ) -> Optional[input_handlers.BaseEventHandler]:
        if event.sym in (tcod.event.KeySym.q, tcod.event.KeySym.ESCAPE):
            raise SystemExit()
        elif event.sym == tcod.event.KeySym.c:
            try:
                return input_handlers.MainGameEventHandler(load_game("savegame.sav"))
            except FileNotFoundError:
                return input_handlers.PopupMessage(self, "No saved game to load.")
            except Exception as exc:
                traceback.print_exc()  # Print to stderr.
                return input_handlers.PopupMessage(self, f"Failed to load save:\n{exc}")
        elif event.sym == tcod.event.KeySym.n:
            return input_handlers.MainGameEventHandler(new_game())

        return None