# AUTHOR: JAKE FOGEL
# STUDENT ID: 261085935

import musicalbeeps

# player = musicalbeeps.Player()
# player.play_note("C4", 1.0) --> Takes note string and duration (+ # or b)

class Note():
    """A class representing a music note to be played by a music player
    
    Instance Attributes:
    * duration: int
    * pitch: str
    * octave: int
    * accidental: str
    Class Attributes:
    * OCTAVE_MIN: int
    * OCTAVE_MAX: int
    """
    
    
    OCTAVE_MIN = 1
    OCTAVE_MAX = 7
    
    def __init__(self, duration, pitch, octave=1, accidental='natural'):
        """(float, str, int, str) -> NoneType
        Initializes a Note object
        
        >>> note = Note(2.0, 'A', 2, 'natural')
        >>> note.octave
        2
        >>> note = Note(2.0, 'T', 2, 'natural')
        AssertionError: Please enter valid pitch
        >>> note = Note(2.0, 'A', 89, 'natural')
        AssertionError: Please enter valid octave
        """
        
        if type(duration) != float or type(pitch) != str or type(octave) != int or type(accidental) != str:
            raise AssertionError('Please enter duration, pitch, octave, and accidental of correct type')
        if duration < 0:
            raise AssertionError('Please enter valid duration')
        if pitch not in 'ABCDEFGR':
            raise AssertionError('Please enter valid pitch')
        if octave < Note.OCTAVE_MIN or octave > Note.OCTAVE_MAX:
            raise AssertionError('Please enter valid octave')
        if accidental.lower() not in ['sharp','flat','natural']:
            raise AssertionError('Please enter valid accidental')
            
        self.duration = duration
        self.pitch = pitch
        self.octave = octave
        self.accidental = accidental.lower()
       
    def __str__(self):
        """() -> str
        Returns string to be outputted whem Note object is printed
        
        >>> note = Note(2.0, 'A', 2, 'natural')
        >>> print(note)
        2.0 A 2 natural
        >>> note = Note(2.0, 'B', 2, 'natural')
        >>> print(note)
        2.0 B 2 natural
        >>> note = Note(2.0, 'C', 2, 'natural')
        >>> print(note)
        2.0 C 2 natural
        """
        return str(self.duration) + ' ' + str(self.pitch) + ' ' + str(self.octave) + ' ' + str(self.accidental)
    
    def play(self, music_player):
        note_string = ''
        duration = float(self.duration)
        
        if self.pitch == 'R':
            note_string = 'pause'
        else:
            note_string = self.pitch + str(self.octave)
            if self.accidental == 'sharp':
                note_string += '#'
            elif self.accidental == 'flat':
                note_string += 'b'
            
            
        music_player.play_note(note_string, duration)
        



