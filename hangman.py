##  ==========================================================================================================
##  Michael Beach
##  hangman-mgb.py

##  This assignment was designed to test our ability to integrate all we've learned so far in creating
##  a game of hangman with graphical interface

##  All the images were created by me and can be freely distributed or reused with attribution
##  ==========================================================================================================

from random import randint
from graphics import *

##  ==========================================================================================================

def getList():

    infile   = open("wordlist.txt", 'r')
    wordlist = infile.readlines()
    infile.close()
    
    return wordlist

##  ==========================================================================================================
    
def getWord():

    wordlist   = getList() 
    randomNum  = randint(0, (len(wordlist) - 1))
    chosenWord = wordlist[randomNum].replace('\n', '')

    secretWord = ""
    
    for letter in chosenWord:
        letter = letter.upper()
        secretWord = secretWord + letter
        
    return secretWord

##  ==========================================================================================================

def dispBlanks(secretWord):

    wordBlanks = []
		
    for letter in range (len(secretWord)):
        
        wordBlanks.append(chr(8226))
        
    wordBlanks = ''.join(wordBlanks)

    return wordBlanks

##  ==========================================================================================================

def drawSegment(strikes, win):

    segmentsAnchor = Point(25,50)

##  Associates each image with the number of strikes it represents

    state0   = Image(segmentsAnchor, '0.gif')
    state1   = Image(segmentsAnchor, '1.gif')
    state2   = Image(segmentsAnchor, '2.gif')
    state3   = Image(segmentsAnchor, '3.gif')
    state4   = Image(segmentsAnchor, '4.gif')
    state5   = Image(segmentsAnchor, '5.gif')
    state6   = Image(segmentsAnchor, '6.gif')
    state7   = Image(segmentsAnchor, '7.gif')
    state8   = Image(segmentsAnchor, '8.gif')

    if strikes == 0:
        state0.draw(win)

    elif strikes == 1:
        state1.draw(win)

    elif strikes == 2:
        state2.draw(win)

    elif strikes == 3:
        state3.draw(win)

    elif strikes == 4:
        state4.draw(win)

    elif strikes == 5:
        state5.draw(win)

    elif strikes == 6:
        state6.draw(win)

    elif strikes == 7:
        state7.draw(win)

    elif strikes == 8:
        state8.draw(win)
    
##  ==============================================================
        
def newGame(win):
    
    # Pick secret word from list and display blanks for each letter
    secretWord = getWord()
    wordBlanks = dispBlanks(secretWord)

##  ===================    
##      CONSTANTS     
##  ===================
    WIDTH  = 1000
    HEIGHT = 500
    CENTER = Point(75,50)
    FONT1  = 'helvetica'
    FONT2  = 'courier'
    LIGHTBLUE = color_rgb(0, 128, 255)
    DARKBLUE  = color_rgb(0, 30, 50)
    YELLOW    = color_rgb(255,170,0)
    DARKRED   = color_rgb(170, 0, 0)
    GREEN     = color_rgb(0, 80, 0)
    LTGREEN   = color_rgb(0, 200, 0)

##  Create window for graphical interface. Checks to see if it's the first time playing or not,
##  so that new windows don't open every time the user decides to play again
    if not(win):
        win = GraphWin("Hangman", WIDTH, HEIGHT)
        win.setBackground('black')
        win.setCoords(0,0,100,100)

##  Loads the image of just the gallows
    drawSegment(0, win)
    
##  Draw blanks for chosen word
    guiBlanks = Text(CENTER, wordBlanks)
    guiBlanks.setSize(36)
    guiBlanks.setStyle('bold')
    guiBlanks.setFace(FONT2)
    guiBlanks.setFill(YELLOW)
    guiBlanks.draw(win)  

##  Draw Used Letters text
    guiUsed = Text(Point(75, 94), 'Used Letters')
    guiUsed.setSize(18)
    guiUsed.setStyle('bold')
    guiUsed.setFill(LIGHTBLUE)
    guiUsed.draw(win)

    guiUsedNone = Text(Point(75,85), 'NONE')
    guiUsedNone.setFill(YELLOW)
    guiUsedNone.setSize(20)
    guiUsedNone.setFace(FONT1)
    guiUsedNone.setStyle('bold')
    guiUsedNone.draw(win)

