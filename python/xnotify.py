# -*- coding: utf-8 -*-

import weechat
import os

weechat.register("xnotify", "", "0.0.5", "GPL", "xmessage notification system for weechat", "", "")
weechat.hook_print("", "irc_privmsg", "", 1, "notify_show", "")

command = "xmessage -center -buttons OK:0 -default OK "


def is_displayed(buffer):
    dp = weechat.buffer_get_integer(buffer, 'num_displayed')
    #weechat.prnt(weechat.current_buffer(),"\ndp: "+str(dp))
    if dp != 0:
        return not inactive()
    return False


def inactive():
    inactivity = int(weechat.info_get('inactivity', ''))
    #weechat.prnt(weechat.current_buffer(),"\nIn: "+str(inactivity))
    if inactivity > 20:
        return True
    else:
        return False


def notify_show(data, bufferp, uber_empty, tagsn, isdisplayed, ishilight, prefix, message):
    l = tagsn.split(",")
    if ishilight == "1" or "notify_private" in l and not is_displayed(bufferp):
        nick = prefix[1:]
        os.system(command + nick+ ": " + message + "&")
    weechat.prnt(weechat.current_buffer(),data + "\n" + bufferp + "\n" + uber_empty + "\n" + tagsn + "\n" + isdisplayed + "\n" + ishilight + "\n" + prefix + "\n" + message  + "\n")
    return weechat.WEECHAT_RC_OK

