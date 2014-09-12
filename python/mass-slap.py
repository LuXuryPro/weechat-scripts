#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This is mass-slap script for weechat. Very usefull for anoye everyone on channel ;-)
#

import weechat as w

w.register("mass-slap","","","","Slaps (highlights) everyone on current channel","","")

def get_nicklist():
    #this function is particulary taked from hl_nicks.py script maden by nesthib.
    #I think that it can be writen more cleary for this special situation, but anyway it works properly so i use it.
    nicklist = []
    infolist_nicklist = w.infolist_get('nicklist', w.current_buffer(), '')
    while w.infolist_next(infolist_nicklist):
        nick = w.infolist_string(infolist_nicklist, 'name')
        prefix = w.infolist_string(infolist_nicklist, 'prefix') #This can be ersed but in future someone may need this.
        nick_type = w.infolist_string(infolist_nicklist, 'type')
        if nick_type != 'nick': # just for sure :)
            pass
        else:
            if not nick in nicklist:
                nicklist.append(nick)
    w.infolist_free(infolist_nicklist)
    return nicklist

def slap_all(data, buffer, args):
    nicks = get_nicklist()
    if len(nicks)>50:
        w.prnt("","Too much nicks on channel: "+str(len(nicks))+" Be carefull :)")
    else:
        nicks.sort(key=str.lower) #sort table
        string = ' '.join(str(n) for n in nicks) #create string from table
        #w.prnt("",string) #for testing
        #w.prnt("",str(len(nicks))) #for testing
        w.command(w.current_buffer(),"/me slaps: "+string) #put on channel
        return w.WEECHAT_RC_OK

hook = w.hook_command("mass-slap", "","","","","slap_all", "")
