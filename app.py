from flask import Flask, request, render_template, jsonify, send_file
import bot as bot
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
   return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
   file = request.files['file']
   file.save('./datafile.xlsx')
   
   return render_template('loadingAndResults.html')


@app.route('/task', methods=['GET'])
def task():
  # Runs the bot and returns the file_path which the result was saved
  file_path = bot.runBot('./datafile.xlsx')
  
  # Passes the file path to the view so that it can be downloaded
  file_name = os.path.basename(file_path)
  return jsonify({'done': True, 'file':file_name})


@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    # Get the full path to the file
    file_path = os.path.join(app.root_path, 'Scan_results', filename)

    # Check if the file exists
    if os.path.exists(file_path):
        # Send the file to the client for download
        return send_file(file_path, as_attachment=True)
    else:
        return "File not found", 404


if __name__ == '__main__':
    app.run(debug=True)