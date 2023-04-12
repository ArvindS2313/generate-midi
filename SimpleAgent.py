from Section import Section
from Chord import Chord
import random

class SimpleAgent:
    def __init__(self):
        self.verse = Section("A", "B", "A", "B", "A", "C", "A", "B")
        self.chorus = Section("A", "B", "A", "B")
        self.generate_chords("A", self.verse)
        for segment in ("B", "C"):
            self.generate_chords(segment, self.verse)
        for segment in ("A", "B"):
            self.generate_chords(segment, self.chorus)

    def check_chord(self, chord):
        if len(chord.notes) > 3:
            return False
        if "7" in chord.name:
            return False
        if "9" in chord.name:
            return False
        if "add" in chord.name:
            return False
        if "dim" in chord.name:
            return False
        if "/" in chord.name:
            return False
        bad_chords_major = ["B", "Cb", "F#", "C#", "Gb", "Db"]
        bad_chords_minor = ["G#m", "D#m", "A#m", "Bbm", "Ebm", "Abm"]
        for maj_chord in bad_chords_major:
            if maj_chord in chord.name:
                return False
        for min_chord in bad_chords_minor:
            if min_chord in chord.name:
                return False
        return True

    def generate_chords(self, segment, section, starter=None):
        start_chord = section.gc(starter)
        while not self.check_chord(start_chord):
            start_chord = section.gc()

        chord_sequence = [start_chord]
        for i in range(3):
            # generate the next chord
            random_num = random.random()
            if random_num < 0.6: 
                chord_sequence.append(chord_sequence[-1])
            else:
                chord = section.gc()
                while not self.check_chord(chord):
                    chord = section.gc()
                chord_sequence.append(chord)
        section.set_pattern(segment, chord_sequence)