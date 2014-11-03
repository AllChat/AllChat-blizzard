# -*- coding:utf-8 -*-
from flask import Flask, request
app = Flask(__name__)

from storage import MessageSaver
saver = MessageSaver()

@app.route("/saveSingleMsg", methods=["POST"])
def saveSingleMsg():
    try:
        para = request.get_json()
    except:
        return ("Can not parse json data.", 403)
    sender = para.get("sender", None)
    receiver = para.get("receiver", None)
    message = para.get("message", None)
    if not all((sender, receiver, message)):
        return ("Required paras not found.", 404)
    saved = saver.saveSingleMsg(sender, receiver, message)
    if saved:
        return "Singe message saved."
    else:
        return ("Invalid para values.", 404)

@app.route("/saveGroupMsg", methods=["POST"])
def saveGroupMsg():
    try:
        para = request.get_json()
    except:
        return ("Can not parse json data.", 403)
    sender = para.get("sender", None)
    group_id = para.get("group_id", None)
    message = para.get("message", None)
    if not all((sender, group_id, message)):
        return ("Required paras not found.", 404)
    saved = saver.saveGroupMsg(sender, group_id, message)
    if saved:
        return "Group message saved."
    else:
        return ("Invalid para values.", 404)

@app.route("/savePicture", methods=["POST"])
def savePicture():
    try:
        para = request.get_json()
    except:
        return ("Can not parse json data.", 403)
    content = para.get("content", None)
    format_ = para.get("format", None)
    if not all((content, format_)):
        return ("Required paras not found.", 404)
    saved = saver.savePicture(content, format_)
    if saved:
        return "Picture saved."
    else:
        return ("Invalid para values.", 404)

if __name__=="__main__":
    app.run()
