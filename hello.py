import sys
import database
from bson import json_util
from flask import Flask, Response, json
from flask.ext.restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('data', type = str)

def abort_if_doesnt_exist(data_id):
	if database.find(data_id) is None:
		abort(404, message = "Data {} doesn't exist".format(data_id))

def json_dump(obj):
	return Response(json.dumps(obj, default=json_util.default), mimetype='application/json')

class Data(Resource):
	def get(self, data_id):
		abort_if_doesnt_exist(data_id)
		return json_dump(database.find(data_id))

class DataList(Resource):
	def get(self):
		dataList = list(database.find_all())
		return json_dump(dataList)

	def post(self):
		args = parser.parse_args()
		data_id = database.insert(args['data'])
		return json_dump(data_id), 201

api.add_resource(Data, '/data/<string:data_id>')
api.add_resource(DataList, '/', '/data')

if __name__ == '__main__':
    app.run(debug=True)
