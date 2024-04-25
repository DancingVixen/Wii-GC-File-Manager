# Wii GameCube File Manager

## Overview

we are all familiar with how stupid the file directories need to be setup in order to play GameCube ISOs on your Homebrewed Wii, I did an online search and everyone complains about this being a very tedious manual process with no way to automate it. Recently had a customer request over 100 GC games on their Wii, and I obviously was not going to spend 3 hours manually renaming and copying files, hence this was created.

Wii GameCube File Manager is a Python script designed to simplify the organization of GameCube ROMs for use with WiiFlow and Nintendont on the Wii console. It copies GameCube ISO files from one directory to another, creating a folder for each game and renaming the ISO file to ,,game.iso" within that folder.

For example, it can take a very nicely organised ,,GameCube ROM" directory where all of your roms are in ,,[real game name].iso" format, copy the file, paste it in a specified destination directory (i.e your Wii SD card), create a folder based on the game name, and past the ,,[real game name].iso" file inside the folder. It will then rename that to ,,game.iso" to comply with Nintendont requirements.

## Features

- **Effortless Gamecube ROM Management**: The script automates the process of organizing GameCube ROMs by creating folders for each game and renaming the ISO files to,,game.iso."

- **Simple Operation**: Just specify the input directory containing your GameCube ISO files and the output directory where you want them organized, and the script handles the rest.
- **Progress Bars**: Super cool Sci-Fi progress bars to show the file copying proggess, alongside an estimated transfer time.
- **File Name/Size Preview**: Not sure if your selected files will fit in your new directory? This programme will provide the selected file sizes, and total copy size, BEFORE copying. - Now that's neat!
- **Russian and English Support**: Russian and English language, with support for cyrillic input including directories. Had to do this since the original script would freak out over my non-latin name being in the directory. 

## Usage

1. **Installation**:
   - Clone the repository or download the script file (`wii_gamecube_file_manager.py`).
   - Ensure you have Python installed on your system (version 3.10.6 or higher).
   - `pip install tqdm`

2. **Execution**:
   - Open a terminal or command prompt and navigate to the directory containing `wii_gamecube_file_manager.py`.
   - Run the script using the command `python wii_gamecube_file_manager.py`.
   - Follow the on-screen instructions to specify the input and output directories.

3. **Result**:
   - The script will organize your GameCube ROMs by creating folders for each game and renaming the ISO files to ,,game.iso," making them ready for use with WiiFlow and Nintendont.

## Compatibility

- Compatible with Windows, macOS, and Linux operating systems.
- Requires Python (version 3.6.10 or higher) installed on your system.

## Support and Feedback

For any issues, suggestions, or feedback, please open an issue on this repository.

If you require a fast response time, message me on discord: `sashaafterbark`

## License

idk what this even means, feel free to steal my code if you want, i dont care

## uwu
из России с любовью
