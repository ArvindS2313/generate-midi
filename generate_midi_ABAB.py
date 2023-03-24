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

# Starting chord for "A" and "B"
list_keys = list(chord_tm.keys())
starting_chord = random.choice(list_keys)


def generate_chord_sequence(starting_chord, num_chords):
    chord_sequence = [starting_chord]
    # generate the entire chord sequence
    sum = 0
    for i in range(num_chords):
        for key in chord_tm[starting_chord].keys():
            sum += chord_tm[starting_chord][key]
        random_number = random.randint(1, sum)
        curr_sum = 0
        for key in chord_tm[starting_chord].keys():
            curr_sum += chord_tm[starting_chord][key]
            if random_number <= curr_sum:
                sum = 0
                chord_sequence.append(key)
                starting_chord = key
                break
    return chord_sequence

A_chords = generate_chord_sequence(starting_chord, 3)
B_chords = generate_chord_sequence(starting_chord, 3)


# check for "add" phrase as mingus.core does not recognize them
def check_add(chord_sequence):
    for i in range(len(chord_sequence)):
        if "add" in chord_sequence[i] and "madd" not in chord_sequence[i]:
            chord_sequence[i] = chord_sequence[i].replace('add', '')

check_add(A_chords)
check_add(B_chords)


OCTAVE = 4  # all notes in octave 4
A0 = 21  # the MIDI number for A0 is 21
NOTES = {"B#": 0, "C": 0, "Dbb": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3,
         "E": 4, "Fb": 4, "E#": 5, "F": 5, "F#": 6, "Gb": 6, "G": 7,
         "G#": 8, "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11, "Cb": 11}

# Constant MIDI file information
track = 0
channel = 0
time = 0
duration = 2
tempo = 120
volume = 100

MyMIDI = MIDIFile(1)
MyMIDI.addTempo(track, time, tempo)

x = 0
# Generate MIDI file from chord sequence
def generate_MIDI_segment(chord_sequence): 
    global x, MyMIDI
    for i in range(len(chord_sequence)):
        chord = chord_sequence[i]  # for each chord in the chord sequence
        try:
            notes = chords.from_shorthand(chord)  # does mingus.core recognize the chord?
        except FormatError:
            print(f"Chord {i + 1} is causing an error. A C major chord"
                f" will be generated instead.")  # generate a Cmaj chord if it doesn't
            notes = ["C", "E", "G"]

        for note in notes:
            # add each note to the MIDI file
            # make sure that the notes are all generated at the same time!
            MyMIDI.addNote(track, channel, convert(note, 4), time + x, duration, volume)
            x = x + 1

print(A_chords)
print(B_chords)
for _ in range(2):
    generate_MIDI_segment(A_chords)
    generate_MIDI_segment(B_chords)

with open("random_chords.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
    print("File has been outputted.")

