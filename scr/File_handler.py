import json
import sys
import os
import dvc.api

sys.path.append(os.path.abspath(os.path.join("../scr/")))
from logger import logger


class FileHandler():
    def dvc_get_data(self, path, version='v3'):
        data = []
        try:
            repo = "home/sucess/10-academy/week-4/Language-Models-NER"
            data_url = dvc.api.get_url(path=path, repo=repo, rev=version)
            data_url = str(data_url)[6:]
            with open(data_url, 'r') as f:
                data = json.loads(f.read())
            #logger.info(f"{path} with version {version} Loaded")
        except Exception as e:
            logger.error(e)
        return data