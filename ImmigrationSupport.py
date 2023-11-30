from os import walk
from os.path import dirname
from json import load,dump
def getSongLen(fileName) -> int:
    from mutagen.oggvorbis import OggVorbis
    song = OggVorbis(fileName)
    return song.info.length.__ceil__()
if False:
    MUSIC_PATH = dirname(__file__) + "\\__Music"
    key = load(open(MUSIC_PATH+"\\key.json",'r'))
    _,_,files = next(walk(MUSIC_PATH))
    key:list[dict] = []
    id = 0
    for fileName in filter(lambda x: x.endswith(('ogg','mp3','wav')),files):
        #these file names are actually id's which correspond with the index in <key> for their attributes
        key.append({})
        name = fileName
        print("Name: "+name)
        artists = input('Artists: ').split("\\")
        print(artists)
        album = input("Album Name: ")
        length = getSongLen(MUSIC_PATH + "\\"+fileName)
        inp = input("is the length: "+ str(length) + '??? If not then put a number if yes then empty: ') 
        if inp:
            length = int(inp)
        key[id].update({"name":name,"artists":artists,"album":album,"length":length})
        id += 1

    print(key)

    yorn = input("Do you wanna save dump this?? O_O")

    if yorn.lower() in ('y','yes','ye','hehehehaw'):
        dump(key,open(MUSIC_PATH+"\\key.json",'w'))
if False:
    MUSIC_PATH2 = dirname(__file__) + "\\__Music2"
    MUSIC_PATH = dirname(__file__) + "\\__Music"
    #_,_,files = next(walk(MUSIC_PATH))
    key2 = load(open(MUSIC_PATH2+"\\key.json",'r'))
    key = load(open(MUSIC_PATH+"\\key.json",'r'))
    import shutil
    songs = list([k['name'] for k in key])
    print(songs)
    int(input("YES??"))
    i_ = 0
    for i,song in enumerate(key2):
        if song['name'] in songs:
            int(input(f'putting {song["name"]}({i}.ogg) as {i_}.ogg'))
            shutil.copy2(MUSIC_PATH2+"\\"+str(i)+".ogg",MUSIC_PATH+"\\"+str(i_)+'.ogg')
            i_+=1 

