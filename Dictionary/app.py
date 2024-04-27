"""
English Dictionary Program

This program allows users to look up the meaning, synonyms, and usage examples of English words using NLTK's WordNet. Additionally, it provides functionalities for tokenization, POS tagging, stemming, lemmatization, and named entity recognition (NER).

Author: Mohammed Kolo Ibrahim
Date: March 22, 2024

Functions:
- get_word_info(word): Get various information related to a word using WordNet.
- main(): Main function to run the English dictionary program.
"""

import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag, ne_chunk
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer

# Download NLTK resources
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def get_word_info(word):
    """
    Get various information related to a word using WordNet.

    Args:
    - word (str): The word for which to retrieve information.

    Returns:
    - dict: A dictionary containing various information related to the word.
    """
    synsets = wn.synsets(word)
    if synsets:
        meaning = synsets[0].definition()
        synonyms = set()
        examples = []
        for synset in synsets:
            for lemma in synset.lemmas():
                synonyms.add(lemma.name())
            examples.extend(sent_tokenize(synset.definition()))
            examples.extend(synset.examples())
        # Remove stopwords from examples
        stop_words = set(stopwords.words('english'))
        examples = [sentence for sentence in examples if word.lower() in word_tokenize(sentence.lower()) and not any(word in word_tokenize(sentence.lower()) for word in stop_words)]
        return {
            'meaning': meaning,
            'synonyms': list(synonyms),
            'examples': examples
        }
    else:
        return None

def get_word_tokens(text):
    """
    Tokenize text into words.

    Args:
    - text (str): The text to tokenize.

    Returns:
    - list: A list of word tokens.
    """
    return word_tokenize(text)

def get_sentence_tokens(text):
    """
    Tokenize text into sentences.

    Args:
    - text (str): The text to tokenize.

    Returns:
    - list: A list of sentence tokens.
    """
    return sent_tokenize(text)

def get_pos_tags(words):
    """
    Tag words with their parts of speech.

    Args:
    - words (list): List of word tokens.

    Returns:
    - list: A list of (word, pos_tag) tuples.
    """
    return pos_tag(words)

def get_named_entities(pos_tags):
    """
    Extract named entities from POS-tagged words.

    Args:
    - pos_tags (list): List of (word, pos_tag) tuples.

    Returns:
    - list: A list of named entities.
    """
    return ne_chunk(pos_tags)

def get_stemming(word):
    """
    Perform stemming on a word.

    Args:
    - word (str): The word to stem.

    Returns:
    - str: The stemmed word.
    """
    porter = PorterStemmer()
    lancaster = LancasterStemmer()
    return {
        'Porter Stemming': porter.stem(word),
        'Lancaster Stemming': lancaster.stem(word)
    }

def get_lemmatization(word):
    """
    Perform lemmatization on a word.

    Args:
    - word (str): The word to lemmatize.

    Returns:
    - str: The lemmatized word.
    """
    lemmatizer = WordNetLemmatizer()
    return lemmatizer.lemmatize(word)

def main():
    """
    Main function to run the English dictionary program.
    """
    print("Welcome to the English Dictionary Program!")
    print("Enter a word (type 'exit' to quit): ")
    while True:
        word = input().strip().lower()
        if word in ['exit', 'quit']:
            print("Exiting the program...")
            break
        
        # Get various information related to the word
        word_info = get_word_info(word)
        
        if word_info:
            print(f"Meaning of '{word}': {word_info['meaning']}")
            if word_info['synonyms']:
                print(f"Synonyms: {', '.join(word_info['synonyms'])}")
            else:
                print("No synonyms found.")
            if word_info['examples']:
                print("Examples:")
                for example in word_info['examples'][:3]:
                    print("-", example)
            else:
                print("No examples found.")
            
            # Additional functionalities
            text = " ".join(word_info['examples']) if word_info['examples'] else word_info['meaning']
            word_tokens = get_word_tokens(text)
            sentence_tokens = get_sentence_tokens(text)
            pos_tags = get_pos_tags(word_tokens)
            named_entities = get_named_entities(pos_tags)
            stemming = get_stemming(word)
            lemmatization = get_lemmatization(word)
            
            print("\nAdditional Functionalities:")
            print("Word Tokens:", word_tokens)
            print("Sentence Tokens:", sentence_tokens)
            print("POS Tags:", pos_tags)
            print("Named Entities:", named_entities)
            print("Stemming:", stemming)
            print("Lemmatization:", lemmatization)
            
        else:
            print(f"Word '{word}' not found in WordNet.")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()