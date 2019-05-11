
import falcon

class MatchResource:
	def on_get(self, request, response):
		response.media = {
			'foo': 'bar'
		}

api = falcon.API()
api.add_route('/match', MatchResource())
