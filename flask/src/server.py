from flask import Flask, session, render_template, request, redirect, url_for, send_from_directory
from pymongo import MongoClient
import os
import time
import datetime
from urllib.parse import urlparse


AVATAR_LINK = "https://i.ibb.co/0nmJ0by/profile.jpg"
MONGO_IP = "172.20.0.3"
MONGO_USER = "root"
MONGO_PW = "example"
MONGO_ROUTE = f"mongodb://{MONGO_USER}:{MONGO_PW}@{MONGO_IP}:27017/"

app = Flask(__name__)

myclient = MongoClient(MONGO_ROUTE)

def query_database():
  db = myclient["admin"]
  collection = db["system.users"]
  query = list(collection.find())
  return query

@app.route('/database')
def database():
  dbs = myclient.list_database_names()
  return str(dbs)

@app.route('/')
def index():
  query = query_database()
  return render_template('index.html', query=query)

@app.route('/cv')
def cv():
  return render_template('cv.html')

@app.route('/resume')
def resume():
  workingdir = os.path.abspath(os.getcwd())
  print(workingdir)
  filepath = workingdir + '/static/misc/'
  return send_from_directory(filepath, 'Resume.pdf')

@app.route('/welcome')
def welcome():
  return render_template('welcome.html')

@app.route('/avatar')
def avatar():
  return {"image_src": AVATAR_LINK}

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
