import os
from random import randrange, sample
import json
from time import sleep

class Hangman:

    def __init__(self):
       self._hangmanSet = ['0','|', '/', '\\', '/', '\\']
       self._hangman = [' ',' ', ' ', ' ', ' ', ' ']
       self._word_list =[]
       self._word = ""
       self._guess = []
       self._tries = 0
       self._stage =1
       self.main()

    def main(self):
        self._word_list = self.load_json()

        self.select_word()
        self.display()
        
        while self._tries <= 5:
            found= False
            inp = input("Enter letter: ")
            for i,x in enumerate(self._word):
                if(x == inp ):
                    self._guess[i]=inp
                    found = True
            
            if found ==False:
                self._hangman[self._tries] = self._hangmanSet[self._tries]
                self._tries +=1
            
            if self.is_solved():
                if self._stage == 5:
                    self._word_list = self.load_json('normal')
                elif self._stage == 9:
                    self._tries = 6
                    self.quit()

                self.is_continue()
                self.select_word()
                self.display()

            else:
                self.display()
        
            if self._tries > 5:
                restart = self.restart()
                if restart:
                    self._tries = 0
                    self.select_word()
                    self.display()
                else:
                    self.quit()
    
    def load_json(self, difficulty ='easy')->list:
        with open('dictionary.json') as json_data:
            data = json.load(json_data)
            json_data.close()
            lst = data[difficulty]
            return sample(lst, 5)

    def select_word(self)->None:
        self._word = self._word_list.pop()
        self.word_guess()

    def is_solved(self)->bool:
        return False if '_' in self._guess else True
    
    def word_guess(self)->None:
        x = randrange(len(self._word))
        ltr = self._word[x]
        ctr=0
        for i in self._word:
            self._guess.append( i if i== ltr  else '_')
            ctr+=1
        
    def display(self)->None:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Stage {self._stage}:")
        print("----------")
        print(f"|    |    |")
        print(f"|    {self._hangman[0]}    |")
        print(f"|   {self._hangman[2]}{self._hangman[1]}{self._hangman[3]}   |")
        print(f"|   {self._hangman[4]} {self._hangman[5]}   |")
        print(f"----------")     
        print(f"\nGuess the word:\n")
        print(' '.join(self._guess))
        print(f"\n")

    def is_continue(self)->None:
        countDown = 5
        self._tries =0
        self._stage += 1
        self._guess = []
        self._hangman = [' ',' ', ' ', ' ', ' ', ' ']
        while countDown > 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\nStage {self._stage}:\n")
            print("Congratulation!!!\nYou solved the puzzle\n\n")
            print(f"Next word will be ready in: {countDown}")
            countDown -=1
            sleep(1)


    def restart(self)->bool:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\nStage {self._stage}:\n")
        self._guess = []
        self._hangman = [' ',' ', ' ', ' ', ' ', ' ']
        nextPuzzle = True
        while nextPuzzle:
            inp = input(f"\nWould you like to restart?: [y/n]\n")
            if inp == 'y':
                return True

            elif inp =='n':
                return False
            else:
                print("Please enter 'y' or 'n ")

    def quit(self)->None:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nThank you for playing!\n\nGood Bye!!!\n\n")

hangman = Hangman()

