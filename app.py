from flask import Flask, request, render_template, jsonify
import bot as bot

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
   return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
   file = request.files['file']
   file.save('./datafile.txt')
   
   return render_template('loadingAndResults.html')


@app.route('/task', methods=['GET'])
def task():
  # Runs the bot and returns the file_path which the result was saved
  file_path = bot.runBot('./datafile.txt')
  
  # Passes the file path to the view so that it can be downloaded
  return jsonify({'done': True, 'file':file_path})