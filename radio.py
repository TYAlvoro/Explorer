import vlc
import time


def play_radio(name, secs):
    with open('radios.txt', encoding='utf-8') as f:
        radios = [x.strip().split('*')[1] for x in f if x.strip().split('*')[0] == name]  
    media = vlc.MediaPlayer(radios[0])
    media.play()
    playing = set([1, 2, 3, 4])
    play = True
    howLongToRun = secs
    timeout = time.time() + howLongToRun 
    while play:
        time.sleep(0.5)
        state = media.get_state()
        if time.time() > timeout:
            play = False
        if state in playing:
            continue
        else:
            play = False
    media.stop()