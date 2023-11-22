# Blender Addon Junction Creator

This Python script facilitates the quick setup of Blender addons by creating a directory junction (a symbolic link on Windows) from an addon's source directory to a targeted Blender version's addons folder. It's beneficial for developers who frequently update their addon repository in one location and must test it within multiple Blender versions.

## Requirements

- Windows Operating System
- Python 3 (tested with Python 3.11)

The script is designed for Windows due to its reliance on `mklink`, a command-line utility specific to Windows.

## Usage

To create a junction for your Blender addon, you need to specify the Blender version and the name of the addon. Optionally, you can also specify the source location of the addon directory. If not provided, the default source location is `L:\BLENDER\ADDONS\`, which is the location of my own add-on source repositories.

You can use either flags or positional arguments for `blender_version`, `addon_name`, and `source`.

### Command-line Arguments

- `-b` or `--blender-version`: The Blender version string corresponding to the addons folder name (e.g., "3.4").
- `-a` or `--addon-name`: The name of the addon folder to which you want to create the junction.
- `-s` or `--source`: The full path to the addon's source directory. If not provided, it defaults to `L:\BLENDER\ADDONS\`.

## Building the Script into a Standalone Executable

To build the script into a standalone executable, you can use [PyInstaller](https://www.pyinstaller.org/). Run the following command to create a single executable file in the `dist` directory:

```bash
pyinstaller --onefile make_junction.py
```

Or download the latest release from the [Releases](https://github.com/RobeSantoro/make_junction/releases/download/v1.0.2/make_junction.exe) page. Then move the executable to a directory in your `PATH` environment variable to use it from anywhere.

## Examples

- To create a junction for an addon named "MyAddon" within the Blender 4.0 addons directory using flags:

    ```bash
    make_junction -b 4.0 -a MyAddon
    ```

- To specify a custom source location for the addon using flags:

    ```bash
    make_junction -b 4.0 -a MyAddon -s C:\MyAddon\
    ```

- To create a junction using positional arguments:

    ```bash
    make_junction 4.0 MyAddon C:\MyAddon\
    ```

- To create a junction with a default source directory using positional arguments:

    ```bash
    make_junction 4.0 MyAddon
    ```

## Support

For bug reporting and feature requests, please open an issue in this repository.

## License

This project is open-source and available under the [MIT License](LICENSE)
