from flask import Flask, request, render_template, jsonify
import scripts.bot as bot

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
   return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
   file = request.files['file']
   # Now you can save the file, read its contents, etc.
   file.save('../datasettest.txt')
   
   return render_template('loadingPage.html')


@app.route('/task', methods=['GET'])
def task():
  bot.runBot('../datasettest.txt')
  
  return jsonify({'done': True})