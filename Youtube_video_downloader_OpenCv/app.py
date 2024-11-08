from flask import Flask, render_template, request, jsonify
import pafy
import os
import youtube_dl

app = Flask(__name__)

# Route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle video download requests
@app.route('/download', methods=['POST'])
def download_video():
    data = request.get_json()
    video_url = data['video_url']
    save_location = data['save_location']

    try:
        # Using youtube-dl to download the video
        ydl_opts = {
            'outtmpl': os.path.join(save_location, '%(title)s.%(ext)s'),
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        return jsonify({'success': True, 'message': 'Video downloaded successfully!'})

    except Exception as e:
        print(f"Error downloading video: {e}")
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
