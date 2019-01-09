# -*- coding: utf-8 -*-
import urllib2, urllib, xbmcaddon, xbmcgui, xbmcplugin, xbmc, re, sys, os, dandy
import xbmc,xbmcaddon,xbmcgui,xbmcplugin
from addon.common.addon import Addon

addon_id='plugin.video.watchcartoon_gw'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
addon_name = selfAddon.getAddonInfo('name')
ADDON      = xbmcaddon.Addon()
ADDON_PATH = ADDON.getAddonInfo('path')
ICON       = ADDON.getAddonInfo('icon')
FANART     = ADDON.getAddonInfo('fanart')
VERSION    = ADDON.getAddonInfo('version')
BASEURL    = 'https://www.watchcartoononline.io'
ART        = ADDON_PATH + "/resources/icons/"

def Main_menu():
    addDir('[B][COLOR orange]Latest 50 Releases[/COLOR][/B]',BASEURL + '/last-50-recent-release',10,ART + 'latest.jpg',FANART,'')
    addDir('[B][COLOR orange]Popular and Ongoing Series[/COLOR][/B]',BASEURL,8,ART + 'popular.jpg',FANART,'')
    addDir('[B][COLOR orange]Dubbed Anime List (Alpha)[/COLOR][/B]',BASEURL + '/dubbed-anime-list',5,ART + 'dubbed.jpg',FANART,'')
    addDir('[B][COLOR orange]Cartoons List (Alpha)[/COLOR][/B]',BASEURL + '/cartoon-list',5,ART + 'cartoons.jpg',FANART,'')
    addDir('[B][COLOR orange]Cartoon Favourites[/COLOR][/B]','https://raw.githubusercontent.com/dandy0850/iStream/master/test/cartoons_anime.txt',11,ART + 'cfav.jpg',FANART,'')
    addDir('[B][COLOR orange]Subbed Anime List (Alpha)[/COLOR][/B]',BASEURL + '/subbed-anime-list',5,ART + 'subbed.jpg',FANART,'')
    addDir('[B][COLOR orange]Search by Genre[/COLOR][/B]',BASEURL + '/search-by-genre',7,ART + 'genre.jpg',FANART,'')
    addDir('[B][COLOR orange]Search[/COLOR][/B]','',4,ART + 'search.jpg',FANART,'')
    addDir('[B][COLOR orange]Ova Series Episodes List (Alpha)[/COLOR][/B]',BASEURL + '/ova-list',6,ART + 'ova.jpg',FANART,'')
    addDir('[B][COLOR orange]Movies (Alpha)[/COLOR][/B]',BASEURL + '/movie-list',6,ART + 'movies.jpg',FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def search(url):
    dirs1 = ['/dubbed-anime-list', '/cartoon-list', '/subbed-anime-list']
    dirs2 = ['/ova-list', '/movie-list']
    if url != None and url != "": search = url
    else: 
        keyb = xbmc.Keyboard('', 'Search for')
        keyb.doModal()
        if keyb.isConfirmed() != None and keyb.isConfirmed() != "": search = keyb.getText()
        else: return
    for dir in dirs1:
        OPEN = Open_Url(BASEURL + dir)
        Regex = re.compile('<div class="ddmcc">(.+?)</td>',re.DOTALL).findall(OPEN)
        Regex2 = re.compile('<li><a href="(.+?)".+?>(.+?)</a></li>',re.DOTALL).findall(str(Regex))
        for url,name in Regex2:
            name = name.replace('&#8216;','\'').replace('&#8217;','\'').replace('&#8211;','-').replace('&#039;','\'').replace('&amp;','&').replace('\\xc3\\xa9','e').replace('\\','').replace('xc3xa4','a').replace('Pxc3xa2tissixc3xa8re','Patissiere').replace('xc3xa','i').replace('xe2x80x93','-').replace(' :',':').replace('xc3xb8','o').replace('xe2x80xa0',' ').replace('xc2xbd','½').replace("`","'").replace("xe2x80x99","'").replace('xc3x9f','ss').replace('xc2xb2','²').replace('xc3x97','x').replace('xc3xb1','ñ')
            if str(search.lower()) in str(name.lower()): addDir(name, url, 20, iconimage, FANART, '')
    for dir in dirs2:
        OPEN = Open_Url(BASEURL + dir)
        Regex = re.compile('<div class="ddmcc">(.+?)</td>',re.DOTALL).findall(OPEN)
        Regex2 = re.compile('<a href="(.+?)" title="(.+?)"',re.DOTALL).findall(str(Regex))
        for url,name in Regex2:
            name = name.replace('&#8216;','\'').replace('&#8217;','\'').replace('&#8211;','-').replace('#038;','').replace('&#039;','\'').replace('&amp;','&').replace('\\xc3\\xa9','e').replace('\\','').replace('English Dubbed','[COLOR blue](English Dubbed)[/COLOR]').replace('English Subbed','[COLOR red](English Subbed)[/COLOR]').replace('xe2x80x99','\'').replace('xe2x80x93','-').replace('&#215;','x').replace('&#8221;','"')
            addDir(name, url, 100, ICON, FANART, '')

def all_list(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<div class="ddmcc">(.+?)</td>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('<li><a href="(.+?)".+?>(.+?)</a></li>',re.DOTALL).findall(str(Regex))
    for url,name in Regex2:
        name = name.replace('&#8216;','\'').replace('&#8217;','\'').replace('&#8211;','-').replace('&#039;','\'').replace('&amp;','&').replace('\\xc3\\xa9','e').replace('\\','').replace('xc3xa4','a').replace('Pxc3xa2tissixc3xa8re','Patissiere').replace('xc3xa','i').replace('xe2x80x93','-').replace(' :',':').replace('xc3xb8','o').replace('xe2x80xa0',' ').replace('xc2xbd','½').replace("`","'").replace("xe2x80x99","'").replace('xc3x9f','ss').replace('xc2xb2','²').replace('xc3x97','x').replace('xc3xb1','ñ')
        name = name.replace('English Dubbed','[COLOR blue](English Dubbed)[/COLOR]').replace('English Subbed','[COLOR red](English Subbed)[/COLOR]')
        addDir(name,url,20,iconimage,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def cart_fav(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<title>(.+?)</title>.+?url>(.+?)</url>.+?thumb>(.+?)</thumb>.+?art>(.+?)</art>',re.DOTALL).findall(OPEN)
    for name,url,icon,fanart in Regex:
        name = name.replace("`","'")
        addDir(name,url,20,icon,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')    

def genre(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<!-- search-by-genre -->(.+?)</div></div></div></div>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('<li><a href="(.+?)">(.+?)</a></li>',re.DOTALL).findall(str(Regex))
    for url,name in Regex2:
        name = name.replace('\\','')
        addDir('[B][COLOR orange]%s[/COLOR][/B]' %name,url,9,ART + 'search.jpg',FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def genre_list(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<div class="ddmcc">(.+?)</td>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('<li><a href="(.+?)">(.+?)</a></li>',re.DOTALL).findall(str(Regex))
    for url,name in Regex2:
        name = name.replace('&#8216;','\'').replace('&#8211;','-').replace('&#039;','\'').replace('&amp;','&').replace('\\xc3\\xa9','e').replace('\\','')
        addDir(name,url,20,ART + 'search.jpg',FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def ova_list(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<div class="ddmcc">(.+?)</td>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('href="(.+?)">(.+?)</a>',re.DOTALL).findall(str(Regex))
    for url,name in Regex2:
        name = name.replace('&#8216;','\'').replace('&#8217;','\'').replace('&#8211;','-').replace('#038;','').replace('&#039;','\'').replace('&amp;','&').replace('\\xc3\\xa9','e').replace('\\','').replace('English Dubbed','[COLOR blue](English Dubbed)[/COLOR]').replace('English Subbed','[COLOR red](English Subbed)[/COLOR]').replace('xe2x80x99','\'').replace('xe2x80x93','-').replace('&#215;','x').replace('&#8221;','"')
        addDir(name,url,100,ICON,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def Get_episodes_top50(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<div class="menulaststyle">(.+?)</ul>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('<li><a href="(.+?)".+?>(.+?)</a></li>',re.DOTALL).findall(str(Regex))
    for url,name in Regex2:
        name = name.replace('&#8217;','\'').replace('&#8211;','-').replace('&#039;','\'').replace('&amp;#038;','&').replace('\\xc3\\xa9','e')
        name = name.replace('English Dubbed','[COLOR blue](English Dubbed)[/COLOR]').replace('English Subbed','[COLOR red](English Subbed)[/COLOR]')
        addDir(name,url,100,ART + 'latest.jpg',FANART,name)
    xbmc.executebuiltin('Container.SetViewMode(50)')

def Get_popular(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<div class="menustyle">.+?<div class="menustyle">(.+?)</ul>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('<li><a href="(.+?)".+?>(.+?)</a></li>',re.DOTALL).findall(str(Regex))
    for url,name in Regex2:
        name = name.replace('&#8217;','\'').replace('&#8211;','-').replace('&#039;','\'').replace('&amp;#038;','&').replace('\\xc3\\xa9','e').replace('\\','').replace('&amp;','&').replace('xc3x97','x').replace('xe2x80x99','\'')
        name = name.replace('English Dubbed','[COLOR blue](English Dubbed)[/COLOR]').replace('English Subbed','[COLOR red](English Subbed)[/COLOR]')
        addDir(name,url,20,ART + 'popular.jpg',FANART,name)
    xbmc.executebuiltin('Container.SetViewMode(50)')

def Get_show_episodes(url,name):
    bollox = name
    OPEN = Open_Url(url)
    Regex = re.compile('class="cat-listview cat-listbsize">(.+?)</ul>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('<a href="(.+?)".+?title="(.+?)"',re.DOTALL).findall(str(Regex))
    Regex2 = list(reversed(Regex2))
    for url,name in Regex2:
        name = name.replace('&amp','&').replace('&#8217;','\'').replace('&#8211;','-').replace('&#039;','\'').replace('#038;','').replace('\\xc3\\xa9','e').replace('&#8230;','....').replace('\\xe2\\x80\\x99','\'').replace('\\xe2\\x80\\x93','').replace(': Episode ','Episode ')
        name = name.replace('English Dubbed','[COLOR blue](English Dubbed)[/COLOR]').replace('English Subbed','[COLOR red](English Subbed)[/COLOR]').replace('Watch ','',1)
        icon = re.compile('<meta property="og:image" content="(.+?)"',re.DOTALL).findall(OPEN)[0]
        if 'Season'in name:
            name = name.replace('Season ','').replace(' Episode ','x')
        #name = name.replace(bollox,'')
        addDir('[B][COLOR orange]%s[/COLOR][/B]' %name,url,100,icon,icon,name)
    xbmc.executebuiltin('Container.SetViewMode(50)')

########################################

def Open_Url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def addDir(name,url,mode,iconimage,fanart,description):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={"Title": name,"Plot":description})
	liz.setProperty('fanart_image', fanart)
	if mode==100:
		liz.setProperty("IsPlayable","true")
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	else:
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok


def resolve(name,url,iconimage,description):
    res_quality = []
    stream_url = []
    quality = ''
    OPEN = Open_Url(url)
    if 'spongebob-squarepants' in url:
        #print 'OPEN page'+OPEN
        try:
            match = re.compile('<iframe id="frameNew.+?" src="(.+?)"').findall(OPEN)
            for link in match:
                #label=link
                label = urllib.unquote(link).decode()
                label = label.split('file=')[1].split('.flv')[0]
                if 'Spongebob.squarepants.' in label:
                    label = label.split('Spongebob.squarepants.')[1].replace('.',' ').title()                
                else:
                    try:
                        label = label.split('- ')[2]
                    except:
                        label= label.split('- ')[1]
                                   
                quality = '[B][COLOR white]%s[/COLOR][/B]' %label
                res_quality.append(quality)
                stream_url.append(link)
            if len(match) >1:
                    dialog = xbmcgui.Dialog()
                    ret = dialog.select('Please Select Episode',res_quality)
                    if ret == -1:
                        return
                    elif ret > -1:
                            request_url = stream_url[ret]
            else:
                request_url = re.compile('iframe id="frameNew.+?" src="(.+?)"').findall(OPEN)[0]
    
        except:
            xbmc.executebuiltin("XBMC.Notification([COLOR cornflowerblue]Sorry[/COLOR],[COLOR cornflowerblue]Link Unavailable[/COLOR] ,2000)")           
    else:
        request_url = re.compile('<iframe id="frameNew.+?" src="(.+?)"').findall(OPEN)[0]
    
    request_url = request_url.replace('cartoon/embed.php','cartoon/embed-jw7.php')
    link2 = Open_Url(request_url)
    try:
            url = re.compile('file: "(.*?)"').findall(link2)[1]
            liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
            liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
            liz.setProperty("IsPlayable","true")
            liz.setPath(url)
            xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
    except:
            url = re.compile('file: "(.*?)"').findall(link2)[0]
            liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
            liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
            liz.setProperty("IsPlayable","true")
            liz.setPath(url)
            xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2: 
        params=sys.argv[2] 
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
            params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}    
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]
    return param

params      = get_params()
url         = None
name        = None
iconimage   = None
mode        = None
fanart      = None
description = None

try:    url         = urllib.unquote_plus(params["url"])
except: pass
try:    name        = urllib.unquote_plus(params["name"])
except: pass
try:    iconimage   = urllib.unquote_plus(params["iconimage"])
except: pass
try:    mode        = int(params["mode"])
except: pass
try:    fanart      = urllib.unquote_plus(params["fanart"])
except: pass
try:    description = urllib.unquote_plus(params["description"])
except: pass

#print str(PATH)+ ": " + str(VERSION)
print "Mode: "        + str(mode)
print "URL: "         + str(url)
print "Name: "        + str(name)
print "IconImage: "   + str(iconimage)

print ADDON.getAddonInfo('path') + ": " + ADDON.getAddonInfo('version')

#########################################################

if   mode == None : Main_menu()
elif mode == 4    : search(url)
elif mode == 5    : all_list(url)
elif mode == 6    : ova_list(url)
elif mode == 7    : genre(url)
elif mode == 8    : Get_popular(url)
elif mode == 9    : genre_list(url)
elif mode == 10   : Get_episodes_top50(url)
elif mode == 11   : cart_fav(url)
elif mode == 20   : Get_show_episodes(url,name)
elif mode == 100  : resolve(name,url,iconimage,description)

xbmcplugin.endOfDirectory(int(sys.argv[1]))