MOVEMENT_SYMBOLS = '><v^'

EMPTY_SYMBOL = '.'

TREASURE_SYMBOL = '+'

BREADCRUMB_SYMBOL = 'X'

MOVEMENT_SYMBOLS_3D = '*|'

def get_nth_row_from_map(map_string, row, width, height):
    """ (str, int, int, int) -> str
    Takes a map (map_string), index of row to print (row), width
    (width), and height (height) and returns the indicated row to
    print from the map
    
    >>> get_nth_row_from_map('^..>>>..v', 1, 3, 3)
    '>>>'
    >>> get_nth_row_from_map('..........', 2, 2, 5)
    '..'
    >>> get_nth_row_from_map('.<.>', 3, 1, 4)
    '>'
    """
    
    if row >= height:
        return ""
    return map_string[width * (row): width * (row + 1)]
        
def print_treasure_map(map_string, width, height):
    """ (str, int, int) -> NoneType
    Takes a map (map_string), width (width), and height (height) and
    prints the 2D map with each row on a new line
    
    >>> print_treasure_map('<..vvv..^', 3, 3)
    <..
    vvv
    ..^
    >>> print_treasure_map('XXXX', 2, 2)
    XX
    XX
    >>> print_treasure_map('.*.*.*.*', 2, 4)
    .*
    .*
    .*
    .*
    """
    
    for row in range (height):
        complete_row = ""
        for column in range (width):
            character = map_string[column + (width * row)]
            complete_row += character
        print (complete_row)

def change_char_in_map(map_string, row, column, character, width, height):
    """ (str, int, int, str, int, int) -> str
    Takes a map (map_string), and the index of row (row) and column
    (column) to replace with a character (character) in a map of]
    width (width) and height (height), returning the updated map
    
    >>> change_char_in_map('.........', 1, 1, 'X', 3, 3)
    '....X....'
    >>> change_char_in_map('....X....', 1, 1, '>', 3, 3)
    '....>....'
    >>> change_char_in_map('.<.....>.', 0, 0, '|', 3, 3)
    '|<.....>.'
    """
    
    if (row >= height or column >= width or row < 0 or column < 0):
        return map_string
    
    before_char = map_string[:column + (width*row)]
    after_char = map_string[column + 1 + (width*row):]
    
    return before_char + character + after_char

def get_proportion_travelled(map_string):
    """ (str) -> float
    Takes a map (map_string), and returns the percentage (represented
    in float form) of the map containing a bread crumb character,
    rounded to two decimal places
    
    >>> get_proportion_travelled('...XXX')
    0.5
    >>> get_proportion_travelled('.>....X')
    0.14
    >>> get_proportion_travelled('.')
    0.0
    """
    if map_string.count(BREADCRUMB_SYMBOL) == 0:
        return 0.0
    appearances = map_string.count(BREADCRUMB_SYMBOL)
    percent_covered = appearances/len(map_string)
    
    return round(percent_covered, 2)
        
    
def get_nth_map_from_3D_map(map_string, map_num, width, height, depth):
    """ (str, int, int, int, int) -> str
    Takes a 3D map (map_string), with width (width), height (height) and
    depth (depth) and returns the 2D map at a given depth index (map_num) 
    
    >>> get_nth_map_from_3D_map('.X.XXX.X..v.vXv.v.', 0, 3, 3, 2)
    '.X.XXX.X.'
    >>> get_nth_map_from_3D_map('XXX>>>|||XXX>*>|||.', 1, 3, 3, 2)
    'XXX>*>|||'
    >>> get_nth_map_from_3D_map('>>>>^^^^XXXX>>>>****^^^^.', 2, 4, 2, 3)
    '****^^^^'
    """
    
    if map_num >= depth or map_num < 0:
        return ""
    before_map = width*height*map_num
    after_map = width*height*(map_num + 1)
    
    return map_string[before_map:after_map]
        

def print_3D_treasure_map(map_string, width, height, depth):
    """ (str, int, int, int) -> NoneType
    Takes a 3D map (map_string), with width (width), height (height) and
    depth (depth) and prints the map with a blank line between each 2D
    map level 
    
    >>> print_3D_treasure_map('.X.XXX.X..v.vXv.v.', 3, 3, 2)
    .X.
    XXX
    .X.
    
    .v.
    vXv
    .v.
    >>> print_3D_treasure_map('**>>.|>>^******||<>|**^v', 4, 2, 3)
    **>>
    .|>>

    ^***
    ***|

    |<>|
    **^v
    >>> print_3D_treasure_map('>>>|||v><|||****<v', 3, 3, 2)
    >>>
    |||
    v><

    |||
    ***
    *<v
    """
    
    for map_num in range (depth):
        map_area = width * height
        map_volume = map_num * map_area
        
        for row in range (height):
            complete_row = ""
            
            for column in range (width):
                character = map_string[(width * row) + (map_volume) + column]
                complete_row += character
                
            print (complete_row)
        
        if map_num < depth - 1:
            print("")
       
def change_char_in_3D_map(map_string, row, column, map_num, character, width, height, depth):
    """ (str, int, int, int, str, int, int, int) -> str
    Takes a map (map_string), and the index of row (row), column
    (column), and depth (depth) to replace with a character
    (character) in a map of width (width), height (height), and
    depth (depth) returning the updated map
    
    >>> change_char_in_3D_map('.X.XXX.X..v.vXv.v.', 0, 0, 0, '#', 3, 3, 2)
    '#X.XXX.X..v.vXv.v.'
    >>> change_char_in_3D_map('^^**|<><><><>*<>|v', 1, 0, 0, 'X', 3, 3, 2)
    '^^*X|<><><><>*<>|v'
    >>> change_char_in_3D_map('**|>><X>', 0, 0, 1, 'X', 2, 2, 2)
    '**|>X<X>'
    """
    
    exceeds_map = row >= height or column >= width or map_num >= depth
    below_first_index = row < 0 or column < 0 or map_num < 0
    if (exceeds_map or below_first_index):
        return map_string
    
    map_area = width * height
    map_volume = map_num * map_area
    
    before_char = map_string[:(width * row) + (map_volume) + column]
    after_char = map_string[(width * row) + (map_volume) + column + 1:]
    
    return before_char + character + after_char