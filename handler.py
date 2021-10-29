import tornado.ioloop
import tornado.web
import requests
import json

def get_meme():
  result = requests.get(url = 'https://meme-api.herokuapp.com/gimme')
  return result.json()

class MemesHandler(tornado.web.RequestHandler):
    def get(self):
        count = self.get_arguments("count")[0]
        data = []
        for x in range(int(count)):
            meme = get_meme()
            data.append(meme['url'])
        self.write(json.dumps(data))

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/memes", MemesHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()