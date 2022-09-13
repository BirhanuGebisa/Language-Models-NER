## Table of Contents
* [Setup](#setup)
* [Generating Prompts](#generating-prompts)
* [Label Token Selection](#label-token-selection)


## Setup

### 1. Create conda environment
```
conda create -n autoprompt -y python=3.7 && conda activate autoprompt
```

### 2. Install dependecies
Install the required packages
```
pip install -r requirements.txt
```
Also download the spacy model
```
python -m spacy download en
```

### 3. Download the data
The datasets 

There are a couple different datasets for fact retrieval and relation extraction so here are brief overviews of each:
- Fact Retrieval
  - `original`: 
  - `original_rob`: 
  - `trex`: 
- Relation Extraction

## Generating Prompts

### Quick Overview of Templates

Depending on the language model 

### Fact Retrieval
```
python
```

### Relation Extraction
```
python -m autoprompt.create_trigger \
    
```

## Label Token Selection

For sentiment analysis
```
python 

For NLI
```
python 
```

## Evaluation for Fact Retrieval and Relation Extraction

###. Setup LAMA
Clone 
```

```

### 4. Miscellaneous
## Citation
```
```
