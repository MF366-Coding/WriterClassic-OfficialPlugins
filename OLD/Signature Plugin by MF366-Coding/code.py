# Code for a Signature Plugin on Writer Classic
# There are 2 different ways to use this plugin

from tkinter import END
from getpass import getuser

"""
First of all:
INSTALLATION!

To install this plugin, first pick what version you want.
The versions are explained below.
Read all of this before actually installing the plugin.

If you picked version 1, you need to replace a slot from plugins.py with the code
for version 1 and you must also download signature.txt and place it on the
folder data/ that comes with WriterClassic

If you picked version 2, you only need to replace the slot with the code for version 2

For both versions, you'll also have to import the modules we request
yes, the ones that are at the start of this file
"""

# Ok, now that INSTALLATION is outta the way
# let's get this started!

'''
1) The first way is a plugin that adds a custom signature made by you.
That signature is saved in a txt file.
The signature is automatically added like this:

"""
Here we have some text that is part of a text document.
After the dot in this sentence, the user has clicked the plugin.

> Whatever your signature is
"""

So, using this version of the plugin goes like:
- the plugin presses ENTER
- the plugin presses ENTER again
- the plugin types whatever you typed on that signature txt file

So, there's no reason to add a breakline (ENTER) in the signature file
because the plugin already adds it automatically.

Great, right?!
'''


# The code starts here:
# version_1 is to identify that this is the version 1 of the plugin
# that is, the one that was explained above
# there is also version 2, which is after this section of code

title_version_1 = "Insert Signature (by MF366-Coding)"

def plugin_version_1(tk_root, tk_text):
    with open("data/signature.txt", "r", encoding="utf-8") as SIGNATURE_FILE:
        signature = SIGNATURE_FILE.read()
        SIGNATURE_FILE.close()
    
    tk_text.insert(END, f"\n\n{str(signature)}")


'''
2) The second way is a plugin that adds an auto signature, not made by the user at all
It uses instead your OS username
so if for your os, your name is jon banana
in the signature it will show up as Jon Banana

The signature is automatically added like this:
Note: in the following example, take jon banana as the username for the OS

"""
Here we have some text that is part of a text document.
After the dot in this sentence, the user has clicked the plugin.

--
Signed,
Jon Banana
"""

So, using this version of the plugin goes like:
- the plugin presses ENTER
- the plugin presses ENTER again
- the plugin types --
- the plugin presses ENTER... again, yes...
- the plugin types Signed,
- the plugin presses ENTER once more
- the plugin types your OS username but with the first letter of every work capitalized

Cool, right?!
'''


# The code starts here:
# version_2 is to identify that this is the version 2 of the plugin
# that is, the one that was explained above
# there is also version 1, which is before this section of code

title_version_2 = "Insert Auto Signature (by MF366-Coding)"

def plugin_version_2(tk_root, tk_text):
    username = getuser()
    transformed_username = username.title()
    
    signature = f"--\nSigned,\n{transformed_username}"
    
    tk_text.insert(END, f"\n\n{str(signature)}")
    
