def formatTime(secs:int):
    return f'{secs//60:3}:{secs%60:2}'

def PATH():
  from os.path import dirname, realpath
  return dirname(realpath(__file__))

def isInsideCircle(x1:int|float,y1:int|float,circlex:int|float,circley:int|float,rad:int|float) -> float:
   return (x1 - circlex)**2 + (y1 - circley)**2 < rad*rad

APPLICATION_PATH = PATH()
MUSIC_PATH = APPLICATION_PATH + '\\__Music'