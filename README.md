# generate-midi

Some old code I wrote for my HS research project. Abandoned this project in June 2023 but making this repo public as it's a proof-of-concept of what agent-based systems can do.

# generate-midi

This library generates a .midi file of chords of an alternating verse and chorus pattern (verse-chorus-verse-chorus). The verses/choruses can either be simple (using the SimpleAgent), exotic (using the ExoticAgent), or not repetitive (using the NonRepetitiveAgent). This can be updated by changing line 13 of generate_midi_VCVC.py. 

```
x = WhateverAgentYouWant();
```

Be sure to use pip install to install the midiutil and mingus.core library. 

Versions:
* First: Generates a certain number of chords using the transition matrix. This is in generate_midi_first.py in Old folder.
* Second: Generates a verse of the form A-B-A-B. Each segment is one bar of four quarter-note chords. This is in generate_midi_ABAB.py in Old folder.
* Third: Creation of a larger song with a verse and a chorus of form V-C-V-C. Verse was 8 bars and chorus was 4 bars. This is in generate_midi_VCVC.py.
* Fourth: Improving upon the larger song by allowing the user to specify chord exoticness and randomness. The different "agents" (SimpleAgent, ExoticAgent, NonRepetitiveAgent) represent this. 

Note that the third implementation and onward is implemented using OOP. The Chord class represents a chord in music while the Section class represents a section (either a verse or chorus). 

