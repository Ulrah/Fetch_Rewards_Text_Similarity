
# Author: Jacob Blair Morris
# Date: 05/13/2021

'''
    This code is designed to solve the following challenge:
        This challenge will focus on the similarity between two texts.
        Your objective is to write a program that takes as inputs two texts and uses a metric to determine how similar they are.
        Documents that are exactly the same should get a score of 1, and documents that don't have any words in common should get a score of 0.
    
    Considerations:
        * Do you count punctuation or only words?
            Punctuations are not specifically handled.
            Words are separated by white-space, so the string "a \n b! !" contains the words: "a", "b!", and "!".
            Also, capitalization matters, so "dog" and "Dog" are not the same.
        * Which words should matter in the similarity comparison?
            All words are considered (stop-words are not removed or handled specially)
        * Do you care about the ordering of words?
            This depends on the shingle_factor.
            If shingle_factor is 1 (bag-of-words), order does not matter.
            As shingle_factor is increased, so too is emphasis on ordering of words.
            Also, choices on capitalization and punctuation place greater emphasis on order.
        * What metric do you use to assign a numerical value to the similarity?
            This solution uses Jaccard Similarity Index/Distance (with optional shingling).
            I was exposed to this method during school, but also refreshed on it using the following resource:
                https://www.cs.utah.edu/~jeffp/teaching/cs5955/L4-Jaccard+Shingle.pdf
        * What type of data structures should be used?
            The primary data structure used in this implementation is the set,
            but list (here) and dictionary (in text_compare_example.py) also used.
'''


import sys


'''
    Text_Compare:
        Creates object that can be used to compare supplied base-text with other texts.
        Comparisons use Jiccard Similarity with optional Shingling (shingle_factor = 1 for bag-of-words approach).
        Higher values of shingle_factor place greater emphasis on order of words.
        For reference:
            https://www.cs.utah.edu/~jeffp/teaching/cs5955/L4-Jaccard+Shingle.pdf
'''
class Text_Compare :

    # warning: object attributes should not be modified after creation
    def __init__( self, base_text, shingle_factor = 1 ) :
        self.__shingle_factor = shingle_factor
        self.__set = self.__shingle_text( base_text )

    # private method to shingle a string (returns shingled set)
    def __shingle_text( self, text ) :
        if 1 >= self.__shingle_factor :
            shingled_set = set( text.split( ) )
        else :
            shingled_set = set( )
            words = text.split( )
            for i in range( len( words ) - self.__shingle_factor + 1 ) :
                shingled_set.add( ' '.join( words[ i : i + self.__shingle_factor ] ) )
            
        return shingled_set

    # returns Jaccard Similarity between base_text and compare_text (using self.shingle_factor), or -1 if union_count = 0
    def compare( self, compare_text ) :
        compare_set = self.__shingle_text( compare_text )
        intersection_count = len( self.__set & compare_set )
        union_count = len( self.__set | compare_set )
        if 0 != union_count :
            similarity = float( intersection_count ) / float( union_count )
        else :
            similarity = -1.0
        
        return similarity


'''
    Entry point for program.
    Expected format for arguments (shingle_factor optional):
        python3 text_compare.py <text_file_path> <text_file_path> <shingle_factor>
'''
def main( ) :
    
    # get texts from files
    with open( sys.argv[1] ) as file :
        text_1 = file.read( )
    with open( sys.argv[2] ) as file :
        text_2 = file.read( )
    
    # if present, get shingle_factor
    if len( sys.argv ) > 3 :
        shingle_factor = int( sys.argv[3] )
    else :
        shingle_factor = 1
    print( "shingle factor: " + str( shingle_factor ) )
    
    # get and print similarity
    base_text = Text_Compare( text_1, shingle_factor = shingle_factor )
    similarity = base_text.compare( text_2 )
    print( "The Jaccard Similarity between " + sys.argv[1] + " and " + sys.argv[2] + " : " + str( similarity ) )


if __name__ == "__main__" :
    main( )
