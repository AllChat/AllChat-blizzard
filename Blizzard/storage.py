# --*-- coding:utf-8 --*--
import os
import time
import hashlib
from threading import Timer
from collections import defaultdict

class MessageSaver(object):
    def __init__(self):
        self._single_message_dict = defaultdict(list)
        self._group_message_dict = defaultdict(list)
        self._current_directory = os.path.dirname(os.path.abspath(__file__))
        self._get_config()
        self._start_writing()

    def _get_config(self):
        root = os.path.dirname(self._current_directory)
        conf_path = os.path.join(root, "conf", "blizzard.conf")
        with open(conf_path,"rb") as conf:
            config_dict = dict(tuple(line.strip(";\n").split(" "))
                for line in conf)
        self._writing_interval = float(config_dict.get("writing_interval", 600))

    def _start_writing(self):
        if self._single_message_dict or self._group_message_dict:
            root = os.path.dirname(self._current_directory)
            date = time.strftime("%Y-%m-%d", time.localtime())
            year, month, day = date.split("-")
            file_name = time.strftime("%H-%M",time.localtime())+".bin"
            for users in self._single_message_dict.iterkeys():
                sender, receiver = users.split("&&")
                messages = "\r\n\r\n".join(self._single_message_dict[users])
                ## ...................................
                ## encrypt messages here... to be done
                ## ...................................
                directory = os.path.join(root, "data", "single_messages",
                    sender, receiver, year, month, day)
                if not os.path.exists(directory):
                    os.makedirs(directory)
                path = os.path.join(directory, file_name)
                with open(path,"wb") as output:
                    output.write(messages)
                directory = os.path.join(root, "data", "single_messages",
                    receiver, sender, year, month, day)
                if not os.path.exists(directory):
                    os.makedirs(directory)
                path = os.path.join(directory, file_name)
                with open(path,"wb") as output:
                    output.write(messages)
            self._single_message_dict = defaultdict(list)
            for group_id in self._group_message_dict.iterkeys():
                messages = "\r\n\r\n".join(self._group_message_dict[group_id])
                ## ...................................
                ## encrypt messages here... to be done
                ## ...................................
                directory = os.path.join(root, "data", "group_messages",
                    group_id, year, month, day)
                if not os.path.exists(directory):
                    os.makedirs(directory)
                path = os.path.join(directory, file_name)
                with open(path,"wb") as output:
                    output.write(messages)
            self._group_message_dict = defaultdict(list)
        timer = Timer(self._writing_interval, self._start_writing)
        timer.start()

    def saveSingleMsg(self, sender, receiver, msg):
        if isinstance(sender, unicode) and sender \
            and(isinstance(receiver, unicode) and receiver) \
            and(isinstance(msg, list) and msg[0] and msg[1]):
            key = "&&".join(set([sender,receiver]))
            self._single_message_dict[key].append(
                "\r\n".join([sender,"\r\n".join(msg)]))
            return True
        else:
            return False

    def saveGroupMsg(self, sender, group_id, msg):
        if isinstance(sender, unicode) and sender \
            and(isinstance(group_id, int) and group_id) \
            and(isinstance(msg, list) and msg[0] and msg[1]):
            self._group_message_dict[group_id].append(
                "\r\n".join([sender,"\r\n".join(msg)]))
            return True
        else:
            return False

    def savePicture(self, content, format):
        if content and (isinstance(format,str) and format):
            md5 = hashlib.md5()
            md5.update(content)
            pic_name = md5.hexdigest()
            path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                "data","picture",pic_name+format)
            if not os.path.exists(path):
                with open(path,"wb") as output:
                    output.write(content)
            return pic_name+format
        else:
            return False
