
"""
This script creates a directory junction on Windows, essentially a symbolic link, for a Blender addon. 
The junction links the addon from its source location to the desired Blender version's addons folder. 
This automates the process of setting up Blender addons, especially when addons are being developed 
and frequently updated in a separate working directory.

Usage:
------
The script takes three main arguments:

1. Blender Version: Specify the Blender version's addons directory where the junction should be created.
   Use the `-b` or `--blender_version` flag followed by the Blender version string (e.g., "3.4").
   
2. Addon Name: Specify the exact name of the addon folder you want to create the junction for.
   Use the `-a` or `--addon_name` flag followed by the addon name string.

3. Source Location (Optional): Specify the directory where the addon is located.
   Use the `-s` or `--source` flag followed by the source directory.
   If this argument is omitted, it defaults to "L:\BLENDER\ADDONS\".

The script requires the `blender_version` and `addon_name` to be specified in order to create the junction.
If no arguments are specified, the script will print out the help message and terminate.

Examples:
---------
Creating a junction for an addon called "my-blender-addon" for Blender version 3.4:

    python junction_for_blender_addon.py -b 3.4 -a my-blender-addon

Creating a junction with a specified source location:

    python junction_for_blender_addon.py -b 3.4 -a my-blender-addon -s C:\\MyAddons\\

Note:
-----
This script is designed to work on Windows due to the use of the `mklink` command.
The Blender addons folder is typically located in the user's AppData folder (accessed with %APPDATA%),
and this script constructs that path dynamically for the specified Blender version.

The script also outputs the constructed paths and the actual command line string that it will use to create the junction.
Please ensure you have the necessary permissions to create junctions on the system.
"""


import os
import sys
import argparse
from colorama import Fore, init

init(autoreset=True)

parser = argparse.ArgumentParser(
    prog='make_junction.py',
    description='Create a junction for a blender addon in the specified blender addons folder.',
    epilog='IE: make_junction -b 3.4 -a my-blender-addon -s C:\\MyAddons\\'
)

# Argument to specify the blender version (Required)
parser.add_argument('-b', '--blender_version', metavar='B', type=str, nargs='*',
                    help='the blender version as a string, ie: "3.4", "3.5"\
                        As the name of the folder you see in the addons blender folder\
                        "...AppData\Roaming\Blender Foundation\Blender"')

# Argument to specify the name of the addon (Required)
parser.add_argument('-a', '--addon_name', metavar='A', type=str, nargs='*',
                    help='the name of the addon you want to create the junction for\
                        ie: "my-blender-addon"\n')

# Argument to specify the source location of the addon, the addon folder (Optional)
parser.add_argument('-s', '--source', metavar='SOURCE', type=str, nargs='*', default='L:\\BLENDER\\ADDONS\\',
                    help='the source location of the addon, the addon folder. Default is "L:\\BLENDER\\ADDONS\\"')

args = parser.parse_args()

# If no arguments are passed, print the help
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

# Parse Blender Version
blender_version = args.blender_version[0]

# Construct Blender Addons Folder from Blender Version
blender_addons_folder = os.path.join(os.getenv(
    'APPDATA'), 'Blender Foundation', 'Blender', blender_version, 'scripts', 'addons')

print()
print(Fore.GREEN + 'Blender Version: ' + Fore.RESET + blender_version)
print(Fore.GREEN + 'Destination: ' + Fore.RESET +
      '"' + blender_addons_folder + '"')

# Parse Addon Name
addon_name = args.addon_name[0]

# Parse Source Location (Default is "L:\BLENDER\ADDONS\")
source = args.source[0]
source = "".join(args.source)

print()
print(Fore.LIGHTBLUE_EX + 'Addon Name: ' + Fore.RESET + addon_name)
print(Fore.LIGHTBLUE_EX + 'Source: ' + Fore.RESET + '"' + source + '"')

if not os.path.exists(blender_addons_folder):
    print()
    print(Fore.RED + 'Blender Addon folder does not exist for the specified version')
    sys.exit(1)


cmd = 'mklink /J /D "' + os.path.join(blender_addons_folder,
                                      addon_name) + '" "' + os.path.join(source, addon_name) + '"'

print()
# print('cmd: ' + cmd)

os.system(cmd)
