from framework import ScrollingMS, Window_Space, getAllInput, init, Button
from framework import RESIZABLE, MinScreenSize,SetSoundVolume,setWindowIcon,setOnSoundPlay
from framework import *
init((900,600),RESIZABLE,'Music-Leo')
from UIFramework import PauseButton, AllSongsList,SongTitle
from utils import formatTime
from colors import *
from assets import *
MinScreenSize(450,300)
SetSoundVolume(.25)
starting_mainSpace = 0
answer_list:list = list()
runningSongLen:int = 1
runningSongName = 'No Song'
window_space = Window_Space()
setWindowIcon(Logo)
timer = Stopwatch()

def onMusicLoad() -> None:
  global runningSongLen,runningSongName,queue
  window_space.bottom.songTitle.setText(runningSongName) #type: ignore
  window_space.bottom.songLen.setText(formatTime(runningSongLen)) #type: ignore
  window_space.getMainSpace(5).queueNames.recalculate_options() #type: ignore
  window_space.getMainSpace(5).playing_now.setText(runningSongName) #type: ignore
  if window_space.activeMainSpace == 5: 
    window_space.update_mainspace(5)
  window_space.bottom.pauseButton.text = UnPaused #type: ignore
  window_space.bottom.magicSlider.changeSliderLimits(newMax = runningSongLen) #type: ignore
  timer.reset()
  timer.unpause()
setOnSoundPlay(onMusicLoad)

def setMSTo(num) -> framework.Callable:
  global window_space
  def _():
    global starting_mainSpace
    window_space.setActiveMainSpace(num)
    starting_mainSpace = num
  return _

