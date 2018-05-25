# coding:utf-8

import itchat


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text


itchat.auto_login(enableCmdQR=True)
itchat.run()

# ret = itchat.get_friends()
#
#
# for item in ret:
#     if item.RemarkName == "小应姗":
#         itchat.send_msg("this is from program.", item.UserName)
# print(item.UserName+"="+item.RemarkName)


# sendResult = i
# print(sendResult)
