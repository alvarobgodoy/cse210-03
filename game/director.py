from game.display import Display
from game.jumper import Jumper
from game.word import Word

class Director:
    '''Someone who controls the game. 
    
    His responsability is to make decisions during the game.

    Attributes:
        _jumper (Jumper): The game's Jumper.
        _word (Word): Manage of the words in the game.
        _display (Display): Controls the terminal (displays things, asks it, etc).
        _user_letter (string): The letter that the user guesses each round.
        _ran_word (string): The random word chosen by Word.
        _guessed_letters (string): All the letters that the user guessed (so far).
        _keep_playing (boolean): Wheter the game continues or not.
    '''
    
    def __init__(self):
        self._jumper = Jumper()
        self._word = Word()
        self._display = Display()
        self._user_letter = ''
        self._ran_word = self._word.get_random_word().lower()
        self._guessed_letters = ''
        self._is_alive = True

    def start_game(self):
        '''Contains the main loop used to start the game.
        
        Args:
            self (Director): an instance of Director.
        '''
        self._do_outputs()
        while self._is_alive:
            self._do_inputs()
            self._do_updates()  
            self._do_outputs()

    def _do_updates(self):
        if self._user_letter.lower() in self._ran_word:
            # User guesses the letter and that is added to the _guessed_letters string
            for i in self._ran_word:
                if i == self._user_letter:
                    self._guessed_letters += self._user_letter
        else:
            # User missed that letter, a life is taken from the jumper
            self._jumper.take_life()

        if sorted(self._ran_word) == sorted(self._guessed_letters):
            # Player guesses the entire word, wons the game
            self._is_alive = False
        if not self._jumper.is_alive():
            # If the jumper is dead the game ends. Player losses
            self._is_alive = False        

    def _do_outputs(self):
        self._display.print_word_so_far(self._ran_word, self._guessed_letters)
        self._display.print_jumper(self._jumper.get_jumper())

    def _do_inputs(self):
        self._user_letter = self._display.get_letter('Guess a letter [a-z]: ')