"""
This script facilitates the quick setup of Blender addons by creating a directory junction 
from an addon's source directory to a targeted Blender version's addons folder.
It's beneficial for developers who frequently update their addon repository in one location
and must test it within various Blender versions
"""

import os
import sys
import argparse
from colorama import Fore, init

init(autoreset=True)

parser = argparse.ArgumentParser(
    prog='make_junction.py',
    description=f'Create a junction for a blender addon for specific blender version. Choose between flags {Fore.RED}OR{Fore.RESET} positional arguments usage.',
    epilog=f'make_junction -b 3.4 -a MyAddon -s C:\\MyAddon\\ {Fore.RED}OR{Fore.RESET} make_junction 3.4 MyAddon C:\\MyAddon\\'
)

# Argument to specify the blender version (Required, positional or as a flag)
parser.add_argument('blender_version', nargs='?', type=str,
                    help='The Blender version as a string, e.g., "3.4".')
parser.add_argument('-b', '--blender_version', dest='blender_version_flag', type=str,
                    help='The Blender version as a string, e.g., "3.4".')

# Argument to specify the name of the addon (Required, positional or as a flag)
parser.add_argument('addon_name', nargs='?', type=str,
                    help='The name of the addon, e.g., "my-addon".')
parser.add_argument('-a', '--addon_name', dest='addon_name_flag', type=str,
                    help='The name of the addon, e.g., "my-addon".')

# Argument to specify the source location of the addon (Optional, positional or as a flag)
parser.add_argument('source', nargs='?', type=str, default='L:\\BLENDER\\ADDONS\\',
                    help='The source path of the addon. Default is "L:\\BLENDER\\ADDONS\\" + addon_name')
parser.add_argument('-s', '--source', dest='source_flag', type=str,
                    help='The source location of the addon.')

args = parser.parse_args()

# Decide which argument values to use based on whether the flags were provided
blender_version = args.blender_version_flag if args.blender_version_flag is not None else args.blender_version
addon_name = args.addon_name_flag if args.addon_name_flag is not None else args.addon_name
source = args.source_flag if args.source_flag is not None else args.source

# If no Blender Version or Addon Name are provided, display help
if not blender_version or not addon_name:
    parser.print_help()
    sys.exit(1)

# Construct Blender Addons Folder from Blender Version
blender_addons_folder = os.path.join(
    os.getenv('APPDATA'),
    'Blender Foundation',
    'Blender',
    blender_version,
    'scripts',
    'addons'
    )

junction_path = os.path.join(blender_addons_folder, addon_name)

# If the source is the default, append the addon name
if source == 'L:\\BLENDER\\ADDONS\\' and addon_name:
    
    # Check if the addon exists in the default source path
    if os.path.exists(os.path.join(source, addon_name)):
        source = os.path.join(source, addon_name)
    else:
        print()
        print(Fore.RED + 'ERROR')
        print(Fore.RED + 'Addon not found in Source path specified:')
        print()
        print(os.path.join(source, addon_name))
        print()
        sys.exit(1)

else:
    source = os.path.abspath(source)
        

# Check if the destination Blender addons folder exists
if not os.path.exists(blender_addons_folder):
    print()
    print(Fore.RED + 'ERROR')
    print(Fore.RED + 'Blender Addon folder does not exist for the specified version.')
    print()
    print(os.path.join(
    os.getenv('APPDATA'),
    'Blender Foundation',
    'Blender',
    Fore.RED + blender_version + Fore.RESET,
    'scripts',
    'addons'
    ))
    print()
    sys.exit(1)

# Print a recap of the arguments
print()
print(Fore.YELLOW + 'Creating Junction with the following arguments:')
print()
print(Fore.GREEN + f'Blender Version: { Fore.RESET + blender_version}')
print(Fore.GREEN + f'Addon Name: { Fore.RESET + addon_name}')
print()
print(Fore.LIGHTCYAN_EX + f'Source: { Fore.RESET + source}')
print(Fore.LIGHTCYAN_EX + f'Destination: { Fore.RESET + junction_path}')
print()

# Command to create the directory junction
cmd = f'mklink /J "{junction_path}" "{source}"'

# Execute the command to create the junction
os.system(cmd)
print()
