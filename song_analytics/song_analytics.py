# started at 10:07 PM
from bintrees import RBTree
from song_repo import SongRepo

class SongAnalytics:
    def __init__(self):
        self.song_repo = SongRepo()
        self.songs_ordered = RBTree() # key = num unique views, value = song ID

    def add_song(self, name):
        return self.song_repo.add_song(name)

    def play_song(self, song_id, user_id):
        if not self.song_repo.check_if_id_exists(song_id):
           return False
        new_user, count = self.song_repo.update_user_count(song_id, user_id)
        self.songs_ordered[]


    def print_analytics(self):




