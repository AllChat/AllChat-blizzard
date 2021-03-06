#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<alen-alex>
  Purpose: provide a message content retrieval interface to web server,
           retrieve from /data directory
  Created: 2014/11/4
"""

import os
import json
from encrypt import Encryptor

#----------------------------------------------------------------------
def getMessages(directory, start_date, end_date):
    """retrieve the messages stored in files
       param: directory: the place where files should be searched from;
       param: start_date: start date of files to retrieve, format by "yyyy-mm-dd";
       param: end_date: end date of files to retrieve, format by "yyyy-mm-dd";
    """
    try:
        start_year, start_month, start_day = start_date.split("-")
        end_year, end_month, end_day = end_date.split("-")
    except ValueError:
        return ("Wrong date format", 404)
    result = list()
    for year in os.listdir(directory):
        if year>=start_year and year<=end_year:
            for month in os.listdir(os.path.join(directory,year)):
                if month>=start_month and month<=end_month:
                    for file_ in os.listdir(os.path.join(directory,year,month)):
                        if file_.rstrip(".bin")>=start_day and \
                           file_.rstrip(".bin")<=end_day:
                            messages = _read_file(os.path.join(directory,year,
                                                               month,file_))
                            result.extend(messages)
    return json.JSONEncoder().encode(result)

#----------------------------------------------------------------------
def _read_file(file_path):
    """"""
    key = _get_encrypt_key()
    encryptor = Encryptor(key)
    messages = list()
    intra_line_sep = "\t\t"
    inter_line_sep = "\t\t\t\t"
    with open(file_path,"rb") as output:
        for segment in output:
            try:
                message = encryptor.DecryptStr(segment.rstrip(os.linesep))
                messages.extend([line.split(intra_line_sep)
                                 for line in message.split(inter_line_sep)])
            except:
                pass
    return messages

#----------------------------------------------------------------------
def _get_encrypt_key():
    """"""
    root = os.path.dirname(os.path.dirname(__file__))
    conf_path = os.path.join(root, "conf", "blizzard.conf")
    if not os.path.exists(conf_path):
        raise ValueError("Invalid config file path.")
    with open(conf_path,"rb") as conf:
        config_dict = dict(tuple(line.split(";")[0].split(" "))
                           for line in conf)
    return int(config_dict.get("encrypt_key"))
