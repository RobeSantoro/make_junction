# Blender Addon Junction Creator

This Python script facilitates the quick setup of Blender addons by creating a directory junction (a type of symbolic link on Windows) from an addon's source directory to a targeted Blender version's addons folder. It's particularly useful for addon developers who frequently update their code and need to test it within Blender.

## Requirements

- Windows Operating System
- Python 3 (tested with Python 3.11)  

The script is designed for Windows due to its reliance on `mklink`, a Windows-specific command-line utility.

## Usage

To create a junction for your Blender addon, you need to specify the Blender version and the name of the addon. Optionally, you can also specify the source location of the addon directory. If not provided, the default source location is `L:\BLENDER\ADDONS\`.

### Command-line Arguments

- `-b` or `--blender_version` (Required): The Blender version string, corresponding to the addons folder name (e.g., "3.4").
- `-a` or `--addon_name` (Required): The name of the addon folder for which you want to create the junction.
- `-s` or `--source` (Optional): The full path to the addon's source directory. If not provided, it defaults to `L:\BLENDER\ADDONS\`.

### Examples

1. To create a junction for an addon named "my_blender_addon" within the Blender 3.4 addons directory:

```bash
python make_junction.py -b 4.0 -a my_blender_addon
```

1. To specify a custom source location for the addon:

```bash
python make_junction.py -b 4.0 -a my_blender_addon -s C:\Path\To\Your\Addon
```

### Important Notes

- Ensure that you run the script with administrative privileges as creating a directory junction requires such permissions.
- The script assumes that your Blender addons folder is located in the typical location within `%APPDATA%\Blender Foundation\Blender`, if your Blender installation is at a custom location you will need to modify the script accordingly.

## Support

For bug reporting and feature requests, please open an issue in this repository.

## License

This project is open-source and available under the [MIT License](LICENSE).
