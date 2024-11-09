import os
from flask import Flask, request, render_template_string
from yt_dlp import YoutubeDL
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    # Load the HTML file for the form
    with open('index.html') as file:
        html_content = file.read()
    return render_template_string(html_content)

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form['url']
    output_name = request.form['output_name']
    
    # Set the output path based on user input (in the c://downloads directory)
    output_path = f"C:\\Downloads\\{output_name}.mp4"
    

    
    # yt-dlp options
    ydl_opts = {
        "format": "best[ext=mp4]",
        "outtmpl": output_path,
    }
    
    # Download the video
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    # Play the video using OpenCV
    play_video(output_path)
    
    return f"Video downloaded and saved as '{output_path}' and is now playing."

def play_video(path):
    vid = cv2.VideoCapture(path)
    if not vid.isOpened():
        print("Error: Could not open video.")
        return

    while vid.isOpened():
        ret, frame = vid.read()
        if not ret:
            print("Video complete or an error occurred.")
            break

        # Resize and display frame
        frame = cv2.resize(frame, (700, 560))
        cv2.imshow("Disclaimer: For stopping video Press key : c", frame)

        # Press 'c' to close the video window
        if cv2.waitKey(25) & 0xFF == ord("c"):
            break

    vid.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    app.run(debug=True)
