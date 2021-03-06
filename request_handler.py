from entries import get_all_entries, get_single_entry, delete_entry, create_entry, update_journal_entry
from moods import get_all_moods
from tags import get_all_tags, create_tag
from entryTags import get_all_entry_tags, create_entry_tag, delete_entryTag
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class HandleRequests(BaseHTTPRequestHandler):
	def do_OPTIONS(self):
		self.send_response(200)
		self.send_header('Access-Control-Allow-Origin', '*')
		self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
		self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
		self.end_headers()

	def parse_url(self, path):
		path_params = path.split("/")
		resource = path_params[1]

		id = None

		try:
			id = int(path_params[2])
		except IndexError:
			pass  # No route parameter exists: /entries
		except ValueError:
			pass  # Request had trailing slash: /entries/

		return (resource, id)

	def _set_headers(self, status):
		self.send_response(status)
		self.send_header('Content-type', 'application/json')
		self.send_header('Access-Control-Allow-Origin', '*')
		self.end_headers()

	def do_GET(self):
		self._set_headers(200)

		response = {}

		parsed = self.parse_url(self.path)
		
		( resource, id ) = parsed

		if resource == "entries":
			if id is not None:
				response = f"{get_single_entry(id)}"
			else:
				response = f"{get_all_entries()}"
		if resource == "moods":
				response = f"{get_all_moods()}"
		if resource == "tags":
				response = f"{get_all_tags()}"
		if resource == "entryTags":
				response = f"{get_all_entry_tags()}"

		self.wfile.write(response.encode())

	def do_POST(self):
		self._set_headers(201)
		content_len = int(self.headers.get('content-length', 0))
		post_body = self.rfile.read(content_len)

		# Convert JSON string to a Python dictionary
		post_body = json.loads(post_body)

		# Parse the URL
		(resource, id) = self.parse_url(self.path)

		new_item = None

		if resource == "entries":
			new_item = create_entry(post_body)
		if resource == "tags":
			new_item = create_tag(post_body)
		if resource == "entryTags":
			new_item = create_entry_tag(post_body)

		self.wfile.write(f"{new_item}".encode())


	def do_PUT(self):
		content_len = int(self.headers.get('content-length', 0))
		post_body = self.rfile.read(content_len)
		post_body = json.loads(post_body)

		# Parse the URL
		(resource, id) = self.parse_url(self.path)
		success = False
		if resource == "entries":
		  success = update_journal_entry(id, post_body)
		
		if success:
			self._set_headers(204)
		else:
			self._set_headers(404)

		self.wfile.write("".encode())
	
	def do_DELETE(self):
		# Set a 204 response code
		self._set_headers(204)

		# Parse the URL
		(resource, id) = self.parse_url(self.path)

		if resource == "entries":
		    delete_entry(id)
		if resource == "entryTags":
		    delete_entryTag(id)

		self.wfile.write("".encode())


# This function is not inside the class. It is the starting
# point of this application.
def main():
	host = ''
	port = 8088
	HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
	main()