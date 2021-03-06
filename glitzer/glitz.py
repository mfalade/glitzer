"""
    This is just a silly function that prints an easily customizable line ontop and below whatever string you pass to it.
    Could be useful when you want to lay emphasis on what you want to print.
"""

def glitz(string, border='.', num_borders=1, padding=1):
    _num_borders = 1 if num_borders < 1 else num_borders
    _padding = 1 if padding < 1 else padding
    
    if type(str) == 'str':
        border_length = len(string) + (_padding * 2)
    else:
        border_length = 10
        
    
    for i in range(_num_borders):
        print(border * border_length)
    
    output_string = '{padding}{string}{padding}'.format(string=string, padding=(' ' * _padding))
    print(output_string)

    for i in range(_num_borders):
        print(border * border_length)
