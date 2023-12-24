try:
    import pretty_midi, os, pyperclip
except ImportError:
    import os
    os.system("pip install pretty_midi && pip install pyperclip")
    import pretty_midi, pyperclip
number_round = int(input("Round number (2: less accurate,saves data|3: more accurate,more data|4,5...)\n > "))
os.chdir(os.path.dirname(__file__))
cnt = 0
lst = []
for b in os.listdir():
    if b.endswith(".mid"):
        lst.append(b)
for x in lst:
    if x.endswith(".mid"):
        cnt += 1
        print(cnt,"-",x)

midi_data = pretty_midi.PrettyMIDI(lst[int(input("File > "))-1])
apnd = ""
for instrument in midi_data.instruments:
    for note in instrument.notes:
        #print(f'{note.pitch:10} {note.start:10} {note.end:10}')
        duration = round(note.end-note.start,number_round)
        print(f'"{str(note.pitch)}|{str(round(note.start,number_round))}|{str(duration)},"',end="")
        apnd += f'{str(note.pitch)}|{str(round(note.start,number_round))}|{str(duration)},'
print(apnd)
pyperclip.copy('"' + apnd + '"')