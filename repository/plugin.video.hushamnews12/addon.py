#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from xbmcswift2 import Plugin


STRINGS = {
    'page': 30001,
    'streams': 30100,
    'streams2': 30101,
	

}

STATIC_STREAMS = (
    {
        'title': 'News 12 Long Island',
        'logo': 'news12.jpg',
        'stream_url': ('http://hls.iptv.optimum.net/news12/nipadlive/index_new.m3u8?callsign=N12LI_WEST'),
    },
	{
        'title': 'News 12 Bronx',
        'logo': 'news12.jpg',
        'stream_url': ('http://hls.iptv.optimum.net/news12/nipadlive/index_new.m3u8?callsign=N12BX'),
    },
	{
        'title': 'News 12 Connecticut',
        'logo': 'news12.jpg',
        'stream_url': ('http://hls.iptv.optimum.net/news12/nipadlive/index_new.m3u8?callsign=N12CT_WEST'),
    },
	{
        'title': 'News 12 Hudson Valley',
        'logo': 'news12.jpg',
        'stream_url': ('http://hls.iptv.optimum.net/news12/nipadlive/index_new.m3u8?callsign=N12HV'),
    },
	{
        'title': 'NEWS 12 NEW JERSEY',
        'logo': 'news12.jpg',
        'stream_url': ('http://hls.iptv.optimum.net/news12/nipadlive/index_new.m3u8?callsign=N12NJ_CENTRAL'),
    },
	{
        'title': 'News 12 Westchester',
        'logo': 'news12.jpg',
        'stream_url': ('http://hls.iptv.optimum.net/news12/nipadlive/index_new.m3u8?callsign=N12WH_WESTCHESTER'),
    },
	{
        'title': 'News 12 Brooklyn',
        'logo': 'news12.jpg',
        'stream_url': ('http://hls.iptv.optimum.net/news12/nipadlive/index_new.m3u8?callsign=N12KN'),
    },
)


STATIC_STREAMS2 = (
    {
        'title': 'Events IPTV Only Links',
        'logo': 'Hushamallsports.jpg',
        'stream_url': ('https://raw.githubusercontent.com/hmemar/husham.com/master/'
                       'Lists/event.m3u'),
    },
)


YOUTUBE_CHANNELS = (
    {
        'name': 'WXII 12 NEWS',
        'logo': 'news12.jpg',
        'channel_id': 'UC0ZsHHC_frpcqneDpMiteCQ',
        'user': 'hmemar22',
    }, 
	{
        'name': 'WDEF News 12',
        'logo': 'news12.jpg',
        'channel_id': 'UCMp6dYTbPOrKFHMH6rGcp2g',
        'user': 'hmemar22',
    }, 
	{
        'name': 'twelvedottv',
        'logo': 'news12.jpg',
        'channel_id': 'UC_DlTqJhRV-OafjHESJciNw',
        'user': 'hmemar22',
    }, 
	{
        'name': 'CNN',
        'logo': 'news12.jpg',
        'channel_id': 'UCupvZG-5ko_eiXAupbDfxWw',
        'user': 'hmemar22',
    }, 
	{
        'name': 'CNN Live',
        'logo': 'news12.jpg',
        'channel_id': 'UCRrW0ddrbFnJCbyZqHHv4KQ',
        'user': 'hmemar22',
    }, 
	{
        'name': 'euronews (in English)',
        'logo': 'news12.jpg',
        'channel_id': 'UCSrZ3UV4jOidv8ppoVuvW9Q',
        'user': 'hmemar22',
    },  
)



YOUTUBE_URL ='plugin://plugin.video.youtube/channel/%s/?page=1'

plugin = Plugin()


@plugin.route('/')
def show_root_menu():
    items = [
        {'label': _('streams'),
         'path': plugin.url_for('show_streams')},
		 {'label': _('Videos'),
         'path': plugin.url_for('show_channels')},

    ]
    return plugin.finish(items)


@plugin.route('/streams/')
def show_streams():
    items = [{
        'label': stream['title'],
        'thumbnail': get_logo(stream['logo']),
        'path': stream['stream_url'],
        'is_playable': True,
    } for stream in STATIC_STREAMS]
    return plugin.finish(items)

	
	

@plugin.route('/channels/')
def show_channels():
    items = [{
        'label': channel['name'],
        'thumbnail': get_logo(channel['logo']),
        'path': YOUTUBE_URL % channel['channel_id'],
    } for channel in YOUTUBE_CHANNELS]
    return plugin.finish(items)

def get_logo(logo):
    addon_id = plugin._addon.getAddonInfo('id')
    return 'special://home/addons/%s/resources/media/%s' % (addon_id, logo)


def _(string_id):
    if string_id in STRINGS:
        return plugin.get_string(STRINGS[string_id])
    else:
        plugin.log.warning('String is missing: %s' % string_id)
        return string_id


def log(text):
    plugin.log.info(text)

if __name__ == '__main__':
    plugin.run()
