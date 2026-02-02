from __future__ import annotations

import lzma
import pickle
from typing import TYPE_CHECKING

from tcod.console import Console
from tcod.map import compute_fov

import exceptions
from message_log import MessageLog
import render_functions

import globalvars

if TYPE_CHECKING:
    from entity import Actor
    from game_map import GameMap, GameWorld

class Engine:
    game_map: GameMap
    game_world: GameWorld

    def __init__(self, player: Actor):
        self.message_log = MessageLog()
        self.mouse_location = (0, 0)
        self.player = player

    def handle_enemy_turns(self) -> None:
        for entity in set(self.game_map.actors) - {self.player}:
            if entity.ai:
                try:
                    entity.ai.perform()
                except exceptions.Impossible:
                    pass  # Ignore impossible action exceptions from AI.

    def update_fov(self) -> None:
        """Recompute the visible area based on the players point of view."""
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=8,
        )
        # If a tile is "visible" it should be added to "explored".
        self.game_map.explored |= self.game_map.visible

    def render(self, console: Console) -> None:
        self.game_map.render(console)

        
        takenwidth = globalvars.GAME_UI_INFOWIDTH + globalvars.GAME_UI_HELPWIDTH
        logwidth = globalvars.GAME_SCREENWIDTH - takenwidth
        self.message_log.render(console=console, x=21, y=globalvars.GAME_MAPHEIGHT+3, width=logwidth, height=7)

        render_functions.render_separator(
            console=console,
            location=(0,globalvars.GAME_MAPHEIGHT+1),
            width=globalvars.GAME_SCREENWIDTH,
        )

        render_functions.render_healthbar(
            console=console,
            current_value=self.player.fighter.hp,
            maximum_value=self.player.fighter.max_hp,
            location=(0, globalvars.GAME_MAPHEIGHT+2),
            total_width=globalvars.GAME_UI_INFOWIDTH,
        )

        ### TODO: FOR WHEN MANA/MAGIC IS IMPLEMENTED
        render_functions.render_manabar(
            console=console,
            current_value=10,
            maximum_value=20,
            location=(0, globalvars.GAME_MAPHEIGHT+3),
            total_width=globalvars.GAME_UI_INFOWIDTH,
        )

        render_functions.render_player_level(
            console=console,
            player_level=self.player.level.current_level,
            player_xp=self.player.level.current_xp,
            player_xpnext=self.player.level.experience_to_next_level,
            location=(0, globalvars.GAME_MAPHEIGHT+4),
        )

        render_functions.render_dungeon_level(
            console=console,
            dungeon_level=self.game_world.current_floor,
            location=(0, globalvars.GAME_MAPHEIGHT+5),
        )

        render_functions.render_names_at_mouse_location(
            console=console, x=globalvars.GAME_UI_INFOWIDTH+1, y=globalvars.GAME_MAPHEIGHT+2, engine=self
        )

        render_functions.render_help_box(
            console=console,
            location=(globalvars.GAME_SCREENWIDTH - globalvars.GAME_UI_HELPWIDTH,globalvars.GAME_MAPHEIGHT+2),
            width=globalvars.GAME_UI_HELPWIDTH,
            height=8
        )

    def save_as(self, filename: str) -> None:
        """Save this Engine instance as a compressed file."""
        save_data = lzma.compress(pickle.dumps(self))
        with open(filename, "wb") as f:
            f.write(save_data)
