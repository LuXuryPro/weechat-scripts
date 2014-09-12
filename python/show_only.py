#!/usr/bin/env python
# -*- coding: utf-8 -*-

import weechat as w

w.register("show-only","","","","Shows messages only from one nick in current buffer","","")

filters = []

def show_only(data, buffer, args):
    if not args:
        return show_all(data, buffer, args)
    nick = args
    filters.append(nick)
    bname = w.buffer_get_string(buffer, "full_name")
    command = "/filter add " + nick + " " + bname + " * " + "!"+nick+"\\t"
    w.prnt("",command)
    w.command("",command)
    return w.WEECHAT_RC_OK

def show_all(data, buffer, args):
    if not filters:
        return w.WEECHAT_RC_OK
    nick = filters.pop()
    bname = w.buffer_get_string(buffer, "full_name")
    command = "/filter del " + nick
    w.prnt("",command)
    w.command("",command)
    return w.WEECHAT_RC_OK

w.hook_command("show_only","","","","","show_only", "")
w.hook_command("show_all","","","","","show_all", "")
