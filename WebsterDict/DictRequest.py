import requests
import json
import pandas as pd

class QueryWords:

    def __init__(self, word):
        self.word = word
        self.thesaurus_api  = "https://dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key=54f5b234-396e-4aaf-b50b-93f4b996c37e"
        self.dictionary_api = "https://dictionaryapi.com/api/v3/references/collegiate/json/{word}?key=b163bc64-3f87-4526-ba76-f4cc12ed21bc"

    def query_thesaurus(self):
        '''Query the thesaurus dictionary and store the returned text as a json object'''
        query = self.thesaurus_api.format(word=self.word)
        r = requests.get(query)
        res = json.loads(r.text)
        return res

    def query_dictionary(self):
        '''Query the collegiate dictionary and store the returned text as a json object'''
        query = self.dictionary_api.format(word=self.word)
        r = requests.get(query)
        res = json.loads(r.text)
        return res

    def thes_extract(self, res):
        res[0]

    def thes_or_dict(self):
        res_d = self.query_dictionary()
        res_t = self.query_thesaurus()

        if type(res_t[0]) != dict:
            return res_d
        else:
            return res_t



word = QueryWords('anachronistic')



# syns = [item for sublist in res[0]['meta']['syns'] for item in sublist]
# fl   = res[0]['fl']
# dt   = res[0]['shortdef']