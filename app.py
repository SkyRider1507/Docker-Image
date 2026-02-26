from flask import Flask, render_template_string
import subprocess

app = Flask(__name__)
VLC_PROCESS = None

HTML = """
<h1>Jayden's Homelab DVD Player</h1>
<button onclick="fetch('/play')">Play DVD</button>
<button onclick="fetch('/stop')">Stop</button>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/play")
def play():
    global VLC_PROCESS
    VLC_PROCESS = subprocess.Popen([
        "cvlc",
        "dvd:///mnt/dvd",
        "--sout",
        "#standard{access=http,mux=ts,dst=:1507}"
    ])
    return "Streaming started on port 1507"

@app.route("/stop")
def stop():
    global VLC_PROCESS
    if VLC_PROCESS:
        VLC_PROCESS.terminate()
    return "Stopped"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1507)
