# !/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import gensim

print('model loading ...')
model = gensim.models.KeyedVectors.load_word2vec_format('/Users/sindongboy/Downloads/lexvec.vectors')
print('model loading done')

# Create custom HTTPRequestHandler class
class KodeFunHTTPRequestHandler(BaseHTTPRequestHandler):
    # handle GET command
    def do_GET(self):
        # send code 200 response
        self.send_response(200)

        score = model.similarity(self.path.split('-')[0], self.path.split('-')[1])
        # send header first
        self.send_header('Content-type','text-html')
        self.end_headers()

        # send file content to client
        self.wfile.write(score)
        return

def run():
    print('http server is starting...')

    # ip and port of servr
    # by default http server port is 80
    server_address = ('127.0.0.1', 80)
    httpd = HTTPServer(server_address, KodeFunHTTPRequestHandler)
    print('http server is running...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
