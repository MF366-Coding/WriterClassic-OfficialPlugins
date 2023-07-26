"""
    WriterClassic !presence

Discord Rich Presence for WriterClassic

DON'T SHARE YOUR CLIENT ID WITH ANYONE!
IT'S YOURS AND YOURS ONLY!

Insert it here and keep this file private!

Check README.md for more info!
"""

client_id = '6666666'  # Fake ID, please insert the correct one
update_loop = 5 # seconds





























from pypresence import Presence
from os import path
import time

def plugin(a, b, c):
    RPC = Presence(client_id)  # Initialize the client class
    RPC.connect() # Start the handshake loop

    filename = path.basename(c)

    print(
        RPC.update(state=f"Editing {str(filename)}",
                   details="Using WriterClassic",
                   large_image="logo")
        )  # Set the presence

    while True:  # The presence will stay on as long as the program is running
        time.sleep(update_loop) # Can only update rich presence every 15 seconds

title = "WriterClassic !presence Loader"
