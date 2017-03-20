#!/usr/bin/env python
import os
from random import randint
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)

def main():
    ljubljana = GlavnoMesto("Ljubljana", "Slovenija","/assets/images/ljubljana.jpg")
    zagreb = GlavnoMesto("Zagreb", "Hrvaska", "/assets/images/zagreb.jpg")
    dunaj = GlavnoMesto("Dunaj", "Avstrija", "/assets/images/vienna.jpg")
    rim = GlavnoMesto("Rim", "Italija", "/assets/images/rome.jpg")
    berlin = GlavnoMesto("Berlin", "Nemcija", "/assets/images/berlin.jpg")
    paris = GlavnoMesto("Paris", "Francija", "/assets/images/paris.jpg")
    amsterdam = GlavnoMesto("Amsterdam", "Nizozemska", "/assets/images/amsterdam.jpg")
    return [ljubljana, zagreb, dunaj, rim, berlin, paris, amsterdam]

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

class GlavnoMesto():
    def __init__(self,glavno_mesto, drzava, slika):
        self.glavno_mesto = glavno_mesto
        self.drzava = drzava
        self.slika = slika

class MainHandler(BaseHandler):
    def get(self):
        glavno_mesto = main()[randint(0, 6)]
        spremenljivka = {"glavno_mesto": glavno_mesto}
        return self.render_template("index.html", spremenljivka)

class RezultatHandler(BaseHandler):
    def post(self):
        odgovor = self.request.get("odgovor")
        drzava = self.request.get("drzava")

        glavna_mesta = main()
        for mesto in glavna_mesta:
            if mesto.drzava == drzava:
                if mesto.glavno_mesto.lower() == odgovor.lower():
                    rezultat = True
                else:
                    rezultat = False

                izpis = {"rezultat": rezultat, "mesto": mesto}
                return self.render_template("rezultat.html", izpis)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/rezultat', RezultatHandler),
], debug=True)