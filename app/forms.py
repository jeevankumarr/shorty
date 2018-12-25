import wtforms
from wtforms import validators
# from flask_wtf.recaptcha import RecaptchaField


class UrlForm(wtforms.Form):
    original_url = wtforms.StringField('',validators=[validators.DataRequired(' If URL\'s were that short, would you even be here?')])
    # recaptcha = RecaptchaField()

    def save_url(self, url):
        
        self.populate_obj(url)
        
        if not "http" in url.original_url:
            url.original_url = "http://" + url.original_url
        if not "." in url.original_url:
            url.original_url = url.original_url + ".com/"
        return url

