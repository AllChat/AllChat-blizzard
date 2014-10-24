# -*- coding:utf-8 -*-
from flask import Flask, request
app = Flask(__name__)

# from storage import MessageSaver
# saver = MessageSaver()

@app.route("/saveSingleMsg", methods=["POST"])
def saveSingleMsg():
    return "singe message saved."

@app.route("/saveGroupMsg", methods=["POST"])
def saveGroupMsg():
    return "group message saved."

@app.route("/savePicture", methods=["POST"])
def savePicture():
    return "picture saved."

if __name__=="__main__":
    app.run()