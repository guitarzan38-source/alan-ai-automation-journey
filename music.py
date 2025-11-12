#!/usr/bin/env python3
import random

sharps_table = [
    ["","Key","I","II","III","IV","V","VI","VII"],
    [0,"C","C","Dm","Em","F","G","Am","Bdim"],
    [1,"G","G","Am","Bm","C","D","Em","F#dim"],
    [2,"D","D","Em","F#m","G","A","Bm","C#dim"],
    [3,"A","A","Bm","C#m","D","E","F#m","G#dim"],
    [4,"E","E","F#m","G#m","A","B","C#m","D#dim"],
    [5,"B","B","C#m","D#m","E","F#","G#m","A#dim"],
    [6,"F#","F#","G#m","A#m","B","C#","D#m","E#dim"]
]

flats_table = [
    ["","Key","I","II","III","IV","V","VI","VII"],
    [1,"F","F","Gm","Am","Bb","C","Dm","Edim"],
    [2,"Bb","Bb","Cm","Dm","Eb","F","Gm","Adim"],
    [3,"Eb","Eb","Fm","Gm","Ab","Bb","Cm","Ddim"],
    [4,"Ab","Ab","Bbm","Cm","Db","Eb","Fm","Gdim"],
    [5,"Db","Db","Ebm","Fm","Gb","Ab","Bbm","Cdim"],
    [6,"Gb","Gb","Abm","Bbm","C","Db","Ebm","Fdim"]
]

def get_table_row(key):
    for row in sharps_table[1:]:
        if row[1] == key:
            return row
    for row in flats_table[1:]:
        if row[1] == key:
            return row
    return None

print("""
Welcome to the Music Key Query Program!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
     Sharps: C, G, D, A, E, B, F#
     Flats:  F, Bb, Eb, Ab, Db, Gb
""")

while True:
    key = input("Please select a key: ").strip()
    if key == "!":              # ← THIS IS THE FIX: quit immediately on "!" at key prompt
        print("See ya, rockstar! 🎸\n")
        break
    key = key.capitalize()
    row = get_table_row(key)
    if not row:
        print(f"ERROR: {key} isn't a valid key\n")
        continue
    
    last_r = 0
    while True:
        r = random.randint(1, 7)
        if r == last_r:
            r = (r % 7) + 1
        last_r = r
        
        chord_names = ["1st","2nd","3rd","4th","5th","6th","7th"]
        en = chord_names[r-1] + " Chord"
        
        answer = input(f"What is the {en} of the key of {key}? ").strip()
        if answer == "!":
            print()  # blank line
            break
            
        answer = answer.capitalize()
        correct = row[r+1]
        if r == 5:
            correct += "7"
            
        if answer == correct:
            print("Correct!\n")
        else:
            print(f"Actually, the {en.lower()} of {key} is {correct}\n")
        print("Input '!' to choose a different key\n")
