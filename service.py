
import falcon
import classify_strings as cache

class MatchResource:
	def __init__(self):
		cache.populate_cache(cache.words_file_path, 2000)

	def on_get(self, request, response):
		response.media = { 'matches': [] }
		if not 'search' in request.params:
			return
		search = request.params['search']
		if len(search) < 3:
			return
		response.media['matches'] = cache.search(search)

api = falcon.API()
api.add_route('/match', MatchResource())
