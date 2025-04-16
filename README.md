# generate-midi

Some old code I wrote for my HS research project. Abandoned this project in June 2023 but making this repo public.

Be sure to use pip install to install the midiutil and mingus.core library. 

Versions:
* First: Generates a certain number of chords using the transition matrix.
* Second: Generates a verse of the form A-B-A-B. Each segment is one bar of four quarter-note chords.
* Third: Creation of a larger song with a verse and a chorus of form V-C-V-C. Verse was 8 bars and chorus was 4 bars.
* Fourth: Improving upon the larger song by allowing the user to specify chord exoticness and randomness (currently working on).

Note that the third implementation and onward is implemented using OOP. The fourth (current) implementation uses three agents (KB systems).

