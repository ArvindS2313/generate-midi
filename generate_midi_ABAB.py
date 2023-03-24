from midiutil import MIDIFile
from mingus.core import chords
from mingus.core.mt_exceptions import FormatError
import random
# Install libraries 

def convert(note, octave):
    # converts a note to a MIDI number
    if "bb" in note:
        note = note.replace("bb", "")
        return (NOTES[note] - 2) + 12 * (octave + 1)
    if "##" in note:
        note = note.replace("##", "")
        return (NOTES[note] + 2) + 12 * (octave + 1)
    return NOTES[note] + 12 * (octave + 1)


with open("transition_matrix.txt", "r") as tm:
    # reads data from the transition_matrix.txt file

    # generated a 2D list - each nth sublist contains the chords from the nth song.
    a = tm.read()
    a = a.split(")")
    for x in range(len(a)):
        a[x] = a[x].replace("'", "")
        a[x] = a[x].replace("(", "")
        a[x] = a[x].replace("\n", "")
        a[x] = a[x].split(",")[6:]

# use data from lists to generate a transition matrix dictionary
chord_tm = {}
for song in a:
    for i in range(len(song)):
        chord = song[i]
        if chord not in chord_tm:
            chord_tm[chord] = {}
        if i < len(song) - 1:
            if song[i + 1] not in chord_tm[chord]:
                chord_tm[chord][song[i + 1]] = 0
            chord_tm[chord][song[i + 1]] += 1
