#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<alen-alex>
  Purpose: serve as the message and picture storage backend of
           AllChat IM server
  Created: 2014/10/18
"""
import os
import retrieve
from flask import Flask, request
app = Flask(__name__)

from storage import MessageSaver
saver = MessageSaver()

@app.route("/saveSingleMsg/", methods=["POST"])
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

@app.route("/saveGroupMsg/", methods=["POST"])
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

@app.route("/savePicture/", methods=["POST"])
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

@app.route("/getSingleMsg/", methods=["GET"])
def getSingleMsg():
    try:
        header = request.headers
    except:
        return ("Can not parse header.", 403)
    sender = header.get("sender", None)
    receiver = header.get("receiver", None)
    start_date = header.get("start_date", None)
    end_date = header.get("end_date", None)
    if not all((sender, receiver, start_date, end_date)):
        return ("Required paras not found.", 404)
    users = "&&".join(set((sender, receiver)))
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    directory = os.path.join(root, "data", "single_messages", users)
    if os.path.exists(directory):
        return retrieve.getMessages(directory, start_date, end_date)
    else:
        return "Does not have any records."
    return "This is getSingleMsg."

@app.route("/getGroupMsg/", methods=["GET"])
def getGroupMsg():
    try:
        header = request.headers
    except:
        return ("Can not parse header.", 403)
    group_id = header.get("group_id", None)
    start_date = header.get("start_date", None)
    end_date = header.get("end_date", None)
    if not all((group_id, start_date, end_date)):
        return ("Required paras not found.", 404)
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    directory = os.path.join(root, "data", "group_messages", str(group_id))
    if os.path.exists(directory):
        return retrieve.getMessages(directory, start_date, end_date)
    else:
        return "Does not have any records."
    return "This is getSingleMsg."

if __name__=="__main__":
    app.run()
