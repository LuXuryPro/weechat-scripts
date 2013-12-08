#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 by the_godfather
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# This is mass-slap script for weechat. Very usefull for anoye everyone on channel ;-)
#

import weechat as w

w.register("mass-slap","antiquo","1.0","GPL3","Slaps (highlights) everyone on current channel","","")

def get_nicklist():
    #this function is particulary taked from hl_nicks.py script maden by nesthib.
    #I think that it can be writen more cleary for this special situation, but anyway it works properly so i use it.
    nicklist = {}
    infolist_nicklist = w.infolist_get('nicklist', w.current_buffer(), '')
    while w.infolist_next(infolist_nicklist):
        nick = w.infolist_string(infolist_nicklist, 'name')
        prefix = w.infolist_string(infolist_nicklist, 'prefix') #This can be ersed but in future someone may need this.
        nick_type = w.infolist_string(infolist_nicklist, 'type')
        if nick_type != 'nick': # just for sure :)
            pass
        else:
            if not nicklist.has_key(nick):
                nicklist[nick]=[]
            nicklist[nick].append(nick)
    w.infolist_free(infolist_nicklist)
    return nicklist

def slap_all(data, buffer, args):
    nicklist = get_nicklist()
    nicks = []
    for nick in nicklist:
        nicks.append(nick)
    if len(nicks)>50:
        w.prnt("","Too much nicks on channel: "+str(len(nicks))+" Be carefull :)")
    else:
        nicks.sort(key=str.lower) #sort table
        string = ' '.join(str(n) for n in nicks) #create string from table
        #w.prnt("",string) #for testing
        #w.prnt("",str(len(nicks))) #for testing
        w.command(w.current_buffer(),"/me slaps: "+string) #put on channel
        return w.WEECHAT_RC_OK

hook = w.hook_command("mass-slap", "","","","""""""""""","slap_all", "")
