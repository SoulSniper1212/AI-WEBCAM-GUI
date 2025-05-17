import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
import cv2
import base64
import io
import os
from dotenv import load_dotenv
from google import generativeai as genai

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please set it in the .env file.")

image_data = {"base64": None}
conversation_history = []

def send_to_gemini(image_base64, prompt, history):
    """Send image and prompt to Gemini API and receive the response."""
    try:
        genai.configure(api_key=API_KEY)
        image_bytes = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(image_bytes))
        model = genai.GenerativeModel(model_name="gemini-2.0-flash")
        
        full_prompt = ""
        for item in history:
            full_prompt += f"{item['role'].capitalize()}: {item['content']}\n"
        full_prompt += f"User: {prompt}"
        
        response = model.generate_content([full_prompt, image])
        return response.text
    except Exception as e:
        return f"Error: {e}"

def main():
    cap = cv2.VideoCapture(0)

    def update_frame():
        ret, frame = cap.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_resized = cv2.resize(frame_rgb, (0, 0), fx=0.6, fy=0.6)
            img = Image.fromarray(frame_resized)
            imgtk = ImageTk.PhotoImage(image=img)
            video_label.imgtk = imgtk
            video_label.configure(image=imgtk)
        root.after(30, update_frame)

    def capture_image_and_send_to_ai():
        ret, frame = cap.read()
        if not ret:
            messagebox.showerror("Error", "Could not capture image.")
            return
        _, buffer = cv2.imencode('.jpg', frame)
        image_data["base64"] = base64.b64encode(buffer).decode('utf-8')
        
        prompt = "Describe what you see in this image in a couple sentences."
        conversation_history.clear()
        conversation_history.append({"role": "user", "content": prompt})
        response = send_to_gemini(image_data["base64"], prompt, conversation_history)
        conversation_history.append({"role": "assistant", "content": response})

        response_text.config(state="normal")
        response_text.delete(1.0, tk.END)
        response_text.insert(tk.END, response)
        response_text.config(state="disabled")

    def continue_conversation_with_new_photo():
        if not use_previous_photo.get():
            ret, frame = cap.read()
            if not ret:
                messagebox.showerror("Error", "Could not capture image.")
                return
            _, buffer = cv2.imencode('.jpg', frame)
            image_data["base64"] = base64.b64encode(buffer).decode('utf-8')

        if not image_data["base64"]:
            messagebox.showerror("Error", "No photo has been captured yet.")
            return

        prompt = question_input.get().strip()
        if not prompt:
            messagebox.showwarning("Empty Prompt", "Please enter a question.")
            return

        conversation_history.append({"role": "user", "content": prompt})
        response = send_to_gemini(image_data["base64"], prompt, conversation_history)
        conversation_history.append({"role": "assistant", "content": response})

        response_text.config(state="normal")
        response_text.delete(1.0, tk.END)
        response_text.insert(tk.END, response)
        response_text.config(state="disabled")

    def exit_app():
        cap.release()
        root.quit()

    root = tk.Tk()
    root.title("Ollama AI Assistant")
    root.state('zoomed')  # Fullscreen mode
    use_previous_photo = tk.BooleanVar(value=True)

    video_label = tk.Label(root, relief=tk.SUNKEN, width=640, height=480)
    video_label.pack(pady=10)

    response_text = ScrolledText(root, height=4, wrap=tk.WORD, state="disabled")
    response_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    question_frame = tk.Frame(root)
    question_frame.pack(pady=5)
    question_input = tk.Entry(question_frame, width=40, font=("Arial", 12))
    question_input.pack(side=tk.LEFT, padx=10)

    toggle_frame = tk.Frame(root)
    toggle_frame.pack(pady=2)
    photo_toggle = tk.Checkbutton(toggle_frame, text="Use previous photo for follow-up question", variable=use_previous_photo)
    photo_toggle.pack()

    button_frame = tk.Frame(root)
    button_frame.pack(pady=5)

    capture_button = tk.Button(button_frame, text="Capture Photo and Analyze", command=capture_image_and_send_to_ai, width=25)
    capture_button.pack(side=tk.TOP, pady=5)

    ask_question_button = tk.Button(button_frame, text="Ask Question", command=continue_conversation_with_new_photo, width=25)
    ask_question_button.pack(side=tk.TOP, pady=5)

    exit_button = tk.Button(button_frame, text="Exit", command=exit_app, width=25)
    exit_button.pack(side=tk.TOP, pady=5)

    update_frame()
    root.mainloop()

if __name__ == '__main__':
    main()
