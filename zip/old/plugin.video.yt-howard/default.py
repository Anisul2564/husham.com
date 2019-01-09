# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Howard Stern on YouTube by Husham Memar
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: Husham Memar
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.yt-howard'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "HOWARDTV"
YOUTUBE_CHANNEL_ID_2 = "PLd1ToAF2Reddoadnwd_-e48YNHRyBrz_p"
YOUTUBE_CHANNEL_ID_3 = "UCbr8JR7gx9V7oZZLo1Xnudg"
YOUTUBE_CHANNEL_ID_4 = "PLuqtdlJ-HdqOXJTQ5TYeKZjMEuCYs-0N9"
YOUTUBE_CHANNEL_ID_5 = "PLa38GwaswYLsBbzYI89OXf9RXPbwux_am"
YOUTUBE_CHANNEL_ID_6 = "PLWnEBus36NdmhV1TniMG505a6fAd6hoNR"
YOUTUBE_CHANNEL_ID_7 = "UCl3rwBZFUP9RnP_rrPoFxOA"

# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))



    plugintools.add_item( 
        #action="", 
        title="The Howard Stern Show",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-lEHROTyGJmU/AAAAAAAAAAI/AAAAAAAAAAA/n3XGG9b_I1g/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The World Of Howard Stern",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-F0CehKkDPrM/AAAAAAAAAAI/AAAAAAAAAAA/AyuVrb0yjCc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

  
    plugintools.add_item( 
        #action="", 
        title="The World Of Howard Stern",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-3sasfRJzKqM/AAAAAAAAAAI/AAAAAAAAAAA/COLF-QtOyk8/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )  

 
    plugintools.add_item( 
        #action="", 
        title="Popular Videos – Howard Stern & Artie Lange",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://i.ytimg.com/vi/nubkPRm8E18/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLDxzdyPr35qwyQxEARJ8LK4V5KfSg",
        folder=True )

 
    plugintools.add_item( 
        #action="", 
        title="Howard Stern Prank Calls",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://i.ytimg.com/vi/3olJlPBJDIs/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLC5Z-Nz-jDDCEFOZnqINsrsVWXK2A",
        folder=True )
		
plugintools.add_item( 
        #action="", 
        title="Howard Stern Best Of",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://i.ytimg.com/vi/6-PSjutg7LI/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLD8_yeJKzgWgHCOXhD3rJjOT6h-rA",
        folder=True )

  
plugintools.add_item( 
        #action="", 
        title="The World Of Howard Stern",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-3sasfRJzKqM/AAAAAAAAAAI/AAAAAAAAAAA/COLF-QtOyk8/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )  
		
   
		
   
run()
