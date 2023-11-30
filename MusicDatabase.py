from warnings import warn
FILE_TO_SONG = ''

class Song:
    def __init__(self,name:str,id:int,artists:tuple[str],album:str):
        self.name = name
        self.artists:tuple[str] = artists
        self.album = album
        self.id = id

    def __repr__(self):
        s = f'Song({self.name}, '
        for a in self.artists:
            s += a + '|'
        s = s[:-1]
        return s+")"

class Playlist:
    def __init__(self,name:str,songs:list[Song]):
        self.name = name
        self.songs = songs

    def __repr__(self):
        s = f'Playlist({self.name}:'
        for a in self.songs:
            s += " "+a.name + ' |'
        s = s[:-1]
        return s+")"

class Database:
    def __init__(self):
        self.songs = []
        self.playlists = []

    def loadFromFiles(self):
        from os import walk
        from os.path import dirname
        from json import load
        MUSIC_PATH = dirname(__file__) + "\\__Music"
        key = load(open(MUSIC_PATH+"\\key.json"))
        print(key)
        _,_,files = next(walk(MUSIC_PATH))
        songs:list[Song|None] = []
        for fileName in filter(lambda x: x.endswith(('ogg','mp3','wav')),files):
            fileName = fileName.strip('.ogg')
            #these file names are actually id's which correspond with the index in <key> for their attributes
            index = int(fileName)
            print(index)
            songData = key[index]
            song = Song(songData['name'],index,songData['artists'],songData['album'])
            while index > len(songs):
                songs.append(None)
            if index == len(songs):
                songs.append(song)
            else:
                songs[index] = song
        self.songs = [s for s in songs if s is not None]
        if len(self.songs) != len(songs):
            raise SystemError("Ther was an erroer WAAAA!! BOOHOO")

    def loadPlaylists(self):
        from os import walk
        from os.path import dirname
        from json import load
        PLAYLIST_PATH = dirname(__file__) + "\\__Playlists"
        _,_,files = next(walk(PLAYLIST_PATH))
        playlists = []
        for file in files:
            songs = [self.songs[i] for i in load(open(PLAYLIST_PATH+"\\"+file,'r'))]
            pl = Playlist(file.strip('.json'),songs)
            playlists.append(pl)
        self.playlists = playlists
        
    def addSongToDatabase(self,artist:str,album:str,songName:str):
        pass

    def getSong(self,artist:str,album:str,songName:str) -> Song: #type: ignore
        pass
        warn(f"Artist: {artist}, Album: {album}, Song:{songName} was not found!")

    def getAllSongNames(self):
        return [song.name for song in self.songs]   

if __name__ == '__main__':

    db = Database()
    db.loadFromFiles()
    db.loadPlaylists()
    import pygame
    pygame.init()
    pygame.mixer.init()
    from os.path import dirname

    print(db.songs)
    print()
    print()
    print()
    print(db.playlists)
    while 1:
        pygame.mixer.music.load(dirname(__file__) + "\\__Music\\"+str(db.songs[int(input('SongName???'))].id) + '.ogg')
        pygame.mixer.music.play()