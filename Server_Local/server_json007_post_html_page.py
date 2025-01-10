#https://anshu-dev.medium.com/creating-a-python-web-server-from-basic-to-advanced-449fcb38e93b
#http://127.0.0.1:7575/

#!/usr/bin/env python3
print("to run , python3 server_json004.py 8082");
"""An example HTTP server with GET and POST endpoints.

Access to XMLHttpRequest at 'http://192.168.1.11:8082/' from origin 'null' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
https://gist.github.com/nitaku/10d0662536f37a087e1b
mfickett commented on Jul 14, 2020


 sudo  fuser -k 8082/tcp
 python3 server_json004.py 8082
 curl http://192.168.1.11:8082



 
 
curl --data "{\"title\": \"My first blogpost ever\",\"body\": \"Lorem ipsum dolor sit amet.\",\"author\": \"Elke\",\"date_ms\": 1593607500000}" --header "Content-Type: application/json" http://192.168.1.11:8082 



{"results":[{"title": "My first blogpost ever!", "body": "Lorem ipsum dolor sit amet.", "author": "Elke", "date_ms": 1593607500000},
{"title": "Look I am blogging!", "body": "Hurray for me, this is my second post!", "author": "Elke", "date_ms": 1593870300000},
{"title": "Another one?!", "body": "Another one!", "author": "Elke", "date_ms": 1594419000000}]}
"""



from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
import json
import time
import logging

# Sample blog post data similar to
# https://ordina-jworks.github.io/frontend/2019/03/04/vue-with-typescript.html#4-how-to-write-your-first-component
_g_posts = [
    {
        'title': 'My first blogpost ever!',
        'body': 'Lorem ipsum dolor sit amet.',
        'author': 'Elke',
        'date_ms': 1593607500000,  # 2020 July 1 8:45 AM Eastern
    },
    {
        'title': 'Look I am blogging!',
        'body': 'Hurray for me, this is my second post!',
        'author': 'Elke',
        'date_ms': 1593870300000, # 2020 July 4 9:45 AM Eastern
    },
    {
        'title': 'Another one?!',
        'body': 'Another one!',
        'author': 'Elke',
        'date_ms': 1594419000000, # 2020 July 10 18:10 Eastern
    }
]


class _RequestHandler(BaseHTTPRequestHandler):
    # Borrowing from https://gist.github.com/nitaku/10d0662536f37a087e1b
    def _set_headers(self):
        self.send_response(HTTPStatus.OK.value)
        self.send_header('Content-type', 'application/json')
        # Allow requests from any origin, so CORS policies don't
        # prevent local development.
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()


    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
            try:
                file_to_open = open(self.path[1:]).read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(file_to_open, 'utf-8'))
            except:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'404 - Not Found')
        elif(self.path == '/time'):
            print("success")
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
            self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
            self.wfile.write(bytes("<a href='/'>Index</a>", "utf-8"))
            self.wfile.write(bytes("<h1>Heading 1 .</h1>", "utf-8"))
            
            self.wfile.write(bytes("<h1>", "utf-8"))
            self.wfile.write("Hello Ahmed, GET request for Current time {}".format(self.get_time()).encode('utf-8'))
            self.wfile.write(bytes("</h1>", "utf-8"))
            self.wfile.write(bytes('<input type="button" onclick="alert(1)"  value="Show confirm box"  />',"utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        elif self.path == '/mesbaha':
            self.path = '/mesbaha.html'
            try:
                file_to_open = open(self.path[1:]).read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(file_to_open, 'utf-8'))
            except:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'404 - Not Found')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 - Not Found')


    def do_POST(self):
        length = int(self.headers.get('content-length'))
        message = json.loads(self.rfile.read(length))
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), message)
        message['date_ms'] = int(time.time()) * 1000
        print("message is ", message)
        _g_posts.append(message)
        self._set_headers()
        #self.wfile.write(json.dumps(_g_posts).encode('utf-8'))

    def do_OPTIONS(self):
        # Send allow-origin header for preflight POST XHRs.
        self.send_response(HTTPStatus.NO_CONTENT.value)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST')
        self.send_header('Access-Control-Allow-Headers', 'content-type')
        self.end_headers()


    def get_time(self):
        from datetime import datetime
        # Returns a datetime object containing the local date and time
        dateTimeObj = datetime.now()
        # get the time object from datetime object
        timeObj = dateTimeObj.time()
        # Access the member variables of time object to print time information
        return (timeObj.hour,':',timeObj.minute,':', timeObj.second)

    def get_date(self):
        from datetime import datetime
        dateTimeObj = datetime.now()
        # get the date object from datetime object
        dateObj = dateTimeObj.date()

        # Access the member variables of time object to print time information
        return  (dateObj.year, '/', dateObj.month, '/', dateObj.day)

def run(server_class=HTTPServer, handler_class=_RequestHandler, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
