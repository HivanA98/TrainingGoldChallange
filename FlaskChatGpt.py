from flask import Flask, request
from flask_restful import Resource, Api
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

class DeleteSentence(Resource):
    def post(self):
        """
        Delete Sentence
        ---
        parameters:
          - name: sentence
            in: formData
            type: string
            required: true
        """
        sentence = request.form['sentence']
        return {'message': 'Sentence deleted: {}'.format(sentence)}, 200

class DeleteWordInSentence(Resource):
    def post(self, word):
        """
        Delete Specific Word in Sentence
        ---
        parameters:
          - name: sentence
            in: formData
            type: string
            required: true
          - name: word
            in: path
            type: string
            required: true
        """
        sentence = request.form['sentence']
        updated_sentence = sentence.replace(word, '')
        return {'message': 'Updated Sentence: {}'.format(updated_sentence.strip())}, 200

api.add_resource(DeleteSentence, '/delete')
api.add_resource(DeleteWordInSentence, '/delete/<string:word>')

if __name__ == '__main__':
    app.run(debug=True)
