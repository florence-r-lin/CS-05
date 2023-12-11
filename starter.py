#
# textmodel.py
#
# TextModel project!
#
# Name(s): Florence Lin and Annette Chang
#

import string 


class TextModel:
    """A class supporting complex models of text."""

    def __init__(self):
        """Create an empty TextModel."""
        # 
        # The text in the model, all in a single string--the original
        # and "cleaned" versions.
        #
        self.text = ''            # No text present yet
        self.cleanedtext = ''     # Nor any cleaned text yet
                                  # ..(cleaned == only letters, all lowercase)

        #
        # Create dictionaries for each characteristic
        #
        self.words = {}           # For counting words
        self.wordlengths = {}     # For counting word lengths
        self.stems = {}           # For counting stems
        self.sentencelengths = {} # For counting sentence lengths

        # Create another dictionary of your own
        #
        self.myparameter = {}     # For counting ___________

    def __repr__(self):
        """Display the contents of a TextModel."""
        s = f'Words:\n{str(self.words)}\n\n'
        s += f'Word lengths:\n{str(self.wordlengths)}\n\n'
        s += f'Stems:\n{str(self.stems)}\n\n'
        s += f'Sentence lengths:\n{str(self.sentencelengths)}\n\n'
        s += f'MY PARAMETER:\n{str(self.myparameter)}\n\n'
        s += '+'*55 + '\n'
        s += f'Text[:42]    {self.text[:len(self.text)]}\n'
        s += f'Cleaned[:42] {self.cleanedtext[:len(self.cleanedtext)]}\n'
        s += '+'*55 + '\n\n'
        return s

    # We provide two text-adding methods (functions) here:
    def addRawText(self, text):
        """addRawText accepts self (the object itself)
                      and text, a string of raw text to add.
           Nothing is returned from this method, but
           the text _is_ added.
        """
        self.text += text 
        self.cleanedtext += self.cleanString(self.text) 

    # The second one adds text from a file:
    def addFileText(self, filename):
        """addFileText accepts a filename.

           Nothing is returned from this method, but
           the file is opened and its text _is_ added.

           If the file is not present, it will crash!
        """
        f = open(filename, 'r', encoding='latin1')
                               # The above may need utf-8 or utf-16, depending
        text = f.read()        # Read all of the contents into text 
        f.close()              # Close the file
        self.addRawText(text)  # Uses the previous method!

    # Include other functions here.
    # In particular, you'll need functions that add to the model.

    def makeSentenceLengths(self):
        """Creates the dictionary of sentence lengths
               should use self.text, because it needs the punctuation!
        """
          
        LoW = self.text.split()
        count = 0
        for i in LoW:
            count += 1
            if i[-1] in '.?!':
              if count in self.sentencelengths:
                self.sentencelengths[count] += 1
              else: 
                self.sentencelengths[count] = 1 
              count = 0
            


    def cleanString(self, s):
        """Returns the string s, but
           with only ASCII characters, only lowercase, and no punctuation.
           See the description and hints in the problem!
        """
        s = s.encode("ascii", "ignore")   # Ignores non-ASCII characters
        s = s.decode()       
      
        result = s.lower()  # converts to lowercase 
      
        for p in string.punctuation: # gets rid of punctuation
          result = result.replace(p, " ")
        
        return result
    
          

    def makeWordLengths(self):
      """creates the dictionary of word-length features using
          self.cleanedtext
      """
      

  
    def normalizeDictionary(self, d):
      """accepts any model dictionary D and returns a normalized version
      """


    def smallestValue(self, nd1, nd2):
      """accepts two model dictionaries and returns the smallest positive 
        value across them both
      """

    def compareDictionaries(self, d, nd1, nd2):
      """
      """

    def createAllDictionaries(self):
      """Create out all five of self's
         dictionaries in full.
      """
      self.makeSentenceLengths()
      self.makeWords()
      self.makeStems()
      self.makeWordLengths()
      self.makePunctuation()


    def compareTextWithTwoModels(self, model1, model2):
      """runs compareDictionaries for each feature dictionaries in self   
          against corresponding dictionaries
      """



# And let's test things out here...
TMintro = TextModel()

# Add a call that puts information into the model
TMintro.addRawText("""This is a small sentence. This isn't a small
sentence, because this sentence contains more than 10 words and a
number! This isn't a question, is it?""")

# Put the above triple-quoted string into a file named test.txt, then run this:
#  TMintro.addFileText("test.txt")   # "comment in" this line, once the file is created

# Print it out
print("TMintro is", TMintro)


# Add more calls - and more models - here:
