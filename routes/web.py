"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome').middleware('auth'),

    # Blog Routes
    Get('/blog', 'BlogController@show').middleware('auth'),
    Post('/blog/create', 'BlogController@store').middleware('auth'),
]

from masonite.auth import Auth 
ROUTES += Auth.routes()
