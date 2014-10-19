import os
import hashlib

def saveSingleMsg(sender, receiver, msg):
    if isinstance(sender, unicode) and sender \
        and(isinstance(receiver, unicode) and receiver) \
        and(isinstance(msg, unicode) and msg):
        return True
    else:
        return False

def saveGroupMsg(sender, group_id, msg):
    if isinstance(sender, unicode) and sender \
        and(isinstance(group_id, int) and group_id) \
        and(isinstance(msg, unicode) and msg):
        return True
    else:
        return False

def savePicture(content, format):
    if content and (isinstance(format,str) and format):
        md5 = hashlib.md5()
        md5.update(content)
        pic_name = md5.hexdigest()
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
            "Data","Picture",pic_name+format)
        if not os.path.exists(path):
            with open(path,"wb") as output:
                output.write(content)
        return (True, pic_name+format)
    else:
        return False
