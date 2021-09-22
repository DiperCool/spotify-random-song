import spotipy
import telebot
import random
import logging
from spotipy.oauth2 import SpotifyClientCredentials
SPOTIPY_CLIENT_ID='0893cd74f2c04be7943175ae4e22b324'
SPOTIPY_CLIENT_SECRET='3b04df03d96844f0b3baa1d437208c5e'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET))
bot = telebot.TeleBot("2049038003:AAEjwRQbhuiWrb6uDxjlRCcDpwaoJh0f8jI")
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) 

def has_list_item(list, item_search):
    for item in list:
        if item["name"].lower() == item_search["name"].lower():
            return True
    return False
def has_string_keyword(keywods, item_search):
    for keyword in keywods:
        if keyword in item_search["name"].lower():
            return True
    return False
def delete_duplicates(list):
    filtered = []
   
    for item in list:
        if not has_list_item(filtered, item):
            filtered.append(item)
    return filtered
def delete_by_keyword(list_keywords, list):
    filtered= []
    for item in list:
        if not has_string_keyword(list_keywords, item):
            filtered.append(item)
    return filtered

ids = ["5HFkc3t0HYETL4JeEbDB1v", "05fG473iIaoy82BF1aGhL8","0GDGKpJFhVpcjIGF8N6Ewt","2ye2Wgw4gimLv2eAKyk1NB"]
birdy_uri = 'spotify:artist:'+random.choice(ids)
keywords = ["live", "new version", "feat", "orchestral version","intro","exclusive", "bonus","rerecorded","edition", "remastered"]
results = spotify.artist_albums(birdy_uri, album_type='album', limit=50)
albums = delete_by_keyword(keywords,delete_duplicates(results["items"]))
tracks = []
for album in albums:
    results_tracks = spotify.album_tracks(album["id"])["items"]


    for track in results_tracks:
        tracks.append(track)
tracks= delete_by_keyword(keywords,delete_duplicates(tracks))

choosed_track = random.choice(tracks)
artist = choosed_track["artists"][0]["name"]
link = choosed_track["external_urls"]["spotify"]
bot.send_message(580414584, 'Your song today is "'+choosed_track["name"]+'" from '+artist)
bot.send_message(580414584, link)
bot.send_message(580414584, "Please don't forget to listen and translate the song")