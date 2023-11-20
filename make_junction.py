
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
Creating a junction for an addon called "blender-2.80-3ds-io-3ds" for Blender version 3.4:

    python junction_for_blender_addon.py -b 3.4 -a blender-2.80-3ds-io-3ds

Creating a junction with a specified source location:

    python junction_for_blender_addon.py -b 3.4 -a blender-2.80-3ds-io-3ds -s C:\\MyAddons\\

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

parser = argparse.ArgumentParser(description='Create a junction for a blender addon in the specified blender addons folder')

# Argument to specify the blender version (Required)
parser.add_argument('-b', '--blender_version', metavar='B', type=str, nargs='+',
                    help='the blender version as a string, ie: "3.4", "3.5"\
                        As the name of the folder you see in the addons blender folder\
                        "...AppData\Roaming\Blender Foundation\Blender"')

# Argument to specify the name of the addon (Required)
parser.add_argument('-a', '--addon_name', metavar='A', type=str, nargs='+',
                    help='the name of the addon you want to create the junction for\
                        ie: "blender-2.80-3ds-io-3ds"\n')

# Argument to specify the source location of the addon, the addon folder (Optional)
parser.add_argument('-s', '--source', metavar='SOURCE', type=str, nargs='+', default='L:\\BLENDER\\ADDONS\\',
                    help='the source location of the addon, the addon folder. Default is "L:\\BLENDER\\ADDONS\\"')

args = parser.parse_args()

# If no arguments are passed, print the help
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

blender_version = args.blender_version[0]
print('blender_version: ' + blender_version)

addon_name = args.addon_name[0]
print('addon_name: ' + addon_name)

source = args.source[0]
source = "".join(args.source) # Join the source arguments to form a string
print('source: ' + source)

blender_addons_folder = os.path.join(os.getenv('APPDATA'), 'Blender Foundation', 'Blender', blender_version, 'scripts', 'addons')
print('blender_addons_folder: ' + blender_addons_folder)

if not os.path.exists(blender_addons_folder):
    print()
    print('Blender Addon folder does not exist for the specified version')
    exit()

cmd = 'mklink /J /D "' + os.path.join(blender_addons_folder, addon_name) + '" "' + os.path.join(source, addon_name) + '"'

print()
print('cmd: ' + cmd)

os.system(cmd)