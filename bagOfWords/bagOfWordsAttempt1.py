#to get bag of words, using topics, originating calenders, descrptions, tite
import metapy
from collections import defaultdict

def tokens_lowercase(doc):
    #Write a token stream that tokenizes with ICUTokenizer, 
    #lowercases, removes words with less than 2 and more than 5  characters
    #performs stemming and creates trigrams (name the final call to ana.analyze as "trigrams")
    #'''Place your code here'''
    #You are required to create a function that tokenizes with ICUTokenizer (without the end/start tags, i.e. use the argument "suppress_tags=True"), 
    #lowercases, removes words with less than 2 and more than 5 characters, performs stemming and produces trigrams for an input sentence.

    tok = metapy.analyzers.ICUTokenizer(suppress_tags=True)
    #tok = metapy.analyzers.LengthFilter(tok, min=2, max=5)
    tok = metapy.analyzers.LowercaseFilter(tok)
    tok = metapy.analyzers.ListFilter(tok, "lemur-stopwords.txt", metapy.analyzers.ListFilter.Type.Reject)
    tok = metapy.analyzers.Porter2Filter(tok)
    #ana = metapy.analyzers.NGramWordAnalyzer(1, tok)
    #trigrams = ana.analyze(doc)
    #leave the rest of the code as is
    tok.set_content(doc.content())
    tokens, counts = [], []
    #for token, count in trigrams.items():
        #counts.append(count)
        #tokens.append(token)
    freq_dict = defaultdict(int)  
    for token in tok:
    	#for token in tokens:
    	freq_dict[token] += 1
    
    top = sorted(freq_dict, key=freq_dict.get, reverse=True)
    top = top[:25]
    return top
    
if __name__ == '__main__':
    file1 = open("words.txt", "r")
    doc = metapy.index.Document()
    doc.content(file1.read())
    print(doc.content()) #you can access the document string with .content()
    tokens = tokens_lowercase(doc)
    print(tokens)

