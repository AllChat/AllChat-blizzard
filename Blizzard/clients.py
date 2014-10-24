# -*- coding:utf-8 -*-
from flask import Flask
app = Flask(__name__)

from storage import MessageSaver
saver = MessageSaver()

@app.route("/saveSingleMsg")
def saveSingleMsg():
    pass

@app.route("/saveGroupMsg")
def saveGroupMsg():
    pass

@app.route("/savePicture")
def savePicture():
    pass

if __name__=="__main__":
    app.run()