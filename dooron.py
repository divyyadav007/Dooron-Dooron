import time
import sys
from pygame import mixer

def print_lyrics():
    lyrics = [
        ("Sochu ke milni te bolaanga ki ❤️,", 0.08), 
        ("Teri taan gallaan ch shayari💕,", 0.08),
        ("Vekhegi mainu te sochegi kya tu 🤷‍♂️,", 0.06),
        ("Mitti da banda main, tu taan pari...👼", 0.07),
        ("Ishqe di galiyan ch khoya e dil ve😉", 0.06),
        ("Aas laagaye ik jaaye tu mil ve...😍", 0.07),  # <-- Yahan comma lagaya
        ("Kol tere mainu aan de soni ...😒", 0.07),          # <-- Yahan comma lagaya
        ("karaan main kitne jatan...😊", 0.07),   # <-- Yahan comma lagaya
        ("O soni 😘", 0.07),                            # <-- Yahan comma lagaya
        ("Dooron dooron main vekhaan tenu soneyo...😁", 0.07)
    ]

    # Total 10 lines hain, to delays bhi 10 hone chahiye (aapne 10 hi diye hain, Good!)
    delays = [1.5, 1.8, 1.5, 1.5, 1.5, 2.0, 1.5, 1.5, 0.5, 2.0] 

    # --- YAHAN CHANGE KARNA HAI ---
    intro_delay = 4  
    # ------------------------------

    print("\n🎵 Now Playing - Dooron Dooron 🎵\n")
    
    time.sleep(intro_delay) 

    for i, (line, char_speed) in enumerate(lyrics):
        for char in line:
            print(char, end='', flush=True)
            time.sleep(char_speed)
        
        # Error handling agar delays kam pad jayein
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(1) # Default delay
            
        print('')

def play_song():
    mixer.init()
    # Make sure file ka naam exactly same ho jo folder me hai
    # Agar file ka naam 'Dooron Dooron.mp3' hai to code me bhi wahi likhna space ke sath
    mixer.music.load("doorondooron.mp3") 
    mixer.music.play()

if __name__ == "__main__":
    play_song()
    print_lyrics()