##  Draw placeholder for messages to the player
    guiMessage = Text(Point(75, 40), 'Good luck!')
    guiMessage.setSize(20)
    guiMessage.setStyle('bold')
    guiMessage.setFill(LIGHTBLUE)
    guiMessage.draw(win)

##  Draw entry box, GUESS button, and text label
    guiGuessEntry = Entry(Point(68, 15), 2)
    guiGuessEntry.setSize(30)
    guiGuessEntry.setStyle('bold')
    guiGuessEntry.setFill(LIGHTBLUE)
    guiGuessEntry.draw(win)
    guiGuessEntry.setText('')
    
    guiGuessButton = Rectangle(Point(71, 10), Point(83, 20))
    guiGuessButton.setFill(DARKBLUE)
    guiGuessButton.setOutline(LIGHTBLUE)
    guiGuessButton.draw(win)
    
    guiGuessLabel = Text(guiGuessButton.getCenter(), 'GUESS')
    guiGuessLabel.setSize(23)
    guiGuessLabel.setStyle('bold')
    guiGuessLabel.setFill(LIGHTBLUE)
    guiGuessLabel.draw(win)

##  Draw " guesses left".. the number is calculated and displayed further down in the code
    guiGuessLeft = Text(Point(75, 5), ' guesses left')
    guiGuessLeft.setSize(17)
    guiGuessLeft.setStyle('bold')
    guiGuessLeft.setFill(LIGHTBLUE)
    guiGuessLeft.draw(win)
 
    validChoices = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
                    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    guessedList  = []
    
    strikes = 0 
    isWinner = False

    
    
    while strikes < 7 and isWinner == False:

##      guessedList is joined into a string of usedLetters and displayed in the center of the screen
        guessedList.sort()
        usedLettersString = ' '.join(guessedList)
        usedLetters = Text(Point(75,85), usedLettersString)
        usedLetters.setFill(YELLOW)
        usedLetters.setFace(FONT1)
        usedLetters.setSize(25)
        usedLetters.setStyle('bold')
        usedLetters.draw(win)

##      Number of guesses left calculated and displayed
        guessesLeft = 7 - strikes
        guiNumLeft = Text(Point(67, 5), guessesLeft)
        guiNumLeft.setSize(17)
        guiNumLeft.setStyle('bold')
        guiNumLeft.setFill(LIGHTBLUE)
        guiNumLeft.draw(win)

        

##      Waits until mouse is clicked and checks to make sure it was within the GUESS button's rectangle
        guessClicked = False
        while not(guessClicked):

            click = win.getMouse()
            if guiGuessButton.getP1().getX() <= click.getX() <= guiGuessButton.getP2().getX() and guiGuessButton.getP1().getY() <= click.getY() <= guiGuessButton.getP2().getY():
                guessClicked = 2

        guessedLetter = guiGuessEntry.getText().upper()
        guiGuessEntry.setText('')

##      clear number of guesses left and used letters displays so they can be updated
        guiNumLeft.undraw()
        guiUsedNone.undraw()
        usedLetters.undraw()


##      GATEKEEPER: Just loops back up to "while strikes < 7 and isWinner == False" if space, null, or a multiple-character guess is made
        if not (guessedLetter in validChoices) or guessedLetter == ' ' or guessedLetter == '' or len(guessedLetter) != 1:
            continue
            

##      CORRECT GUESSES that are NOT ALREADY GUESSED are first added to the guessedList... 
        if guessedLetter in secretWord and not (guessedLetter in guessedList):         
            guessedList.append(guessedLetter)
            
            
##          ...then goes into the loop where it sets wordBlanks equal to secretWord, so there are no underscores left. Then for each letter 
##          in wordBlanks it looks to see if that letter has been guessed yet (ie, is in guessedList). If not, it replaces that letter with
##          an underscore again. Once finished, the display is updated and any of the word's letters that have been guessed are revealed. 
            wordBlanks = secretWord
            for letter in secretWord:
                if (not (letter in secretWord) or not(letter in guessedList)) and letter != ' ':
                    wordBlanks = wordBlanks.replace(letter, chr(8226))
                
                guiBlanks.setText(wordBlanks)
                    
                    
                    
##          after that operation, if wordBlanks == secretWord then no letters were replaced with underscores. That means the player
##          has guessed all the correct letters, and is a WINNER
            if wordBlanks == secretWord:
                isWinner = True
                
##          since player didn't win, they must have made a correct guess. Display is updated.
            else:
                guiMessage.setText("Great! {0} is in the word. Keep it up.".format(guessedLetter))
                guiMessage.setFill(GREEN)

