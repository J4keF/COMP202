import musicalbeeps
from melody import Melody

if __name__ == "__main__":
    player = musicalbeeps.Player()
    melody = Melody("megalovania.txt")
    print(melody.get_total_duration())
    for note in melody.notes:
        print(note)
    
    melody.upper_octave()
    melody.upper_octave()
    melody.change_tempo(0.342)
    print(melody.get_total_duration())
    melody.play(player)