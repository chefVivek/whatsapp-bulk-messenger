Sure! Below are examples of a `README.md` and a `LICENSE` file for your project.

### README.md
```markdown
# WhatsApp Bulk Messenger

WhatsApp Bulk Messenger is a Python-based automation tool that allows you to send bulk messages to multiple contacts on WhatsApp Web. The tool uses Selenium to automate the message-sending process.

## Features
- Send bulk messages to multiple contacts
- Attach an image with the message
- Easy-to-use graphical user interface (GUI) using Tkinter

## Requirements
- Python 3.x
- Selenium
- WebDriver Manager
- Tkinter (comes pre-installed with Python)

## Installation
1. Clone the repository or download the code:
   ```bash
   git clone https://github.com/chefVivek/whatsapp-bulk-messenger.git
   cd whatsapp-bulk-messenger
   ```

2. Install the required Python packages:
   ```bash
   pip install selenium webdriver-manager
   ```

3. Install Google Chrome and the corresponding ChromeDriver:
   - Download and install Google Chrome: [Chrome Download](https://www.google.com/chrome/)
   - ChromeDriver will be installed automatically by the `webdriver-manager` package.

## Usage
1. Prepare your contacts and message:
   - `numbers.txt`: A text file containing the phone numbers (one per line) of the contacts you want to message.
   - `message.txt`: A text file containing the message you want to send.

2. Run the script:
   ```bash
   python main.py
   ```

3. Follow the on-screen instructions to input the country code, numbers, message, and image path.

## Creating an Executable
To create an executable file from the Python script, you can use PyInstaller:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

The executable will be generated in the `dist` directory.