def preStart():
  global dataBase,playlists,window_space,timer,title,queue
  title = TitleScreen(1)
  title.logopic = Image((framework.WIDTH//2-framework.HEIGHT//2,0),FullSizeLogo) #type: ignore
  title._start()
  addKeysThatIgnore(escape_unicode)
  addKeysThatIgnore(enter_unicode)


def postStart() -> None:
  while not title.TitleDone:
    time.sleep(.01)
  for _,playlist in enumerate([]):
    window_space.addMainSpace(ScrollingMS())
    window_space.getMainSpace(_+6).songs = Dropdown((20,100),(window_space.MSSize[0]-40,40),light_grey,dark_grey,black,None,None,window_space.MSSize[1]-100,None,(0,10))
    window_space.getMainSpace(_+6).titleBox = ScreenSurface((0,0),(window_space.MSSize[0],100),royal_purple)    
    window_space.getMainSpace(_+6).title = TextBox((10,10),makeFont('Roboto',50),playlist.name,white)
    window_space.getMainSpace(_+6).renameTitle = Button((window_space.MSSize[0]-100,10),80,30,None,grey,theme_light_purple,theme_purple,'Rename',2,text_color= white)
    window_space.getMainSpace(_+6).playSongs = RoundButton((30,70),20,None,theme_light_yellow,theme_yellow,theme_yellow,resizeSurface(Paused,(20,20)),-10,-10)
  window_space.setActiveMainSpace(starting_mainSpace)
  window_space.first_update()
  window_space.first_draw()
  window_space.drawMS()



def redoDownloadScreen():
  window_space.emptyMainSpace(4)  
def start() -> None:
  #Screen Objects
  global window_space
  window_space = Window_Space()
  window_space.addBorder('bottom',70 ,light_dark_grey,2)
  window_space.addBorder('left',200,theme_purple,1,theme_light_purple,3)
  window_space.addMiniWindow('Add Playlist',(framework.WIDTH//2-200,framework.HEIGHT//2-150),(400,300))
  window_space.miniWindow('Add Playlist').newPlaylistName = InputBox((30,40),(340,25),'New Playlist Name',dark_light_grey,20,None,upperCaseLetters.union(lowerCaseLetters).union(miscCharacters).union(numbers).union(symbolCharacters))
  window_space.miniWindow('Add Playlist').doneButton = Button((30,70),70,24,None,dark_green,grey,light_green,'Done',10,2,None,'\r')
  window_space.miniWindow('Add Playlist').cancelButton = Button((300,70),70,24,window_space.deactivateMiniWindow,dark_green,grey,light_green,'Cancel',2,2,None,'\x1b')
  window_space.addMiniWindow('Add Song',(framework.WIDTH//2-200,framework.HEIGHT//2-150),(400,300))
  window_space.miniWindow('Add Song').DownloadedName = InputBox((10,50),(380,30),'Save Song As:',light_grey,30,None,fileNameFriendlyCharactes)
  window_space.miniWindow('Add Song').okButton = Button((10,100),100,50,None,dark_green,light_green,green,'Download',10,15)
  window_space.addMiniWindow('Rename Playlist',(framework.WIDTH//2-250,framework.HEIGHT//2-75),(500,200))
  window_space.miniWindow('Rename Playlist').newName = InputBox((10,40),(480,30),'New Name:',light_grey,30,None,allLetters.union(miscCharacters).union(numbers).union(symbolCharacters))
  window_space.miniWindow('Rename Playlist').done = Button((10,80),50,30,None,grey,grey,white,'Done',10,0,None,enter_unicode)
  window_space.mainSpace = ScrollingMS() # Home Page
  window_space.mainSpace.welcome_text = TextBox((30,30),font.SysFont('Arial',20),'Welcome To Fake Spotify 3.0!', light_red)
  window_space.mainSpace.welcome_text2 = TextBox((30,60),font.SysFont('Arial',20),'Brought to you by: ME (leo)', light_green)
  window_space.mainSpace.improvements = TextBox((30,95),makeFont('Arial',20),'Improvments: Absolutely Nothing!!!!!',white)
  window_space.mainSpace.unprovements = TextBox((30,130),makeFont('Arial',20),'Downgrades: Lots of things stopped working!!!!!',white)
  window_space.mainSpace.notes = TextBox((30,155),makeFont('Arial',20),'NOTE: Dont click, "hello" the program will crash',white)
  window_space.mainSpace.notes = TextBox((30,155),makeFont('Arial',20),'and also the program will forever be too dumb to realize that you are online',white)
  window_space.mainSpace = ScrollingMS() # Search Page
  window_space.mainSpace.searchBox = InputBox((20,30),(window_space.MSSize[0]-110,26),'Song Name',light_grey,30,None,upperCaseLetters.union(lowerCaseLetters).union(miscCharacters).union(numbers).union(symbolCharacters))
  window_space.mainSpace.searchButton = Button((window_space.MSSize[0]-85,30),75,26,None,dark_grey,grey,light_grey,'Search',5,5,key='\r')
  window_space.mainSpace.results = Dropdown((20,66),(window_space.MSSize[0]-40,40),grey,dark_grey,black,lambda:answer_list,None,window_space.MSSize[1]-66,None,(0,10))
  window_space.mainSpace = ScrollingMS() # All Songs Page
  window_space.mainSpace.songs = AllSongsList((20,100),(window_space.MSSize[0]-40,40),(80,80,80),(120,120,120),(255,255,255),window_space.MSSize[1]-100)
  window_space.mainSpace.topBorder = ScreenSurface((0,0),(window_space.MSSize[0],100),theme_red_purple)
  window_space.mainSpace.mstitle = TextBox((10,10),font.SysFont('Roboto',50),'All Songs', theme_light_yellow)
  window_space.mainSpace = ScrollingMS() # Add To Playlist Page
  window_space.mainSpace.allPlaylists = Dropdown((20,50),(window_space.MSSize[0]-40,30),light_grey,grey,black,None,None,window_space.MSSize[1]-50)
  window_space.mainSpace = ScrollingMS() # Download Song Page
  window_space.mainSpace.surf = Image((window_space.MSSize[0]//2-noInternet.get_size()[0]//2,100),noInternet)
  window_space.mainSpace.text = TextBox((window_space.MSSize[0]//2-100,300),makeFont('Arial',30),'NO INTERNET',purple)
  window_space.mainSpace = ScrollingMS() # Song Queue Page
  window_space.mainSpace.top_border = ScreenSurface((0,0),(window_space.MSSize[0],50),theme_dark_purple)
  window_space.mainSpace.queue_text = TextBox((10,2),makeFont('Arial',40,True),'Queue',white)
  window_space.mainSpace.playing_now_text = TextBox((10,55),makeFont('Arial',25),'Playing Now:',white)
  window_space.mainSpace.up_next_text = TextBox((10,130),makeFont('Arial',25),'Up Next:',white)
  window_space.mainSpace.playing_now = TextBox((10,90),makeFont('Arial',25),'No Song Playing',theme_light_yellow)
  window_space.mainSpace.queueNames = Dropdown((10,160),(200,50),grey,grey,blue,lambda : [],None,window_space.MSSize[1]-160)

  window_space.left.homeButton = Button((0,0),window_space.leftSize,50,setMSTo(0),light_grey,theme_red_purple,blue,' Home',0,10,text_color=theme_light_yellow) #type: ignore
  window_space.left.searchButton = Button((0,53),window_space.leftSize,50,setMSTo(1),light_grey,theme_red_purple,blue,' Search',0,10,text_color=theme_light_yellow) #type: ignore
  window_space.left.allSongs = Button((0,106),window_space.leftSize,50,setMSTo(2),light_grey,theme_red_purple,blue,' All Songs',0,10,text_color=theme_light_yellow) #type: ignore
  window_space.left.addPlaylist = Button((0,159),window_space.leftSize,50,window_space.activateMiniWindow('Add Playlist',True),light_grey,theme_red_purple,blue,' New Playlist',0,10,text_color=theme_light_yellow) #type: ignore
  window_space.left.downloadSong = Button((0,212),window_space.leftSize,50,setMSTo(4),light_grey,theme_red_purple,blue,' Download Song',1,10,text_color=theme_light_yellow) #type: ignore
  window_space.left.playListDropdown = Dropdown((0,265),(window_space.leftSize,25),light_green,light_grey,black,lambda : ['hello'],None,framework.HEIGHT-265,None,(5,0)) #type: ignore
  window_space.bottom.slider = Slider(framework.WIDTH-110,35,100,5,1,101,lambda x:SetSoundVolume((x/100)**2),dark_grey,theme_yellow) #type: ignore
  window_space.bottom.slider.set_value(sqrt(getSoundVolume())*100) #type: ignore
  #window_space.bottom.pauseButton = RoundButton((framework.WIDTH//2,window_space.bottomSize//2-5),20,None,light_grey,white,light_grey,Paused,-7,-7,key = ' ')

  window_space.bottom.pauseButton = PauseButton((framework.WIDTH//2,window_space.bottomSize//2-5)) #type: ignore

  window_space.bottom.magicSlider = Slider(framework.WIDTH//4,window_space.bottomSize-13,framework.WIDTH//2,5,0,runningSongLen,None,black,grey,True,2,theme_purple) #type: ignore
  #window_space.bottom.magicSlider.onDeactivate = setMusicPos
  window_space.bottom.nextSongButton = Button((framework.WIDTH//2+30,window_space.bottomSize//2-20),30,30,None,light_dark_grey,light_dark_grey,light_dark_grey,NextSong) #type: ignore
  window_space.bottom.prevSongButtom = Button((framework.WIDTH//2-60,window_space.bottomSize//2-20),30,30,None,light_dark_grey,light_dark_grey,light_dark_grey,PrevSong) #type: ignore
  window_space.bottom.repeatButton = ButtonSwitch((framework.WIDTH//2+65,window_space.bottomSize//2-20),(30,30),0,[NotOnRepeat,OnRepeat] ) #type: ignore
  window_space.bottom.shuffleButton = Button((framework.WIDTH//2-95,window_space.bottomSize//2-20),30,30, lambda:1,light_dark_grey,light_dark_grey,light_dark_grey,ShuffleOff) #type: ignore
  window_space.bottom.songSecs = TextBox((framework.WIDTH//4-40,window_space.bottomSize-20),makeFont('Arial',18),'0:00',theme_yellow) #type: ignore
  #window_space.bottom.songTitle = TextBox((5,10),font.SysFont('Roboto',30),runningSongName,theme_yellow) #type: ignore
  window_space.bottom.songTitle = SongTitle((5,10),font.SysFont('Roboto',30)) #type: ignore
  window_space.bottom.songLen = TextBox((3*framework.WIDTH//4+5,window_space.bottomSize-20),makeFont('Arial',18),'0:00',theme_yellow) #type: ignore
  window_space.bottom.songLen.setText(formatTime(runningSongLen)) #type: ignore
  window_space.bottom.queueButton = Button((framework.WIDTH-150,35),30,20,setMSTo(5),blue,blue,black,'KEU',text_color=white) #type: ignore
  window_space.bottom.pauseButton.text = Paused if getSoundPos() == -1 else UnPaused #type: ignore

preStart()
start()
postStart() 
running = 1
while running:
  myInput = getAllInput()
  if myInput.quitEvent:
    window_space.onQuit()
    break
  else:
    if VIDEORESIZE in myInput.Events:
      start()
      postStart()
  window_space.update(myInput)
  window_space.draw()
  tick()
