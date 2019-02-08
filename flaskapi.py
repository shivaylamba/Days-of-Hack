from flask import flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
from model import LinearModel


app = Flask(__name__)
api = Api(app)




model = LinearModel()
clf_path = 'lib/models/LinearModel.pkl'
with open(clf_path, 'rb') as f:
    model.clf = pickle.load(f)

parser = reqparse.RequestParser()
parser.add_argument('query')




class PredictEnergy(Resource):
    def get(self):
        args = parser.parse_args()
        user_query = args['query']
        uq_vectorized = model.vectorizer_transform(
            np.array([user_query]))
        prediction = model.predict(uq_vectorized)
        pred_proba = model.predict_proba(uq_vectorized)
        
      
        output = {'prediction': pred_text, 'Energyconsumed': confidence}
        
        return output



   api.add_resource(PredictEnergy, '/')
  
api.add_resource(PredictEnergy, '/energyconsumed')     

f __name__ == '__main__':
    app.run(debug=True)
