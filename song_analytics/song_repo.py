

class SongRepo:
    def __init__(self):
        self.songs = []

    def add_song(self, name):
        self.songs.append((name, set()))
        return len(self.songs)

    def check_if_id_exists(self, song_id):
        if song_id <= 0 or song_id > len(self.songs):
            print(f'Error: Song ID {song_id} does not exist.')
            return False
        return True

    def update_user_count(self, song_id, user_id):
        if not self.check_if_id_exists(song_id):
            return None
        new_user = False
        user_set = self.songs[song_id - 1][1]
        if user_id not in user_set:
            new_user = True
            user_set.insert(user_id)
        return new_user, len(user_set)

