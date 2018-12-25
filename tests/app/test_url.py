from app.models import URL
 
 
def test_new_user():
    url = URL(original_url='http://www.google.com', short_url='iffgg')
    assert url.original_url == 'http://www.google.com'
    assert url.short_url == 'iffgg'


    
