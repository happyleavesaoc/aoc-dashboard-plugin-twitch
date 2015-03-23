import plugins
import urllib
import urllib2
import _ssl
# Import note: May only import modules that are linked in the core executable
_ssl.PROTOCOL_SSLv23 = _ssl.PROTOCOL_TLSv1 # http://bugs.python.org/issue11220

class Twitch(plugins.DashboardPlugin):
	"""Twitch Title Interface

	Subscribes to title changes and updates Twitch channel accordingly.
	"""

	API_URL = "https://api.twitch.tv/kraken/channels/"	#: Twitch API url
	GAME = "Age of Empires II: The Conquerors"			#: Game name

	def init(self, configuration):
		"""Initialization

		Called on plugin system initialization

		:param configuration: Configuration section as dictionary
		"""
		self._channel = configuration["channel"]
		self._oauth = configuration["oauth"]
		self._prefix = configuration["prefix"]
		self._suffix = configuration["suffix"]

	def registration(self):
		"""Registration

		Dashboard plugin manager calls this and subscribes plugin
		to message types returned.

		:returns: Dictionary of message types to callback functions
		"""
		return {
			"title": self.on_title
		}

	def on_title(self, title):
		"""Title change callback

		This callback function will run any time the game title changes, including:

		- At the game start
		- After spectator issues !title command
		- After spectator issues !t[1,2] command (if team game)

		:param title: Game title string
		"""
		title = " ".join([self._prefix, title, self._suffix]).strip()
		url = "{}{}?{}".format(Twitch.API_URL, self._channel, urllib.urlencode({"channel[status]": title, "channel[game]": Twitch.GAME}))

		# Construct request
		request = urllib2.Request(url)
		request.add_header("Accept", "application/vnd.twitchtv.v2+json")
		request.add_header("Authorization", "OAuth {}".format(self._oauth))
		request.add_header("Content-Length", "0")
		request.get_method = lambda: "PUT"

		# Send request
		urllib2.build_opener(urllib2.HTTPHandler).open(request)