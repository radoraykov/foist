from foist.conversion import to_html
from flask import Flask, make_response
from flask.ext import restful
from flask.ext.restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('url', type=str)
app = Flask(__name__)
api = restful.Api(app)


class Convert(restful.Resource):
    def post(self):
        args = parser.parse_args()
        return make_response(to_html(args['url'], 'html'))

api.add_resource(Convert, '/convert')

if __name__ == '__main__':
    app.run(debug=True)