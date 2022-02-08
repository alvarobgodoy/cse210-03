guessed_letter = []
shots = 5

class Display:
    
    """The display provides the output for the jumper game"""
    def print_jumper(jumper): #Prints the jumper according to the quantity of attempts remaining.
        if shots == 5:
            print("""
                    _____
                   /_____\
                   \     /
                    \   /
                     \_/
                      O
                     /|\
                     / \

                    ^^^^^^
            """)

        if shots == 4:
            print("""
                    
                   /_____\
                   \     /
                    \   /
                     \_/
                      O
                     /|\
                     / \
                          
                    ^^^^^^
            """)
        
        if shots == 3:
            print("""

                   ______
                   \     /
                    \   /
                     \_/
                      O
                     /|\
                     / \
                          
                    ^^^^^^
            """)
        
        if shots == 2:
            print("""

                    \   /
                     \_/
                      O
                     /|\
                     / \

                    ^^^^^^
            """)

        if shots == 1:
            print("""

                     \_/
                      O
                     /|\
                     / \

                    ^^^^^^
            
            
            """)
        if shots == 0:
            print("""

                     \ 0 /
                       |
                      / \    

                    ^^^^^^
            
            
            """)


    def get_letter(letter): #Prints the message to get a letter from the user.
        letter = input("Please, write a letter to guess the secret word: ")
        return letter

    def print_word_so_far(word, guessed_letter): #uses a loop to display a word, 
        #for every letter in word if that letter is also in guessed_letters then it gets printed, 
        # if not a ‘_’ is printed in its place.
        for letter in word:
            if letter == guessed_letter:
                print(letter)
            elif letter not in guessed_letter:
                print("_") 
            else:
                print("You have chosen that letter already!")
        

