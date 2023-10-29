from config import CONN, CURSOR


class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        try:
            sql = """
                    CREATE TABLE IF NOT EXISTS songs (
                        id INTEGER PRIMARY KEY, 
                        name TEXT, 
                        album TEXT
                )"""

            CURSOR.execute(sql)
        except:
            CURSOR.execute("""DROP TABLE IF EXISTS songs""")

    def save(self):

        sql = """
                INSERT INTO songs (name, album)
                VALUES (?, ?)
            """

        CURSOR.execute(sql, (self.name, self.album))

        self.id = CURSOR.execute(
            "SELECT last_insert_rowid() FROM songs").fetchone()[0]
        return self.id

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        song.save()
        return song

#our code that instantiates and saved some songs
# Song.create_table()
# song = Song("Hold On", "Born to Sing")
# song.save()
# print(song.id)

# song2 = Song("Hello", "25")
# song2.save()
# print(song2.id)
# print(song2.name)

song = Song.create("Hold On", "Born to Sing")
print(song.id)
song2 = Song.create("Hello", "25")
print(song2.id)

