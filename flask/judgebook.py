from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import requests
import json # For interacting with the Google Cloud Vision API
from google.cloud import vision
from google.cloud.vision import types

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    title = TextField('Title:', validators=[validators.required()])
    author = TextField('Author:', validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        title=request.form['title']
        author=request.form['author']

        if form.validate():
            # Save the comment here.
            flash('OK, looking for the book ' + title + ' by ' + author)
            labels = judgeBookByCover(title, author)
            render_template('results.html', labels=labels)
        else:
            flash('All the form fields are required. ')

    return render_template('index.html', form=form)

def judgeBookByCover(title, author):
    params = {'title': title, 'author': author}
    response = requests.get('http://openlibrary.org/search.json', params=params)
    if response.ok:
        parsed = json.loads(response.text)
        if len(parsed['docs']) > 0:
            if len(parsed['docs'][0]['isbn']) > 0:
                isbn = parsed['docs'][0]['isbn'][0]
            else:
                raise Exception("Can't find isbn.")
        else:
            raise Exception("Can't find book.")
        coverURL = 'http://covers.openlibrary.org/b/ISBN/' + isbn + '-L.jpg'
        coverResponse = requests.get(coverURL, stream=True)
        if coverResponse.ok:
            with open('cover.jpg', 'wb') as f:
                f.write(coverResponse.content)
            client = vision.ImageAnnotatorClient()
            content = open('cover.jpg', 'rb').read()
            image = types.Image(content=content)
            response = client.label_detection(image=image)
            labels = response.label_annotations
            print('Judgments:')
            descriptions = [label.description for label in labels]
            return descriptions
        else:
            raise Exception("Can't find cover.")
    else: 
        raise Exception("Bad response from initial book search.")


if __name__ == "__main__":
    app.run()
