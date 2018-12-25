from app.models import URL
 
 
def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
    user = User('patkennedy79@gmail.com', 'FlaskIsAwesome')
    assert new_user.email == 'patkennedy79@gmail.com'
    assert new_user.hashed_password != 'FlaskIsAwesome'
    assert not new_user.authenticated
    assert new_user.role == 'user'
    """
    url = URL(original_url='http://www.google.com', short_url='iffgg')
    assert url.original_url == 'http://www.google.com'
    assert url.short_url == 'iffgg'
    print(url)


    
