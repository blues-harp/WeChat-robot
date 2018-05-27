#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import itchat  # 这是一个用于微信回复的库
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

KEY_FOR_YS = 'd8bbf2a4678d401a849e3a55e69797e8'
KEY = '126539e4ee8d4a2ab82f40aa9c939f84'


# 向api发送请求
def get_response(msg, key=KEY):
    api_url = 'http://www.tuling123.com/openapi/api'
    data = {

        'key': key,
        'info': msg,
        'userid': 'pth-robot',
    }
    try:
        r = requests.post(api_url, data=data).json()
        return r.get('text') + "\n" + u'(这是来自机器人的回复^_^)'.encode("utf-8")
    except:
        return


# 自动回复群消息
@itchat.msg_register(itchat.content.TEXT, isFriendChat=False, isGroupChat=True)
def turing_reply_for_group(msg):
    if is_auto_replay_for_group(msg):
        turing_response = get_response(msg['Text'], KEY)
        prefix = ''
        if msg.isAt:
            prefix = '@' + msg.ActualNickName + ' '
        return prefix + turing_response


# 自动回复个人消息
@itchat.msg_register(itchat.content.TEXT, isFriendChat=True, isGroupChat=False)
def turing_reply_for_friends(msg):
    key = KEY
    if msg.User.NickName.encode("utf-8") == '迷鹿' or msg.User.RemarkName.encode("utf-8") == '小应姗':
        key = KEY_FOR_YS
    turing_response = get_response(msg['Text'], key)
    return turing_response


# 是否自动回复该群消息
def is_auto_replay_for_group(msg):
    nickName = msg.User.NickName.encode("utf-8")
    if nickName == '十年' or nickName == "十年聚_联络" or nickName == "同学十年庆~策划部":
        return True
    else:
        return False


itchat.auto_login(enableCmdQR=True, hotReload=True)
itchat.run()