##      ALREADY GUESSED notification display        
        elif guessedLetter in guessedList:
            guiMessage.setText("You've already guessed {0}.".format(guessedLetter))
            guiMessage.setFill(YELLOW)

##      WRONG! notification display. Also ADD 1 STRIKE, update guessedList with guess, and CHANGE HANGMAN IMAGE
        else:
            guessedList.append(guessedLetter)
            strikes = strikes + 1
            guiMessage.setText("Sorry, {0} isn't in the word.".format(guessedLetter))
            guiMessage.setFill(DARKRED)
            drawSegment(strikes, win)

##  =========================
##          GAME OVER          
##  =========================
    
##  Reveal secretWord
    guiBlanks.setText(secretWord)
    guiBlanks.setStyle('bold')
    guiBlanks.setSize(36)
    guiBlanks.move(0,30)
    guiBlanks.setFace(FONT1)
    guiWordWas = guiBlanks.clone()
    guiWordWas.setText('The secret word was:')
    guiWordWas.setSize(22)
    guiWordWas.setFill(YELLOW)
    guiWordWas.draw(win)
    guiWordWas.move(0,10)
    


##  Show PLAY button
    usedLetters.undraw()
    guiPlay = Rectangle(Point(58, 40), Point(73, 60))
    guiPlay.setFill(GREEN)
    guiPlay.draw(win)
    
    guiPlayText = Text(guiPlay.getCenter(), 'PLAY')
    guiPlayText.setFill(YELLOW)
    guiPlayText.setSize(20)
    guiPlayText.setStyle('bold')
    guiPlayText.draw(win)

##  Show QUIT button
    guiUsed.undraw()
    guiQuit = Rectangle(Point(78,40), Point(93, 60))
    guiQuit.setFill(DARKRED)
    guiQuit.draw(win)
    
    guiQuitText = Text(guiQuit.getCenter(), 'QUIT')
    guiQuitText.setFill(YELLOW)
    guiQuitText.setSize(20)
    guiQuitText.setStyle('bold')
    guiQuitText.draw(win)

##  UPDATE DISPLAY TO REFLECT WIN
    if isWinner == True:
        guiMessage.setText("You earned a stay of execution!")
        guiMessage.setFace(FONT1)
        guiMessage.setFill(GREEN)
        guiBlanks.setFill(GREEN)
        guiMessage.move(0,-23)
        drawSegment(8, win)
        

##      UNDRAW UNNEEDED OBJECTS
        guiGuessLeft.undraw()
        usedLetters.undraw()
        guiNumLeft.undraw()
        guiGuessButton.undraw()
        guiGuessEntry.undraw()
        guiGuessLabel.undraw()

##  UPDATE DISPLAY TO REFLECT LOSS       
    else:
        guiMessage.setText("You have been hanged.")
        guiMessage.setFace(FONT1)
        guiMessage.setFill(DARKRED)
        guiBlanks.setFill(DARKRED)
        guiMessage.move(0,-23)
        guiNumLeft.setText('0')

##      UNDRAW UNNEEDED OBJECTS        
        guiNumLeft.undraw()
        usedLetters.undraw()
        guiGuessLeft.undraw()
        guiGuessButton.undraw()
        guiGuessEntry.undraw()
        guiGuessLabel.undraw()
    

##  Wait for PLAY or QUIT to be selected by the player...
    
    selectionMade = False
    while not(selectionMade):
            selPoint = win.getMouse()

##          PLAY AGAIN
            if  guiPlay.getP1().getX() <= selPoint.getX() <= guiPlay.getP2().getX() and guiPlay.getP1().getY() <= selPoint.getY() <= guiPlay.getP2().getY():

##              Undraw all graphics objects from this game and call another instance of the game
                guiObjects = [guiMessage, guiBlanks, guiPlay, guiPlayText, guiQuit, guiQuitText, guiNumLeft, guiWordWas,
                              usedLetters, guiGuessEntry, guiNumLeft, guiGuessLabel, guiGuessLeft, guiGuessButton]
                for entry in guiObjects:
                    entry.undraw()

                newGame(win)

##          QUIT GAME
            elif guiQuit.getP1().getX() <= selPoint.getX() <= guiQuit.getP2().getX():
                
                win.close()

##  ==============================================================
                
def main():

    newGame(False)

##  ==============================================================
    
main()
