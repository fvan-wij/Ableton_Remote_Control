from flask import Flask, render_template, redirect, url_for, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_recording', methods=['POST'])
def start_recording():
    subprocess.run(['python', 'TriggerRecording.py'])
    try:
        return redirect(url_for('index'))
    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)