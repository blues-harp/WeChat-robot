# -*- coding: utf-8 -*-
import itchat


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print(msg.text)
    return "this is from robot: " + msg.text


# itchat.auto_login(enableCmdQR=2)
itchat.auto_login()
ret = itchat.search_chatrooms(u"十年")
ret2 = itchat.update_chatroom(ret[0].UserName)
for item in ret2.MemberList:
    print(item.NickName + "=" + item.DisplayName)



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
