from Corpus.Sentence import Sentence

from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer

word_list,type_list = [],[]

fsm = FsmMorphologicalAnalyzer()
sentence = Sentence("iyade gönderdim hala bi cevap veren olmadi 15 gündür halen beklemedeyiz")
parseLists = fsm.morphologicalAnalysis(sentence)
for i in range(len(parseLists)):
    for j in range(parseLists[i].size()):
        parse = parseLists[i].getFsmParse(j)
        word_list.append(parse.transitionList())
        type_list.append(parse.getInitialPos())
        #print(parse.getSurfaceForm())
        #print(parse.getInitialPos())
        print(parse.transitionList())
        #print(parseLists)
    #print("-----------------")

#print(word_list)

word = ""
noun_list = []
plus_count = 0
 
            

for i in word_list:
    for j in i:
        if plus_count == 2 or j == "ADV" or j=="ADJ" or j=="VERB":
            break
        elif j != "+":
            word += j
        else:
            plus_count += 1
            if word == "NOUN":
                break
            else:
                copy_word = word
            #print(copy_word)
            word = ""
    plus_count=0
    if word == "NOUN" and copy_word not in noun_list:
        noun_list.append(copy_word)
    word=""
    copy_word=""

print(noun_list)

