```markdown
# GUI AI Assistant

This is a GUI-based AI Assistant that uses Google Gemini 2.0 for image-based content generation and question answering. It allows you to capture images from your webcam, send them with prompts to Gemini, and get detailed responses in an interactive graphical interface.

## Features:

* Capture an image from your webcam via GUI.
* Send the image along with prompts to Gemini for analysis.
* Ask follow-up questions about the captured image.
* Interactive graphical user interface using tkinter.

## Installation:

1. Clone the repository:
```

   ```bash
   git clone https://github.com/SoulSniper1212/AI-WEBCAM-GUI.git
   cd AI-WEBCAM-GUI
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set your Google Gemini API key:

   * Create a `.env` file in the root directory:

     ```bash
     echo "GEMINI_API_KEY=your_api_key_here" > .env
     ```

## Usage:

Run the script using:

```bash
python3 main.py
```

The GUI window will open, allowing you to capture photos, analyze them with Gemini, and ask follow-up questions.

## Notes:

* Ensure your webcam is connected and functional before running the app.
* Make sure your `.env` file is in the same directory as `main.py`.

## Requirements:

* Python 3.8+
* OpenCV
* Pillow
* Google Generative AI
* tkinter
* dotenv

You can find all dependencies in `requirements.txt`.

## License:

Custom License for GUI AI Assistant

Permission is granted to use this software for personal and educational purposes only. Commercial use, modification, or redistribution of this software, in whole or in part, is strictly prohibited without explicit written permission from the author.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY ARISING FROM THE USE OF THE SOFTWARE.

## Author:

Arush Wadhawan
```
