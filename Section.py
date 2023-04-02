from Chord import Chord 
from transition_dictionary import chord_tm
import random


class Section():
    def __init__(self, *pattern):
        self.pattern = pattern
        self.segments = [None for x in self.pattern] 
    

    def generate_pattern(self, segment, first_chord, num_chords=4):
        first_chord_name = first_chord.name
        chord_sequence = [first_chord]
        # generate the entire chord sequence
        sum = 0
        for i in range(num_chords-1):
            for key in chord_tm[first_chord_name].keys():
                sum += chord_tm[first_chord_name][key]
            random_number = random.randint(1, sum)
            curr_sum = 0
            for key in chord_tm[first_chord_name].keys():
                curr_sum += chord_tm[first_chord_name][key]
                if random_number <= curr_sum:
                    sum = 0
                    chord_sequence.append(Chord(key))
                    first_chord = key
                    break
        for i in range(len(self.pattern)):
            if self.pattern[i] == segment:
                self.segments[i] = chord_sequence
                
a = Section("A", "B", "A", "B")
a.generate_pattern("A", Chord("Dbsus4"))
a.generate_pattern("B", Chord("C"))
print(a.segments)