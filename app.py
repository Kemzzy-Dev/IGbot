from flask import Flask, request, render_template, jsonify
import bot as bot

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
   return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
   file = request.files['file']
   # Now you can save the file, read its contents, etc.
   file.save('./data.txt')
   
   return render_template('loadingAndResults.html')


@app.route('/task', methods=['GET'])
def task():
  file_path = bot.runBot('./data.txt')
  
  return jsonify({'done': True, 'file':file_path})