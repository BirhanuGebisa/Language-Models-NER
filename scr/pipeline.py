import sys
import os
import matplotlib.pyplot as plt
from difflib import SequenceMatcher

sys.path.append(os.path.abspath(os.path.join("./scr/")))
from logger import logger


class Pipeline():

    def __init__(self, currernt_technique='technique1') -> None:
        self.techniques_list = ['technique1']
        self.currernt_technique = currernt_technique

    def send_request_to_cohere(self, co, prompt, model='xlarge'):
        """
            Sends an API request to cohere and reuturns the response
        """
        try:
            response = co.generate( 
                model=model, 
                prompt=prompt, 
                max_tokens=400, 
                temperature=0.5, 
                k=0, 
                p=1, 
                frequency_penalty=0, 
                presence_penalty=0, 
                stop_sequences=["--"], 
                return_likelihoods='NONE')
            logger.info("Rquest successful")
            return response.generations[0].text
        except Exception as e:
            logger.error(e)

    def get_tokens(self, data):
        token_dict = {}
        try:
            for token in data['tokens']:
                entity_label = token['entityLabel']
                if entity_label in token_dict.keys():
                    token_dict[entity_label] += f",{token['text']}"
                else:
                    token_dict[entity_label] = f"{token['text']}"
            logger.info("Tokens converted to Dict")
        except Exception as e:
            logger.error(e)
        return token_dict

    def process_response(self,response):
        response = str(response).strip().split('\n')
        response_dict = {}
        for vl in response:
            try:
                splitted_val = vl.split(':')
                response_dict[splitted_val[0]] = splitted_val[1]
            except Exception as e:
                pass

        return response_dict

    def get_prediction_similarity(self, token_dict, response_dict):
        try:
            prediction_similarity = {}
            for k,v in token_dict.items():
                if k in response_dict.keys():
                    prediction_similarity[k] = SequenceMatcher(None, v, response_dict[k]).ratio()
                else:
                    prediction_similarity[k] = 0.0
            return prediction_similarity
        except Exception as e:
            logger.error(e)
            return {}

    def plot_result(self, result):
        try:
            plt.bar(range(len(result)), list(result.values()), align='center')
            plt.xticks(range(len(result)), list(result.keys()))
            plt.show()
            logger.info("Plotted result")
        except Exception as e:
            logger.error(e)


    def extract_values(self, data):
        s: str = ''
        try:
            for d in data:
                s+='Job Description: '
                s+=str(d['document']).strip().replace('\n', ' ').strip()
                s+='\n'
                token_dict = {}
                for token in d['tokens']:
                    entity_label = token['entityLabel']
                    if entity_label in token_dict.keys():
                        token_dict[entity_label] += f",{token['text']}"
                    else:
                        token_dict[entity_label] = f"{token['text']}"
                dict_str = ''
                for key,value in token_dict.items():
                    dict_str+=f"{key}: {value}\n"
                s+=dict_str
                s+='\n--\n'
            logger.info("Values extracted.")
            return s
        except Exception as e:
            logger.error(e)

    

