# Ex 25: Even More Practice

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints sthe first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

"""

Press ENTER or type command to continue
Python 2.7.11 (default, Feb 14 2016, 01:07:15) 
[GCC 4.4.5] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import ex25
>>> sentence = "All good things come to those who wait."
>>> words = ex25.break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
>>> sorted_words = ex25.sorted_words(words)
Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      AttributeError: 'module' object has no attribute 'sorted_words'
      >>> sorted_words = ex25.sort_words(words)
      >>> sorted_words
      ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
      >>> ex25.print_first_and_last(sentence)
      All
      wait.
      >>> ex25.print_first_and_last_sorted(sentence)
      All
      who
      >>> 
      Press ENTER or type command to continue
      Python 2.7.11 (default, Feb 14 2016, 01:07:15) 
      [GCC 4.4.5] on linux2
      Type "help", "copyright", "credits" or "license" for more information.
      >>> import ex25
      >>> sentence = "All good things come to those who wait."
      >>> words = ex25.break_words(sentence)
      >>> words
      ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
      >>> sorted_words = ex25.sorted_words(words)
      Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      AttributeError: 'module' object has no attribute 'sorted_words'
      >>> sorted_words = ex25.sort_words(words)
      >>> sorted_words
      ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
      >>> ex25.print_first_and_last(sentence)
      All
      wait.
      >>> ex25.print_first_and_last_sorted(sentence)
      All
      who
      >>> 
"""
