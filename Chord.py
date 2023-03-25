from mingus.core import chords
from mingus.core.mt_exceptions import FormatError

class Chord:
    def __init__(self, name, octave=4, inversion=0) -> None:
        self.name = name
        self.octave = octave
        self.inversion = inversion
        self.notes = self.generate_notes()
        self.NOTES = {"B#": 0, "C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3,
         "E": 4, "Fb": 4, "E#": 5, "F": 5, "F#": 6, "Gb": 6, "G": 7,
         "G#": 8, "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11, "Cb": 11}
        self.midi = self.convert()

        
    def generate_notes(self):
        try:
            notes = chords.from_shorthand(self.name)
        except FormatError:
            notes = ["C", "E", "G"]
        notes = [[note,self.octave] for note in notes]
        return notes

    def apply_inversion(self):
        for i in range(self.inversion):
            to_remove = self.notes[0]
            to_remove[1] += 1 
            self.notes.pop(0)
            self.notes.append(to_remove)

    def convert(self):
        for note in self.notes:
            # converts a note to a MIDI number
            if "bb" in note[0]:
                note[0] = note[0].replace("bb", "")
                return (self.NOTES[note[0]] - 2) + 12 * (self.octave + 1)
            if "##" in note[0]:
                note[0] = note[0].replace("##", "")
                return (self.NOTES[note[0]] + 2) + 12 * (self.octave + 1)
            return self.NOTES[note[0]] + 12 * (self.octave + 1)

a = Chord("Cmaj7", inversion=1)
a.apply_inversion()
print(a.notes)