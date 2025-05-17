```markdown
# AI Assistant GUI

This is a **GUI-based AI Assistant** that uses Google Gemini 2.0 for image-based content generation and question answering. The app captures images from your webcam, sends them along with prompts to Gemini, and displays detailed responses in an interactive Tkinter interface.

## Features:

- Live webcam preview inside the GUI.
- Capture photo and send it for AI analysis.
- Ask follow-up questions with or without a new photo.
- Conversation history with the AI assistant.
- Easy-to-use graphical interface built with Tkinter.

## Installation:

1. Clone the repository:

```bash
git clone https://github.com/SoulSniper1212/AI-Assistant-GUI.git
cd AI-Assistant-GUI
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set your Google Gemini API key:

Create a `.env` file in the root directory with the following content:

```bash
GEMINI_API_KEY=your_api_key_here
```

Make sure to replace `your_api_key_here` with your actual API key.

## Usage:

Run the app using:

```bash
python main.py
```

## How to Use:

- The app will show a live webcam feed.
- Click **Capture Photo and Analyze** to take a snapshot and send it to the AI for description.
- Enter follow-up questions in the input box and click **Ask Question** to continue the conversation.
- Use the checkbox to decide whether to use the previous photo or capture a new one for follow-up questions.
- Click **Exit** to close the application.

## Requirements:

- Python 3.8+
- OpenCV
- Pillow
- Google Generative AI SDK
- python-dotenv
- requests

All dependencies are listed in `requirements.txt`.

## License:

Custom License for AI Assistant GUI

Permission is granted to use this software for personal and educational purposes only. Commercial use, modification, or redistribution of this software, in whole or in part, is strictly prohibited without explicit written permission from the author.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY ARISING FROM THE USE OF THE SOFTWARE.

## Author:

Arush Wadhawan

---

An interactive GUI application that leverages Google Gemini 2.0 to provide image-based insights from your webcam in real time, with a simple and user-friendly Tkinter interface.

```
