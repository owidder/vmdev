import webapp2

class HelloWorld(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('Hello ' + self.request.get('name'))

application = webapp2.WSGIApplication([
    ('/', HelloWorld)
], debug=True)
