from flask import Flask, render_template, request
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
from scripts.news_classifier_pipline import Pipeline
from scripts.job_desc_pipeline import Job_Pipeline
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/news')
def news():
   return render_template('news_classify.html')

@app.route('/bnewscore')
def newsscore():
   title = request.args.get('title')
   desc = request.args.get('desc')
   pipe = Pipeline()
   pred = pipe.pipeline(title, desc)
   return render_template('news_classify.html', prediction=pred)

@app.route('/job')
def job():
   return render_template('entity_rego.html')

@app.route('/jdentities')
def job_desc_entities():
   document = request.args.get('document')
   pipe = Job_Pipeline()
   pred = pipe.pipeline(document)
   return render_template('entity_rego.html', prediction=pred)


if __name__ == '__main__':
   app.run(debug = True)