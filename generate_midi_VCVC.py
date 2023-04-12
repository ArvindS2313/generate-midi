from Section import Section
from SimpleAgent import SimpleAgent
from midiutil import MIDIFile

# verse = Section("A", "B", "A", "B", "A", "C", "A", "B")
# for x in ("A", "B", "C"):
#     verse.generate_pattern(x)

# chorus = Section("D", "E", "D", "E")
# chorus.generate_pattern("D", verse.segments[1][-1])
# chorus.generate_pattern("E")

x = SimpleAgent()
verse = x.verse
chorus = x.chorus

# Constant MIDI file information
track = 0
channel = 0
time = 0
duration = 1
tempo = 120
volume = 100

MyMIDI = MIDIFile(1)
MyMIDI.addTempo(track, time, tempo)

counter = 0

for segment in (verse, chorus, verse, chorus):
    for part in segment.segments:
        for chord in part:
            for note in chord.midi:
                MyMIDI.addNote(track, channel, note, time + counter, duration, volume)
            counter = counter + 1


with open(f"VCVC_simple_agent.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
    print("File has been outputted.")

# Print VERSE
print("Verse Segments: ", end="  ")
for segment in verse.segments:
    for chord in segment:
        print(chord.name, end="  ")
print()
print("Chorus Segments: ", end="  ")
for segment in chorus.segments:
    for chord in segment:
        print(chord.name, end="  ")



