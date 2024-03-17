# Take a word and add a prefix to form a new word
def add_prefix_un(word):
    prefixed_word = "un" + word
    return prefixed_word


""" Take a list in the form of ['prefix', 'word1','word2'...'wordn'] and\
   form a list of prefixed words. """
def make_word_groups(vocab_words:list):
    output = f"{vocab_words[0]}"
    for index in range(1,len(vocab_words)):
        output += f" :: {vocab_words[0]}{vocab_words[index]}"
    return output

    
# Remove the "ness" suffix and restore it to the root word if needed.
def remove_suffix_ness(word):
    if word.endswith("ness"):   
        word_list = list(word)[0:-4]
        word_remove = "".join(word_list)
        if word_remove.endswith("i"):
           result = word_remove.replace("i","y")
           return result
        else:
           return word_remove
        
        
# Transform a verb into a adjective by adding "en".
def adjective_to_verb(sentence, index):
    sentence_list = sentence.split()
    return str(sentence_list[index])+"en"