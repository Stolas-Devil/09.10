class Alphabet:
    """алфавит"""
    def __init__(self, lang, letters): #lang - язык
        self.lang = lang
        self.letters = letters
   
    def print(self):
        print(self.letters)    

    def letters_num(self):
        print(len(self.letters))

class  EngAlphabet(Alphabet):
    """анг алфавит"""
    def __init__(self):
        super().__init__(En, list(string.ascii_uppercase) )

    @property
    def letters_num(self): 
        self.__letters_num

    def is_en_letter(self, let): 
         print(let in self.letters) 

    @staticmethod 
    def example(): 
         print('Englih text')

 
def main(): 
    eng = EngAlphabet() 
    eng.print() 
    print(eng.letters_num) 
    eng.is_en_letter("F") 
    eng.is_en_letter("Щ") 
    print("English Example:") 
    EngAlphabet.example()

 
if __name__ == "__main__": 
    main()