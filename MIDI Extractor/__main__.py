try:
    import pretty_midi, os, pyperclip
except ImportError:
    import os
    os.system("pip install pretty_midi && pip install pyperclip")
    import pretty_midi, pyperclip
number_round = input("Round number (2: less accurate,saves data|3: more accurate,more data|4,5..)\n > ")
if 'e' in number_round:
    plane_crazy = True
else:
    plane_crazy = False
number_round = int(number_round.replace("e",""))
os.chdir(os.path.dirname(__file__))
cnt = 0
lst = []
made_temp = False
for b in os.listdir("MIDI_Files"):
    if b.endswith(".mid") or b.endswith(".midi"):
        lst.append(b)
for x in lst:
    if x.endswith(".mid") or x.endswith(".midi"):
        cnt += 1
        print(cnt,"-",x)
song = input("File or Download Link > ")
try:
    midi_data = pretty_midi.PrettyMIDI(lst[int(song)-1])
except:
    try:
        import requests

    except ImportError:
        os.system('pip install requests')
    # Make a requests object that downloads a download link
    r = requests.get(song,headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.362"})
    # Make the open function name it ending with .mid or .midi depending on the file extension in the link
    open(f"temp.{song.split(".")[-1]}","wb").write(r.content)
    made_temp = True
    try:
        midi_data = pretty_midi.PrettyMIDI(f"temp.{song.split(".")[-1]}")
    except:
        os.remove(f"temp.{song.split(".")[-1]}")
        
apnd = ""
for instrument in midi_data.instruments:
    for note in instrument.notes:
        if not plane_crazy:
            #print(f'{note.pitch:10} {note.start:10} {note.end:10}')
            duration = round(note.end-note.start,number_round)
            #print(f'{str(note.pitch)}|{str(round(note.start,number_round))}|{str(duration)},',end="")
            apnd += f'{str(note.pitch)}|{str(round(note.start,number_round))}|{str(duration)},'
        else:
            apnd +=  str(note.pitch)+"-"+str(round(note.start,number_round))+";"
print("Copied to your clipboard")
pyperclip.copy('"' + apnd + '"')
if made_temp:
    os.remove(f"temp.{song.split(".")[-1]}")