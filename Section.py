from Chord import Chord 
from transition_dictionary import chord_tm
import random


class Section():
    def __init__(self, *pattern):
        self.pattern = pattern
        self.segments = [None for x in self.pattern] 

    def gc(self, starting_chord=None):
        if starting_chord == None:
            return Chord(random.choice(list(chord_tm.keys())))
        else:
            starting_chord_name = starting_chord.name
            sum = 0
            for key in chord_tm[starting_chord_name].keys():
                sum += chord_tm[starting_chord_name][key]
            random_number = random.randint(1, sum)
            curr_sum = 0
            for key in chord_tm[starting_chord_name].keys():
                curr_sum += chord_tm[starting_chord_name][key] 
                if random_number <= curr_sum:
                    return Chord(key)

    def generate_pattern(self, segment, starter=None, num_chords=4):
        pass
        # first_chord = self.get_chord(starter)
        # first_chord_name = first_chord.name
        # chord_sequence = [first_chord]
        # # generate the entire chord sequence
        # sum = 0
        # for i in range(num_chords-1):
        #     for key in chord_tm[first_chord_name].keys():
        #         sum += chord_tm[first_chord_name][key]
        #     random_number = random.randint(1, sum)
        #     curr_sum = 0
        #     for key in chord_tm[first_chord_name].keys():
        #         curr_sum += chord_tm[first_chord_name][key]
        #         if random_number <= curr_sum:
        #             sum = 0
        #             chord_sequence.append(Chord(key))
        #             first_chord = key
        #             break
        # for i in range(len(self.pattern)):
        #     if self.pattern[i] == segment:
        #         self.segments[i] = chord_sequence

    def set_pattern(self, segment, chord_sequence):
        for i in range(len(self.pattern)):
            if self.pattern[i] == segment:
                self.segments[i] = chord_sequence

