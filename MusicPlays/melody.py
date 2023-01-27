# AUTHOR: JAKE FOGEL
# STUDENT ID: 261085935

from note import Note
import musicalbeeps

class Melody():
    """A class representing a melody to be played in sequence by a music player
    
    Instance Attributes:
    * title: str
    * author: str
    * notes: []
    """
    
    def __init__(self, file_name):
        """(str) -> NoneType
        Initializes a Melody object
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> len(happy_birthday.notes)
        25
        >>> happy_birthday = Melody("birthday.txt")
        >>> print(happy_birthday.notes[6])
        0.25 D 4 natural
        >>> buns = Melody("hotcrossbuns.txt")
        >>> print(buns[6])
        0.25 G 4 natural
        """
        
        file = open(file_name, 'r')
        rfile = file.read()
        list_file = rfile.split('\n')
            
        self.title = list_file[0]
        self.author = list_file[1]
        self.notes = []
        
        repeat = []
        repeating = False
            
        for note in list_file[2:]:
            
            line_list = note.split()
            
            if line_list[1] == 'R':
                new_note = Note(float(line_list[0]), line_list[1])
            else:
                new_note = Note(float(line_list[0]), line_list[1], int(line_list[2]), line_list[3])
            self.notes.append(new_note)
                
                
            if line_list[-1] == 'true':
                if repeating:
                    repeating = False
                    repeat.append(Note(new_note.duration, new_note.pitch, new_note.octave, new_note.accidental))
                        
                    self.notes += repeat
                            
                    repeat = []
                        
                else:
                    repeating = True
                
            if repeating:
                new_note_rep = Note(new_note.duration, new_note.pitch, new_note.octave, new_note.accidental)
                repeat.append(new_note_rep)
            
    def play(self, music_player):
        for note in self.notes:
            note.play(music_player)
            
    def get_total_duration(self):
        """() -> float
        Returns the total duration of a melody
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.get_total_duration()
        13.0
        >>> mega = Melody("megalovania.txt")
        >>> mega.get_total_duration()
        19.0
        >>> howl = Melody("howls.txt")
        >>> howl.get_total_duration()
        24.0
        """
        output = 0
        for note in self.notes:
            output += note.duration
        return output
    
    def change_octave(self, step):
        """(int) -> bool
        Changes the octave attribute of each note in a melody by a given step
        interval and returns its ability to do so as a bool
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.change_octave(-1)
        True
        >>> mega = Melody("megalovania.txt")
        >>> mega.change_octave(1)
        True
        >>> eigth_octave = Melody("songateigthoctave.txt")
        >>> eigth_octave.change_octave(1)
        False
        """
        
        for note in self.notes:
            if note.pitch == 'R':
                continue
            elif note.octave + step >= Note.OCTAVE_MIN and note.octave + step <= Note.OCTAVE_MAX:
                note.octave += step
            else:
                return False
        return True
    
    def lower_octave(self):
        """() -> bool
        Passes a given step into change_octave with step 1 and returns the
        called method output
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.lower_octave()
        True
        >>> happy_birthday.notes[1].octave
        2
        >>> mega = Melody("megalovania.txt")
        >>> mega.lower_octave()
        True
        >>> mega.notes[1].octave
        2
        >>> eigth_octave = Melody("songateigthoctave.txt")
        >>> eigth_octave.lower_octave()
        True
        >>> eight_octave.notes[1].octave
        7
        """
        return(self.change_octave(-1))
        
    def upper_octave(self):
        """() -> bool
        Passes a given step into change_octave with step 1 and returns the
        called method output
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.upper_octave()
        True
        >>> happy_birthday.notes[1].octave
        4
        >>> mega = Melody("megalovania.txt")
        >>> mega.upper_octave()
        True
        >>> mega.notes[1].octave
        4
        >>> eigth_octave = Melody("songateigthoctave.txt")
        >>> eigth_octave.upper_octave()
        False
        """
        
        return(self.change_octave(1))
        
    def change_tempo(self, factor):
        """() -> NoneType
        Passes a given step into change_octave with step 1 and returns the
        called method output
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.change_tempo()
        >>> happy_birthday.get_total_duration
        26
        >>> mega = Melody("megalovania.txt")
        >>> mega.change_tempo(2)
        >>> mega.get_total_duration
        38
        >>> eigth_octave = Melody("songateigthoctave.txt")
        >>> eigth_octave.change_tempo(2)
        >>> eigth_octave.get_total_duration()
        20
        """
        
        for note in self.notes:
            note.duration *= factor


