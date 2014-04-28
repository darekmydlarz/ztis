import sys
import database
import mock
from bson import json_util
import flask
from flask import Flask, Response
from flask.ext.restful import reqparse, abort, Api, Resource
import urllib2, json

app = Flask(__name__)
api = Api(app)

def abort_if_doesnt_exist(data_id):
	if database.find(data_id) is None:
		abort(404, message = "Data {} doesn't exist".format(data_id))

def json_dump(obj):
	return Response(flask.json.dumps(obj, default=json_util.default), mimetype='application/json')

class Data(Resource):
	def get(self, data_id):
		abort_if_doesnt_exist(data_id)
		return json_dump(database.find(data_id))

class DataList(Resource):
	def get(self):
		dataList = list(database.find_all())
		return json_dump(dataList)

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('data', type = str)
		args = parser.parse_args()
		data_id = database.insert(args['data'])
		return flask.json.dumps(data_id, default=json_util.default), 201

class Mock(Resource):
	def get(self):
		return json_dump(json_util.loads(mock.getData()))


class Consume(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('address', type = str)
		# address must be given from other proccess of application
		# e.g. run one on port 5000, another on 3000 and communicate each other
		address = parser.parse_args()['address']
		eventData = json.loads(urllib2.urlopen(address).read())
		eventId = database.insertEvents(eventData["events"])
		return {}, 201


api.add_resource(Data, '/data/<string:data_id>')
api.add_resource(DataList, '/', '/data')
api.add_resource(Mock, '/mock')
api.add_resource(Consume, '/consume')

if __name__ == '__main__':
    app.run(debug=True)
