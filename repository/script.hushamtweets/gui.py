
import random, threading
import xbmc, xbmcaddon, xbmcvfs, xbmcgui

# Plugin Info
ADDON_ID       = 'script.hushamtweets'
REAL_SETTINGS  = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME     = REAL_SETTINGS.getAddonInfo('name')
ADDON_VERSION  = REAL_SETTINGS.getAddonInfo('version')
ADDON_PATH     = (REAL_SETTINGS.getAddonInfo('path').decode('utf-8'))
SETTINGS_LOC   = REAL_SETTINGS.getAddonInfo('profile').decode('utf-8')
                                                                         
## GLOBALS ##
CLOSE_TIME     = [2,5,10,15,30,60,120][int(REAL_SETTINGS.getSetting('Close_Time'))]
ID_LIST        = [30100,30200,30300]
IMG_LIST       = {30101:'HushamTweet_%d.png'  %random.randint(1,4),
                  30201:'HushamTweet_%d.png' %random.randint(1,5),
                  30301:'HushamTweet_%d.png'%random.randint(1,7)}

class GUI(xbmcgui.WindowXMLDialog):
    def __init__(self, *args, **kwargs ):
        self.lockAction = False
        self.closeTimer = threading.Timer(CLOSE_TIME, self.close)
        
        
    def log(self, msg, level=xbmc.LOGDEBUG):
        xbmc.log(ADDON_ID + '-' + ADDON_VERSION + '-' + msg, level)
            
            
    def onInit(self):
        random.seed()
        self.lockAction = True
        select = random.choice(ID_LIST)
        for id in ID_LIST: 
            if id != select: self.getControl(id).setVisible(False)
        self.getControl(select + 1).setImage(IMG_LIST[select + 1])
        xpos, ypos = self.getControl(select).getPosition()
        width = self.getControl(select + 1).getWidth()
        xmin = 0 + int(width)
        xmax = 1920 - int(width)
        self.getControl(select).setPosition(random.randrange(xmin,xmax,int(width//4)), ypos)
        self.getControl(select).setVisible(True)
        xbmc.sleep(1500)
        self.lockAction = False
        self.closeTimer.start()

        
    def onAction(self, action):
        if self.lockAction == False: self.close()