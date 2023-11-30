import pygame
from MusicDatabase import Database, Playlist, Song
from collections import deque
from os.path import dirname
from json import load, dump
from utils import MUSIC_PATH
database = Database()
database.loadFromFiles()
database.loadPlaylists()

class MusicQueue:
    played:deque[Song] = deque()
    current:Song|None = None
    queued:deque[Song] = deque()

    repeat_level = 0

    loadedPlaylist:Playlist|None
    """Level of repeat\n
    0 =  No repeat\n
    1 = Repeat playlist when done\n
    2 = Repeat song when song done
    """
    
    @classmethod
    def nextSong(cls) -> Song|None:
        '''Returns the next song to play, it could be the same one currently playing. if return
        None then no song should be played'''
        if cls.current is None:
            return cls.current
        
        if cls.repeat_level == 0:
            if cls.queued:
                cls.played.append(cls.current)
                cls.current = cls.queued.popleft()
            else:
                cls.current = None 
        elif cls.repeat_level == 1:
            if cls.queued:
                cls.played.append(cls.current)
                cls.current = cls.queued.popleft()
            else:
                cls.played.append(cls.current)
                cls.queued.extend(cls.played)
                cls.played.clear()
                cls.current = cls.queued.popleft()
        elif cls.repeat_level == 3:
            pass
        return cls.current

    @classmethod
    def loadPlaylist(cls,playlist:Playlist):
        cls.loadedPlaylist = playlist
        cls.queued.clear()
        cls.queued.extend(playlist.songs)

    @classmethod
    def standalonePlaySong(cls,song:Song):
        cls.loadedPlaylist = None
        cls.queued.clear()
        cls.current = song
        cls.played.clear()


class MusicPlayer:
    songLoaded:bool = False
    volume:float = 0.0
    paused:bool = False
    music_position:float = 0.0
    songQueue = MusicQueue()

    
    @classmethod
    def getPaused(cls) -> bool:
        return cls.paused
    
    @classmethod
    def setPaused(cls,newVal:bool):
        cls.paused = newVal
        if newVal:
            pygame.mixer_music.pause()
        else:
            pygame.mixer_music.unpause()

    @classmethod
    def pause(cls):
        cls.setPaused(True)

    @classmethod
    def unpause(cls):
        cls.setPaused(False)

    @classmethod
    def set_volume(cls,volume:float):
        pygame.mixer_music.set_volume(volume)
        cls.volume = volume
    
    @classmethod
    def get_volume(cls) -> float:
        return pygame.mixer_music.get_volume()
    
    @classmethod
    def playAbsolute(cls,index:int):
        cls.songLoaded = True
        cls.paused = False
        cls.songQueue.current= database.songs[index]
        pygame.mixer_music.load(MUSIC_PATH + '\\' + str(database.songs[index].id) + '.ogg')
        pygame.mixer_music.play()


    
print(MusicPlayer.paused)
