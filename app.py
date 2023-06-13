from flask import Flask, request, jsonify
from bardapi import Bard
import os

app = Flask(__name__)
os.environ['_BARD_API_KEY'] = "XQgHISTD3YxeDpORSZNcxd9N3yE1H33_TETWss3ZiKPyIkvcHVuSkdBEQOWhWKaswoPaUw."

@app.route('/api', methods=['POST'])
def get_bard_content():
    input_text = request.form.get('input')
    content = Bard().get_answer(input_text)['content']
    return jsonify({"content": content})

if __name__ == '__main__':
    app.run()
