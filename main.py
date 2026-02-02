#!/usr/bin/env python3
import warnings
import traceback
import tcod

import color
import exceptions
import input_handlers
import setup_game

import globalvars
import pygame

##########################
#
# Used tutorial at https://www.rogueliketutorials.com/
#
##########################


### CONSTANTS FOR EASE ###

# Moved to globalvars.py

warnings.filterwarnings("ignore")

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=2048)
pygame.mixer.init()

music_file = "dungeon_walk.mod"

pygame.mixer.music.load(music_file)
pygame.mixer.music.play(-1)  # -1 = loop forever

# Optional: lower volume if it's screaming
# pygame.mixer.music.set_volume(0.7)


"""
if (pygame.mixer.music.get_busy()):
    pygame.mixer.music.pause()
else:
    pygame.mixer.music.unpause()


"""


def save_game(handler: input_handlers.BaseEventHandler, filename: str) -> None:
    """If the current event handler has an active Engine then save it."""
    if isinstance(handler, input_handlers.EventHandler):
        handler.engine.save_as(filename)
        print("Game saved.")


def main() -> None:
    screen_width = globalvars.GAME_SCREENWIDTH
    screen_height = globalvars.GAME_SCREENHEIGHT

    #game_tilesheetsdir = "tilesheets/"
    #game_tilesheet = "Anikki_square_20x20.png"
    #game_tilesheet = "VGA9x16.png"
    #game_tilesheet = "Md_curses_16x16.png"

    tileset = tcod.tileset.load_tilesheet(
        #"dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
        globalvars.GAME_TILESHEETSDIR + globalvars.GAME_TILESHEET, 16, 16, tcod.tileset.CHARMAP_CP437
    )

    handler: input_handlers.BaseEventHandler = setup_game.MainMenu()
    
    tcod.sdl.render.ScaleMode(0)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title=globalvars.GAME_TITLEBAR,
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        try:
            while True:
                root_console.clear()
                handler.on_render(console=root_console)
                context.present(root_console)

                try:
                    for event in tcod.event.wait():
                        context.convert_event(event)
                        handler = handler.handle_events(event)
                except Exception:  # Handle exceptions in game.
                    traceback.print_exc()  # Print error to stderr.
                    # Then print the error to the message log.
                    if isinstance(handler, input_handlers.EventHandler):
                        handler.engine.message_log.add_message(
                            traceback.format_exc(), color.error
                        )
        except exceptions.QuitWithoutSaving:
            raise
        except SystemExit:  # Save and quit.
            save_game(handler, "savegame.sav")
            raise
        except BaseException:  # Save on any other unexpected exception.
            save_game(handler, "savegame.sav")
            raise
            

if __name__ == "__main__":
    main()