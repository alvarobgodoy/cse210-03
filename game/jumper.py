'''2. Jumper: 
> self._jumper = list, each element contains one line of the jumper (9 elements in total)
> take_life() = takes one life away from the jumper (deletes the first element from the list _jumper), 
    if _jumper length is 6 then it sets _jumper as the death one (the head is an "x"), then returns it.
> get_jumper() = returns _jumper
> is_alive() = returns true if _jumper has enough lives.

'''


class Jumper:
    '''this is the class of the Jumper where the little
    person is in risk to die if the user doesn't guess with 
    the funny game 
    Attributes:    
        _jumper (list): the parts of the little man.


    '''
    
    def __init__(self):
        ''' Constructs a new Jumper 
        
        Args:
            self (Jumper): creates a new instance of the class Jumper

        '''
        
        
        self._jumper = [    
            '    ___     ',
            '   /___\    ',
            '   \   /    ',
            '    \ /     ',
            '     O      ',
            '    /|\     ',
            '    / \     ',
            '            ',
            '  ^^^^^^^   ' 
        ]  # this is the list of the little man
        self._boolean_value = True  # this is the boolean value that allows says the man to be alive


    def take_life(self):
        ''' Deletes the first letter from the list jumper parameter: 
        Args:
            self (Jumper): An instance of Jumper
        
        '''

        self._jumper.pop(0)  # each time the take_life() is called it pops the first element of the list
        if len(self._jumper) == 5:     # conditional if the little man doesn't have any rope
            self._jumper[0] = '     x      '   # and add the cross in the head... 
            self._boolean_value = False   #  Remember the boolean value...? here is the response if the list has only four left

    def get_jumper(self):
        '''Simply returns the list of the jumper to 
        make it print in with the display class methods

        Args:
            self (Jumper): An instance of Jumper

        Returns:
            list: The list of the draw of the little man
        '''

        return self._jumper   


    def is_alive(self):
        '''returns that the little man
        is alive
        Args:
            self (Jumper): An instance of Jumper

        Returns:
            boolean: the value true if there is a certain amount of items in the list

        '''

        does_live = self._boolean_value
        return does_live      # simply returns the value of the boolean value each time the is_alive method... If the jumper is alive or dead



