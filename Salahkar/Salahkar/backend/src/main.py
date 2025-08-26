from flask import Flask, request, jsonify
from models.ai_model import AImodel

app = Flask(__name__)
ai_model = AImodel()

@app.route('/simplify', methods=['POST'])
def simplify_document():
    data = request.json
    document = data.get('document')
    simplified_text = ai_model.simplify_document(document)
    return jsonify({'simplified': simplified_text})

@app.route('/summarize', methods=['POST'])
def summarize_terms():
    data = request.json
    terms = data.get('terms')
    summary = ai_model.summarize_terms(terms)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
