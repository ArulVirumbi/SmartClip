# SmartClip

SmartClip is a clipboard management tool that helps you save and retrieve text snippets quickly using keyboard shortcuts. Whether you're working on multiple tasks or need to store frequently used text, SmartClip helps you streamline your workflow by providing easy access to your clipboard history.

## Features

- **Save Snippets**: Save selected text to the clipboard using the `Ctrl+Alt+C` keyboard shortcut.
- **Retrieve Snippets**: Retrieve saved text snippets using the `Ctrl+Alt+V` keyboard shortcut.
- **System Tray Icon**: The app runs in the background and can be controlled via the system tray icon.
- **Cross-Platform Support**: Works on both Windows and macOS systems.
- **Lightweight**: Minimal resource usage with a small memory footprint.

## How to Use

1. **Install Dependencies**:  
   First, install the required Python packages. You can do this by running:
   ```bash
   pip install pystray Pillow pyperclip keyboard
   ```

2. **Running the Application**:  
   To run SmartClip, simply execute the `main.py` file in your terminal:
   ```bash
   python main.py
   ```

3. **Using the Shortcuts**:
   - **Save Text**: Select any text, press `Ctrl+C` and then press `Ctrl+Alt+C` to save it by entering a key.
   - **Retrieve Text**: Press `Ctrl+Alt+V` to open a search window and enter your key and press enter to paste it.

4. **System Tray**:
   - The app will minimize to the system tray, where you can click on the tray icon to exit the application.

## Installation for Executable

You can also convert the application into a standalone executable for easy use on Windows or macOS. To create an `.exe` file for Windows:

1. **Install pyinstaller**:
   ```bash
   pip install pyinstaller
   ```

2. **Convert to Executable**:
   Run the following command to package the app into a single executable file:
   ```bash
   pyinstaller --onefile --noconsole main.py
   ```
   This will generate an executable that you can run without needing Python installed.

## Troubleshooting

- **Text Not Being Copied**: Ensure that the correct permissions are granted for clipboard access. On Windows, you might need to run the app as Administrator to allow clipboard access for certain applications.
- **System Tray Icon Not Showing**: Ensure that the pystray library is working correctly and your system allows tray icons. Some systems may have restrictions on system tray functionality.

## License

SmartClip is dual-licensed under the GNU AGPL v3 and a Commercial License.

AGPL v3: Allows free use for individual and non-commercial purposes but requires open-sourcing modifications.

Commercial License: Required for companies or professional/commercial use. See LICENSE-COMMERCIAL.md for details.

## Notes

SmartClip uses a local JSON file to store saved snippets. You can change the storage path by modifying the .env.local file.

Make sure the app has the necessary permissions for clipboard access, and the system tray icon should appear on most systems automatically after launching the app.

## Contributing

If you'd like to contribute to SmartClip, feel free to fork the repository, make your changes, and submit a pull request. Make sure to follow the coding conventions and add tests for new features.

## Contact

For support or suggestions, feel free to reach out at arul.virumbi@gmail.com.

