import logging
import os
import json
import time
import pwnagotchi.plugins as plugins
from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts

class WofBridge:
    def __init__(self, json_file):
        self.__json_file = json_file
        known_flippers = self.__load_data()
        self.__known_flippers = [ flipper["UUID"] for flipper in known_flippers ]
        if len(self.__known_flippers) > 0:
            logging.info(f"Already met {len(self.__known_flippers)} Flipper")

    def get_update(self):
        update = {
            "new": [],
            "online": [],
            "met": 0
        }
        
        flippers = self.__load_data()
        flippers.sort(key = lambda flipper: flipper["unixLastSeen"], reverse = True)
        for flipper in flippers:
            # new discovered flippers
            if flipper["UUID"] not in self.__known_flippers:
                self.__known_flippers.append(flipper["UUID"])
                update["new"].append(flipper["Name"])
        
            # online flippers (it is considered if last seen is max 5 minutes ago)
            if time.time() - flipper["unixLastSeen"] < 60 * 5:
                update["online"].append(flipper["Name"])

        update["met"] = len(self.__known_flippers)

        return update

    def __load_data(self):
        if os.path.isfile(self.__json_file):
            with open(self.__json_file) as file:
                try:
                    return json.loads(file.read())
                except Exception as e:
                    logging.critical(f"Error while loading and parsing json file: {e}")
                    return []
        else:
            logging.critical(f"File not found: {self.__json_file}")
            return []


class WofPlugin(plugins.Plugin):
    __author__ = 'CyberArtemio'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'Display found Flipper Zeros from Wall of Flippers'
    
    DEFAULT_POS = (5, 83) # TODO: load from config and use this as a fallback
    JSON_FILE = "/root/Wall-of-Flippers/Flipper.json" # TODO: load from config and use this as a fallback


    def on_loaded(self):
        logging.debug("Initializing wof plugin...")
        self.__wof_bridge = WofBridge(self.JSON_FILE)
        logging.debug("Checking that wof is installed...") # TODO: check installation
        logging.debug("Checking that wof is running...") # TODO: check running

    # called before the plugin is unloaded
    def on_unload(self, ui):
        logging.debug("Stop wof")

    # called to setup the ui elements
    def on_ui_setup(self, ui):
        # add custom UI elements
        ui.add_element('wof', LabeledValue(color=BLACK,
                                           label='[wof]',
                                           value=" - ",
                                           position=self.DEFAULT_POS,
                                           label_font=fonts.Medium,
                                           text_font=fonts.Medium))

    # called when the ui is updated
    def on_ui_update(self, ui):
        flippers = self.__wof_bridge.get_update()

        if len(flippers["new"]) > 0:
            if len(flippers["new"]) == 1:
                ui.set('status', f'Ooh, just met F0 {flippers["new"][0]}')
            else:
                ui.set('status', f'Yooh, just met {len(flippers["new"])} new F0')
        
        if len(flippers["online"]) == 0:
            ui.set('wof', f' {flippers["met"]} F0 met')
        else:
            ui.set('wof', f'{flippers["online"][0]} ({flippers["met"]})')
