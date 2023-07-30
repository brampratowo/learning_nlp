import os
import json
from json import JSONEncoder
from nltk.util import ngrams
import nltk


class HelperFunction(object):
    def loadJsonFile(filename):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, filename)
        with open(file_path) as data_file:
            data = json.load(data_file)
        return data

    def loadTextFile(filename):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, filename)
        with open(file_path, encoding="utf-8") as data_file:
            data = data_file.read()
        return data

    def gramsText(text, range):
        NGRAMS=ngrams(sequence=nltk.word_tokenize(text), n=range)
        grams_list = []
        for grams in NGRAMS:
            grams_list.append(grams)
        
        return grams_list

class SetEncoder(JSONEncoder):
    def default(self, obj):
        return list(obj)
