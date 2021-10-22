import time
import logging

from zemberek import (
    TurkishSpellChecker,
    TurkishSentenceNormalizer,
    TurkishSentenceExtractor,
    TurkishMorphology,
    TurkishTokenizer
)

#from TurkishStemmer import TurkishStemmer
from snowballstemmer import TurkishStemmer

logger = logging.getLogger(__name__)

examples = ["Yrn okua gidicem"
            ]

morphology = TurkishMorphology.create_with_defaults()

# SENTENCE NORMALIZATION
start = time.time()
normalizer = TurkishSentenceNormalizer(morphology)
logger.info(f"Normalization instance created in: {time.time() - start} s")

start = time.time()
for example in examples:
    print(example)
    print(normalizer.normalize(example), "\n")
logger.info(f"Sentences normalized in: {time.time() - start} s")

start = time.time()
sc = TurkishSpellChecker(morphology)
logger.info(f"Spell checker instance created in: {time.time() - start} s")


# SPELLING SUGGESTION
li = ["iyade", "tartısıyor", "Ankar'ada", "knlıca", "yapablrim", "kıredi", "geldm", "geliyom", "aldm", "asln"]
start = time.time()
for word in li:
    print(word + " = " + ' '.join(sc.suggest_for_word(word)))
logger.info(f"Spells checked in: {time.time() - start} s")


# SENTENCE BOUNDARY DETECTION
start = time.time()
extractor = TurkishSentenceExtractor()
print("Extractor instance created in: ", time.time() - start, " s")

text = "iyade gönderdim hala bi cevap veren olmadi 15 gündür halen beklemedeyiz"
       

start = time.time()
sentences = extractor.from_paragraph(text)
print(f"Sentences separated in {time.time() - start}s")

noun_list = []
stemmer = TurkishStemmer()
turkStem=TurkishStemmer()

tokenizer = TurkishTokenizer.DEFAULT

for sentence in sentences:
    splitwords = sentence.split()
    for word in splitwords:
        results = morphology.analyze(word)
        for result in results:
            #print(result.format_string())
            if ":Noun" in result.format_string() and not word in noun_list:
                #noun_list.append(stemmer.stem(word))
                #noun_list.append(turkStem.stemWord(word))
                result_split = result.format_string().split()
                count = 0
                for key in result_split:
                    if count == 2:
                        break
                    count = 0
                    tokens=tokenizer.tokenize(key)
                    for token in tokens:
                        count += 1
                        #print('Content = ', token.content)
                        #print('Type = ', token.type_.name)
                        #print('Start = ', token.start)
                        #print('Stop = ', token.end, '\n')
                        
                        if count == 2:
                            noun_list.append(token.content)
                            break
                """
                for key in result_split:
                    break
                    #print(key)
                """
            else:
                print("Nope")
            break
             
        print("\n")
      
print(noun_list)

 

