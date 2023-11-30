from typing import Any
from framework import ButtonSwitch,Dropdown,TextBox
import framework
from colors import null,white,theme_yellow
from assets import Paused, UnPaused
from AppFramework import MusicPlayer,database
from utils import isInsideCircle
class PauseButton(ButtonSwitch):
    shared_state = [0]
    @classmethod
    def accepts(cls) -> tuple:
        return ('mpos','mb1down','KDQueue')
    def __init__(self,pos:tuple[int,int]):
        size = 20
        super().__init__((pos[0] - size,pos[1] - size),(size*2,size*2),1,[UnPaused,Paused])  


    def update(self,input:tuple):
        if not MusicPlayer.songLoaded: return
        if MusicPlayer.paused != self.state:
            self.state = MusicPlayer.paused
        mpos,mb1,KDQueue = input
        if (' ' in KDQueue) or (self._rect.collidepoint(mpos)  and mb1 and isInsideCircle(mpos[0],mpos[1],self._rect.centerx,self._rect.centery,20)):
            MusicPlayer.setPaused(not MusicPlayer.paused)
            self.state = (self.state + 1) % len(self.state_pics)

    def draw(self):
        png = self.state_pics[self.state]
        framework.draw.circle(framework.screen,white,self._rect.center,20)
        framework.screen.blit(png,(self._rect.centerx - png.get_width()//2, self._rect.centery - png.get_height()//2))

class AllSongsList(Dropdown):
    def __init__(self, pos, size, up_color, down_color, text_color, maxy):
        super().__init__(pos, size, up_color, down_color, text_color, database.getAllSongNames, MusicPlayer.playAbsolute, maxy, None, (3,10), 1)

class SongTitle(TextBox):
    def __init__(self, pos, font):
        super().__init__(pos, font, "No Song", theme_yellow)

    def update(self,thing:tuple):
        name = MusicPlayer.songQueue.current.name if MusicPlayer.songQueue.current is not None else "No Song"
        if self.text != name:
            self.setText(name)
