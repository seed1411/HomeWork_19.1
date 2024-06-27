from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

host_name = "localhost"
server_port = 8080


class MyServer(BaseHTTPRequestHandler):

    def __get_index(self):
        with open("index.html", encoding="utf-8") as file:
            content = file.read()
        return content

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        page_content = self.__get_index()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    web_server = HTTPServer((host_name, server_port), MyServer)
    print("Server started http://%s:%s" % (host_name, server_port))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped.")
