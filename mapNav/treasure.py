import random
from treasure_utils import *

def change_char_in_row(row_string, index, character):
    """ (str, int, str) -> str
    Takes a row of a map (row_string) and an index (index)
    to replace with a character (character) returning the
    updated row
    
    >>> change_char_in_row('........', 4, '>')
    '....>...'
    >>> change_char_in_row('...', 2, '*')
    '..*'
    >>> change_char_in_row('......>><', 1, '|')
    '.|....>><'
    """
    
    before_char = row_string[:index]
    after_char = row_string[index + 1:]
    
    return before_char + character + after_char

def generate_treasure_map_row(width, is_3D):
    """ (int, bool) -> str
    Takes a width (width) of a new map row and if the row is
    part of a 3D map (is_3D), and returns a generated map row
    with characters featured based on different probabilities
    
    >>> random.seed(9001)
    >>> generate_treasure_map_row(10, False)
    'vv>..v>^.^'
    >>> random.seed(9001)
    >>> generate_treasure_map_row(7, True)
    'vv>.|v>'
    >>> random.seed(9001)
    >>> generate_treasure_map_row(12, False)
    'vv>..v>^.^.<'
    """
    
    row = ""
    
    move_symb_3D = random.randint(1, 2) != 2
    for i in range(width):
        move_symb = random.randint(1, 6) != 6
        empty_symb = not move_symb
        
        if move_symb:
            row += MOVEMENT_SYMBOLS[random.randint(0, 3)]
        else:
            row += EMPTY_SYMBOL
        
        
    if is_3D and move_symb_3D and width != 0:
        replace_index =  random.randint(0, width - 1)
        symbol = MOVEMENT_SYMBOLS_3D[random.randint(0, 1)]
        row = change_char_in_row(row, replace_index, symbol)
    return row

def generate_treasure_map(width, height, is_3D):
    """ (int, int, bool) -> str
    Takes a width (width) and height (height) of a new 2D map
    and if the 2D map is part of a 3D map (is_3D), and returns
    a map with characters featured based on different
    probabilities and a right movement symbol in the first index
    
    >>> random.seed(9001)
    >>> generate_treasure_map(3, 3, False)
    '>vv..v>^.'
    >>> random.seed(9001)
    >>> generate_treasure_map(1, 1, True)
    '>'
    >>> random.seed(9001)
    >>> generate_treasure_map(3, 5, True)
    '>|v>^.|.<<|.^^*'
    """
    
    map = MOVEMENT_SYMBOLS[0]
    
    map += generate_treasure_map_row(width - 1, is_3D)
    for i in range(height - 1):
        map += generate_treasure_map_row(width, is_3D)
    
    return map

def generate_3D_treasure_map(width, height, depth):
    """ (int, int, int) -> str
    Takes a width (width), height (height), and depth (depth)
    of a new 3D map, and returns a map with characters featured
    based on different probabilities and a right movement symbol
    in the first index
    
    >>> random.seed(9001)
    >>> generate_3D_treasure_map(3, 3, 3)
    '>|v>^.|.<<|.^^*|^v<vv.*v^<>'
    >>> random.seed(9001)
    >>> generate_3D_treasure_map(3, 2, 1)
    '>|v>^.'
    >>> random.seed(9001)
    >>> generate_3D_treasure_map(3, 2, 4)
    '>|v>^.|.<<|.^^*|^v<vv.*v'
    """
    
    map = generate_treasure_map(width, height, True)
    
    for depth in range(depth - 1):
       for row in range(height):
           map += generate_treasure_map_row(width, True) 
    return map

def follow_trail(map_string, s_row, s_column, s_depth, width, height, depth, tiles):
    """ (str, int, int, int, int, int, int, int) -> str
    Takes a map (map_string) with width (width), height (height),
    and depth (depth) and progresses through the map starting from
    row index (s_row), column index (s_column) and depth index
    (s_depth) according to the movement icons, placing breadcrumbs
    at each, until a breadcrumb is reached or the specified number
    of tiles (tiles) are covered (ignoring tile count if given -1),
    then printing the number of treasures collected and the number
    of tiles covered, and returning the updated map
    
    >>> follow_trail('>+v..*..<...v.<*.|vvv+v+>.|', 0, 0, 0, 3, 3, 3, -1)
    Treasures collected: 1
    Symbols visited: 15
    'X+X..X..X...X.XX.Xvvv+v+X.X'
    >>> follow_trail('>*.v|<v.+|>^|v+*^.', 0, 0, 0, 2, 3, 3, -1)
    Treasures collected: 2
    Symbols visited: 16
    'XX.XXXX.+XXXXX+XX.'
    >>> follow_trail('>+>v^..v^<+<', 2, 3, 0, 4, 3, 1, -1)
    Treasures collected: 2
    Symbols visited: 10
    'X+XXX..XXX+X'
    """
    
    tiles_moved = 0
    treasure_count = 0
    area = width*height
    
    #Initiates current 3D position index values
    cur_depth = s_depth
    cur_row = s_row
    cur_col = s_column
        
    #Checks if input is greater than possible or less than 0 (terms multiply to zero)
    exceeds_map = cur_depth >= depth or cur_row >= height or cur_col >= width
    below_first_index = cur_depth < 0 or cur_row < 0 or cur_col < 0
    if exceeds_map or below_first_index:
        return map_string
    
    #Initiates current symbol
    current_symbol = map_string[(cur_depth*area) + (cur_row*width) + cur_col]
    move_code = ""
    
    while (tiles_moved < tiles or tiles == -1) and current_symbol != BREADCRUMB_SYMBOL:
        
        if current_symbol == TREASURE_SYMBOL:
            treasure_count += 1
        
        if current_symbol in MOVEMENT_SYMBOLS or current_symbol in MOVEMENT_SYMBOLS_3D:
            move_code = current_symbol
            map_string = change_char_in_3D_map(map_string, cur_row, cur_col, cur_depth, BREADCRUMB_SYMBOL, width, height, depth)
        
        #right
        if move_code == MOVEMENT_SYMBOLS[0]:
            on_edge = cur_col + 1 == width
            if (on_edge):
                cur_col -= width - 1
            else:
                cur_col += 1
        #left
        elif move_code == MOVEMENT_SYMBOLS[1]:
            on_edge = cur_col == 0
            if (on_edge):
                cur_col += width - 1
            else:
                cur_col -= 1
        #down
        elif move_code == MOVEMENT_SYMBOLS[2]:
            on_edge = cur_row + 1 == height
            if (on_edge):
                cur_row -= height - 1
            else:
                cur_row += 1
        #up
        elif move_code == MOVEMENT_SYMBOLS[3]:
            on_edge = cur_row == 0
            if (on_edge):
                cur_row += height - 1
            else:
                cur_row -= 1 
    
        #below
        elif move_code == MOVEMENT_SYMBOLS_3D[0]:
            on_edge = cur_depth + 1 == depth
            if (on_edge):
                cur_depth -= depth - 1
            else:
                cur_depth += 1
                
        #above
        elif move_code == MOVEMENT_SYMBOLS_3D[1]:
            on_edge = cur_depth == 0
            if (on_edge):
                cur_depth += depth - 1
            else:
                cur_depth -= 1
        
        
        tiles_moved += 1
        current_symbol = map_string[(cur_depth*area) + (cur_row*width) + cur_col]
        
    print("Treasures collected: " + str(treasure_count))
    print("Symbols visited: " + str(tiles_moved))
    return map_string