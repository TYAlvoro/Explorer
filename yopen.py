from youtubesearchpython import VideosSearch
import webbrowser


def search_in_youtube(searching):
    videosSearch = VideosSearch(searching, limit = 2)
    link = videosSearch.result()['result'][1]['link']
    webbrowser.open(link)