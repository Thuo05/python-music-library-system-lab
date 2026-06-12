class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artists_count()

    def add_song_to_count(self):
        type(self).count += 1

    def add_to_genres(self):
        if self.genre not in type(self).genres:
            type(self).genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in type(self).artists:
            type(self).artists.append(self.artist)

    def add_to_genre_count(self):
        cls = type(self)
        cls.genre_count[self.genre] = cls.genre_count.get(self.genre, 0) + 1

    def add_to_artists_count(self):
        cls = type(self)
        cls.artist_count[self.artist] = cls.artist_count.get(self.artist, 0) + 1
        cls.artists_count = cls.artist_count
