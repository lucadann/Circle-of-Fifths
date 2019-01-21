###  DIATONIC SCALE AND CHORD GENERATION USING THE CIRCLE OF FIFTHS ###

import numpy as np
from pandas import Series

class Diatonic_Scale(Series):
    CoF = np.array(['Fb', 'Cb', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F', 'C', 'G', 'D',
        'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#', 'E#', 'B#'])
    modes = {'Lydian' : 3, 'Ionian' : 2, 'Mixolydian' : 1, 'Dorian' : 0,
        'Aeolian' : -1, 'Phrygian' : -2, 'Locrian' : -3}
    def __init__(self, root, mode):
        if root in Diatonic_Scale.CoF[np.concatenate([np.arange(-3-Diatonic_Scale.modes[mode], 0),
            np.arange(0, 3-Diatonic_Scale.modes[mode])])]:
            raise Exception("Inappropriate key signature")
        else:
            root_position = np.where(Diatonic_Scale.CoF == root)[0]
            notes = Diatonic_Scale.CoF[np.arange((root_position-3+Diatonic_Scale.modes[mode]),
                (root_position+3+Diatonic_Scale.modes[mode]+1))]
            scale = np.array([notes]*3).flatten()[(3-Diatonic_Scale.modes[mode])::2][:7]
            super().__init__(scale, index = np.arange(1, 8))
            self.root = root
            self.mode = mode
    def chord(self, position, seventh = False):
        chord = self.append(self)[(position-1)::2][0:(3+seventh)]
        chord.index = [1, 3, 5] + [7,]*seventh
        return chord
