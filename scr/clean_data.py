import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join("./scr/")))
from logger import logger

class Cleaned():
    def __init__(self) -> None:
        pass

    def remove_irrelevant_pairs(self, data, key):
        try:
            del data[key]
        except Exception as e:
            pass
        
    def clean_tokens(self, data, irrelevant_keys=['start', 'end', 'token_start', 'token_end']):
        try:
            final_data = []
            for d in data:
                temp_data = d
                temp_tokens = []
                for token in d['tokens']:
                    temp_token = {}
                    for k in token.keys():
                        if k not in irrelevant_keys:
                            temp_token[k] = token[k]
                    temp_tokens.append(temp_token)
                temp_data['tokens'] = temp_tokens
                final_data.append(temp_data)
            logger.info("Cleaned Irrelevant key:value pairs in tokens.")
        except Exception as e:
            logger.error(e)


    def runpipeline(self, data, irrelevant_data_keys=[], irrelevant_token_keys=[]):
        for df in data:
            for key in irrelevant_data_keys:
                self.remove_irrelevant_pairs(df, key)

        self.clean_tokens(data, irrelevant_keys=irrelevant_token_keys)

    

