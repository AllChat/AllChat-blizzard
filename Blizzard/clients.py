# -*- coding:utf-8 -*-
from flask import Flask, request
app = Flask(__name__)

# from storage import MessageSaver
# saver = MessageSaver()

@app.route("/saveSingleMsg", methods=["POST"])
def saveSingleMsg():
    try:
        para = request.get_json()
    except:
        return "required paras not found."
    return "singe message saved."

@app.route("/saveGroupMsg", methods=["POST"])
def saveGroupMsg():
    try:
        para = request.get_json()
    except:
        return "required paras not found."
    return "group message saved."

@app.route("/savePicture", methods=["POST"])
def savePicture():
    try:
        para = request.get_json()
    except:
        return "required paras not found."
    return "picture saved."

if __name__=="__main__":
    app.run()