# Dominic Reen
# SDEV 220
# SDEV 220 Final Project - Game: hangman
# Due May 12th

from tkinter import * # Import tkinter
import random # import random

class Hangman:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Hangman") # Set title

        width = 600
        height = 400
        radius = 2
        self.canvas = Canvas(window, width = width, height = height)
        self.canvas.pack()

        self.frame = Frame(window)
        self.frame.pack()

        # Receive key input
        self.canvas.bind("<Key>", self.processKeyEvent)
        self.canvas.focus_set()

        guessedLetter = "" # Empty letter that will be accessed globally

        self.setUpGame()

        window.mainloop() # Create an event loop

    def setUpGame(self):
        # Clear the screen
        self.canvas.delete("gallows", "titleText", "word", "youWon", "missingText", "youLost") # delete words
        self.canvas.delete("head", "torso", "leftLeg", "rightLeg", "leftArm", "rightArm") # Delete man
        
        # Draw the hangman gallows
        self.canvas.create_line(50, 50, 50, 350, tags = "gallows")
        self.canvas.create_line(10, 350, 200, 350, tags = "gallows")
        self.canvas.create_line(50, 300, 100, 350, tags = "gallows")
        self.canvas.create_line(50, 50, 200, 50, tags = "gallows")
        self.canvas.create_line(200, 50, 200, 75, tags = "gallows")

        # Create list of words
        answerList = ["young", "weak", "close", "poetry",
                      "tired", "tooth", "flow", "lunch",
                      "studio", "leaf", "treat", "wood",
                      "beach", "chest", "coffee", "truck",
                      "arena", "berry", "jewel", "guide",
                      "winner", "torch", "motif", "black",
                      "lady", "faith", "noble", "coin", "recipe",
                      "knife"]
        
        # Shuffle the words
        random.shuffle(answerList)

        # Then use the first word as our answer, and convert it to a list
        self.answerWord = list(answerList[0])

        self.guessed = [] # Empty list to hold guessed numbers

        self.displayList = [] # List of letters to display

        self.displayList.extend(self.answerWord) # Puts the answer word into the variable to display

        self.count = 5 # Number of possible wrong guesses

        #guessed.extend(displayList) # Add letters so we can take them out

        # Turn all the letters in displayList into asterisks
        for i in range (len(self.displayList)):
            self.displayList[i] = "*" 

        # Display text
        self.canvas.create_text(350, 300, text = "Guess a word: ", font = ("Times", 16, "normal"), tags = "titleText")
        self.canvas.create_text(450, 300, text = self.displayList, font = ("Times", 16, "normal"), tags = "word")
        
        ''' UN-COMMENT THIS TO SEE WHAT THE WORD IS!!! '''
        #self.canvas.create_text(430, 250, text = self.answerWord, font = ("Times", 16, "normal"), tags = "word")
        

    def playGame(self, letter):
        correctWasGuessed = False
        if (self.count < 1):
            self.displayBodyPart(self.count) # Display last piece
            self.canvas.delete("missingText", "titleText", "word") # Clear words
            self.canvas.bind("<Key>", self.processKeyGameOver) # Stop player from entering anything other than ENTER
            self.canvas.create_text(300, 200, text = "You Lost!", font = ("Times", 50, "normal"), tags = "youLost")
            self.canvas.create_text(300, 250, text = "The word is: ", font = ("Times", 16, "normal"), tags = "youLost")
            self.canvas.create_text(400, 250, text = self.answerWord, font = ("Times", 16, "normal"), tags = "youLost")
            self.canvas.create_text(430, 300, text = "To continue the game, press ENTER", font = ("Times", 16, "normal"), tags = "youWon")
            return
            
        for i in range(len(self.answerWord)):
            # First check if the user has already incorrectly guessed the letter
            if (letter in self.guessed):
                return
            if (letter == self.answerWord[i]):
                self.displayList[i] = self.answerWord[i]
                # Update displayList
                self.canvas.delete("word")
                self.canvas.create_text(450, 300, text = self.displayList, font = ("Times", 16, "normal"), tags = "word")
                correctWasGuessed = True

                # Check if the whole word is guessed yet
                if (self.displayList == self.answerWord):
                    self.canvas.delete("missingText", "titleText", "word")
                    self.canvas.bind("<Key>", self.processKeyGameOver) # Stop player from entering anything other than ENTER
                    self.canvas.create_text(300, 200, text = "You Won!", font = ("Times", 50, "normal"), tags = "youWon")
                    self.canvas.create_text(430, 300, text = "To continue the game, press ENTER", font = ("Times", 16, "normal"), tags = "youWon")
                    return
                else:
                    continue
            else:
                continue
            
        if (not correctWasGuessed):
            # Display next piece of man
            self.displayBodyPart(self.count)
            
            self.count -= 1 # Wrong letter was guessed
            self.guessed.extend(letter) # Add wrong letter to list

            self.canvas.delete("text", "missingText") # Clear the words
            # Display updated text
            self.canvas.create_text(350, 320, text = "Missed letters: ", font = ("Times", 16, "normal"), tags = "missingText")
            self.canvas.create_text(450, 320, text = self.guessed, font = ("Times", 16, "normal"), tags = "missingText")
        return
            
            
    # Get guessed letter
    def processKeyEvent(self, event):
        self.playGame(event.char)

    # Get ENTER key pressed
    def processKeyGameOver(self, event):
        print(event.keycode)
        if (event.keycode == 13):
            self.canvas.bind("<Key>", self.processKeyEvent) # Let player from enter anything again
            self.setUpGame() # Start a new game
        else:
            return
        
        
    def displayBodyPart(self, count):
        # Depending on what the count is, display corresponding body part
        if (count == 5): # Dusplay head
            self.canvas.create_oval(175, 75, 225, 125, tags = "head")
        elif (count == 4): # Dusplay torso
            self.canvas.create_line(200, 125, 200, 250, tags = "torso")
        elif (count == 3): # Dusplay left leg
            self.canvas.create_line(200, 250, 150, 300, tags = "leftLeg")
        elif (count == 2): # Dusplay right leg
            self.canvas.create_line(200, 250, 250, 300, tags = "rightLeg")
        elif (count == 1): # Dusplay left arm
            self.canvas.create_line(200, 175, 150, 125, tags = "leftArm")
        elif (count == 0): # Dusplay right arm
            self.canvas.create_line(200, 175, 250, 125, tags = "rightArm")
            


Hangman() # Create GUI
