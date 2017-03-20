#!/usr/bin/env python
import os
import jinja2
import webapp2
from datetime import datetime

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)

def datum_in_ura():
    ustvari_datum_in_ura = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    return ustvari_datum_in_ura

class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        izpis_datum_in_ura = datum_in_ura()
        izpis = {
            "datum_in_ura": izpis_datum_in_ura
        }
        return self.render_template("hello.html", izpis)

class OmeniHandler(BaseHandler):
    def get(self):
        izpis_datum_in_ura = datum_in_ura()
        izpis = {
            "datum_in_ura": izpis_datum_in_ura
        }
        return self.render_template("o_meni.html", izpis)

class MojiprojektiHandler(BaseHandler):
    def get(self):
        izpis_datum_in_ura = datum_in_ura()
        izpis = {
            "datum_in_ura": izpis_datum_in_ura
        }
        return self.render_template("moji_projekti.html", izpis)

class BlogHandler(BaseHandler):
    def get(self):
        izpis_datum_in_ura = datum_in_ura()
        izpis = {
            "datum_in_ura": izpis_datum_in_ura
        }
        return self.render_template("blog.html", izpis)

class KontaktHandler(BaseHandler):
    def get(self):
        izpis_datum_in_ura = datum_in_ura()
        izpis = {
            "datum_in_ura": izpis_datum_in_ura
        }
        return self.render_template("kontakt.html", izpis)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/o_meni', OmeniHandler),
    webapp2.Route('/moji_projekti', MojiprojektiHandler),
    webapp2.Route('/blog', BlogHandler),
    webapp2.Route('/kontakt', KontaktHandler),
], debug=True)
