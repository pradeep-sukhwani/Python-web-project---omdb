import webapp2
import helper_functions as helper

form_omdb="""
<html>
    <body style="background-color: grey">
        <form method="post">

            <div class="title">
            <h1><center>OMDB</center></h1>
            <h1><center>(Open Movie Database)<center><h1>
            </div>

            <div class="information">
            <div class="information" style="margin-left: 500px;">
            <label> 
            <h4>Find Movies</h4> <input type="text" name="movie" value="%(user_input)s">
            </label>

            <br>
            <br>
            <input type="submit">
            </div>
        </form>
    </body>
</html>
"""


class Movie(webapp2.RequestHandler):
    def write_form(self, form_input=""):
        self.response.out.write(form_omdb % {"user_input": helper.escape_html(form_input)})

    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.write_form()

    def post(self):
        movie_name = self.request.get('movie')
        if not movie_name:
            self.write_form("No results found")
        else:
            self.redirect('/result?name=%s' % movie_name)

class ResultHandler(webapp2.RequestHandler):
    
    def get(self):
        movie_name = self.request.get('name')
        user_movie = helper.main_call(movie_name)
        self.response.out.write(user_movie)
        # movie_details = helper.main_call(movie_name)
        # organized_movie_details = helper.organise_movie_info(movie_details)
        # self.response.out.write(organized_movie_details)

app = webapp2.WSGIApplication([('/', Movie),
                               ('/result', ResultHandler)], debug=True)