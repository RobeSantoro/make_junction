import os
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