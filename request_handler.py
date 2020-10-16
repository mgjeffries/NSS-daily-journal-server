from entries import get_all_entries, get_single_entry, delete_entry
from moods import get_all_moods
from tags import get_all_tags
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class HandleRequests(BaseHTTPRequestHandler):
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

		self.wfile.write(f"{new_item}".encode())


	def do_PUT(self):
		self._set_headers(204)
		content_len = int(self.headers.get('content-length', 0))
		post_body = self.rfile.read(content_len)
		post_body = json.loads(post_body)

		# Parse the URL
		(resource, id) = self.parse_url(self.path)

		# if resource == "animals":
		#     update_animal(id, post_body)
		# if resource == "customers":
		#     update_customer(id, post_body)
		# if resource == "employees":
		#     update_employee(id, post_body)

		self.wfile.write("".encode())
	
	def do_DELETE(self):
		# Set a 204 response code
		self._set_headers(204)

		# Parse the URL
		(resource, id) = self.parse_url(self.path)

		if resource == "entries":
		    delete_entry(id)

		# Encode the new animal and send in response
		self.wfile.write("".encode())


# This function is not inside the class. It is the starting
# point of this application.
def main():
	host = ''
	port = 8088
	HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
	main()