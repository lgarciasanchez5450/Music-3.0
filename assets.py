from framework import resizeSurface,loadImg,flipSurface
import framework
ShuffleOn = resizeSurface(loadImg('__Images/NewShuffleOn.png',True),(30,30))
ShuffleOff = resizeSurface(loadImg('__Images/ShuffleOn.png',True),(30,30))
NotOnRepeat = resizeSurface(loadImg('__Images/NotOnRepeat.png',True),(30,30))
OnRepeat = resizeSurface(loadImg('__Images/OnRepeat.png',True),(30,30))
PrevSong = resizeSurface(loadImg('__Images/PrevSongButton.png',True),(30,30))
NextSong = resizeSurface(flipSurface(loadImg('__Images/PrevSongButton.png',True),True,False),(30,30))
Paused = resizeSurface(loadImg('__Images/NewPaused.png',True),(15,15))
UnPaused = resizeSurface(loadImg('__Images/NewPlaying.png',True),(15,15))
Logo = resizeSurface(loadImg('__Images/Logo.jpeg'),(64,64))
FullSizeLogo = resizeSurface(loadImg('__Images/Logo.jpeg'),(framework.HEIGHT,framework.HEIGHT))
noInternet = loadImg('__Images/noInternet.jpg')