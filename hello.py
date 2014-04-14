#import database
from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

data = {}

parser = reqparse.RequestParser()
parser.add_argument('data', type = str)

def abort_if_doesnt_exist(data_id):
	if data_id not in data:
		abort(404, message = "Data {} doesn't exist".format(data_id))

class Data(Resource):
	def get(self, data_id):
		abort_if_doesnt_exist(data_id)
		return data[data_id]

	def delete(self, data_id):
		abort_if_doesnt_exist(data_id)
		del data[data_id]
		return '', 204

	def put(self, data_id):
		args = parser.parse_args()
		updated_data = {'data': args['data']}
		data[data_id] = updated_data
		return data, 201

class DataList(Resource):
	def get(self):
		return data;

	def post(self):
		args = parser.parse_args()
		data_id = len(data) + 1
		data[data_id] = {'data': args['data']}
		return data[data_id], 201


api.add_resource(Data, '/data/<int:data_id>')
api.add_resource(DataList, '/', '/data')

if __name__ == '__main__':
    app.run(debug=True)
