from time import time

from app.User import User

# Date & Datetime Format Syntax: https://carbon.nesbot.com/docs/#api-localization
DEFAULT_DATE_FORMAT = 'D MMM YYYY'
DEFAULT_DATETIME_FORMAT = 'D MMM YYYY, HH:mm'

# // Direction, according to language
# // (left-to-right vs right-to-left)
HTML_DIRECTION = 'ltr'

""" HEAD 
"""
# Project name. Shown in the window title.
PROJECT_NAME = 'Backpack for Masonite'

#  When clicking on the admin panel's top-left logo/name,
#      where should the user be redirected?
#      The string below will be passed through the url() helper.
#      - default: '' (project root)
#      - alternative: 'admin' (the admin's dashboard)
HOME_LINK = ''

# Content of the HTML meta robots tag to prevent indexing and link following
META_ROBOTS_CONTENT = 'noindex, nofollow'

""" STYLES 
"""

# CSS files that are loaded in all pages, using Masonite's static() helper
STYLES = [
    'packages/backpack/base/css/bundle.css',

    # """
    #     // Here's what's inside the bundle:
    #     // 'packages/@digitallyhappy/backstrap/css/style.min.css',
    #     // 'packages/animate.css/animate.min.css',
    #     // 'packages/noty/noty.css',
    # """

    # Load the fonts separately (so that you can replace them at will):
    'packages/source-sans-pro/source-sans-pro.css',
    'packages/line-awesome/css/line-awesome.min.css',

    #
    # """
    #     // Example (the fonts above, loaded from CDN instead)
    #     // 'https://maxcdn.icons8.com/fonts/line-awesome/1.1/css/line-awesome-font-awesome.min.css',
    #     // 'https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,600,700,300italic,400italic,600italic',
    #
    #     // Example (load font-awesome instead of line-awesome):
    #     // 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.2/css/all.min.css',
    # """
]

# CSS files that are loaded in all pages, using Laravel's mix() helper
MIX_STYLES = [
# 'css/app.css' => '',
]

""" HEADER
"""

# Menu logo. You can replace this with an <img> tag if you have a logo.
PROJECT_LOGO = '<b>Backpack for Masonite</b>'

# Show / hide breadcrumbs on admin panel pages.
BREADCRUMBS = True

# Horizontal navbar classes. Helps make the admin panel look similar to your project's design.
HEADER_CLASS = 'app-header bg-light border-0 navbar'
"""
// For background colors use: bg-dark, bg-primary, bg-secondary, bg-danger, bg-warning, bg-success, bg-info, bg-blue, bg-light-blue, bg-indigo, bg-purple, bg-pink, bg-red, bg-orange, bg-yellow, bg-green, bg-teal, bg-cyan, bg-white
// For links to be visible on different background colors use: "navbar-dark", "navbar-light", "navbar-color"
"""

""" BODY
"""

# Body element classes.
BODY_CLASS = 'app aside-menu-fixed sidebar-lg-show'
# Try sidebar-hidden, sidebar-fixed, sidebar-compact, sidebar-lg-show

# Sidebar element classes.
SIDEBAR_CLASS = 'sidebar sidebar-pills bg-light'

""" FOOTER
"""

# Footer element classes.
FOOTER_CLASS = 'app-footer d-print-none'
"""
// hide it with d-none
// change background color with bg-dark, bg-primary, bg-secondary, bg-danger, bg-warning, bg-success, bg-info, bg-blue, bg-light-blue, bg-indigo, bg-purple, bg-pink, bg-red, bg-orange, bg-yellow, bg-green, bg-teal, bg-cyan, bg-white
"""

# Developer or company name. Shown in footer.
DEVELOPER_NAME = 'Mokhlas Hussein'

# Developer website. Link in footer. Type false if you want to hide it.
DEVELOPER_LINK = 'https://imokhles.com'

# Show powered by Backpack for Masonite in the footer? true/false
SHOW_POWERED_BY = True

""" SCRIPTES
"""

# JS files that are loaded in all pages, using Masonite's static() helper
SCRIPTS = [
    # Backstrap includes jQuery, Bootstrap, CoreUI, PNotify, Popper
    'packages/backpack/base/js/bundle.js',

    # """
    #     // examples (everything inside the bundle, loaded from CDN)
    #     // 'https://code.jquery.com/jquery-3.4.1.min.js',
    #     // 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js',
    #     // 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js',
    #     // 'https://unpkg.com/@coreui/coreui/dist/js/coreui.min.js',
    #     // 'https://cdnjs.cloudflare.com/ajax/libs/pace/1.0.2/pace.min.js',
    #     // 'https://unpkg.com/sweetalert/dist/sweetalert.min.js',
    #     // 'https://cdnjs.cloudflare.com/ajax/libs/noty/3.1.4/noty.min.js'
    #
    #     // examples (VueJS or React)
    #     // 'https://unpkg.com/vue@2.4.4/dist/vue.min.js',
    #     // 'https://unpkg.com/react@16/umd/react.production.min.js',
    #     // 'https://unpkg.com/react-dom@16/umd/react-dom.production.min.js',
    # """
]

# JS files that are loaded in all pages, using Masonite's static() helper
MIX_SCRIPTS = [

]

""" CACHE-BUSTING
"""

CACHEBUSTING_STRING = time()

""" Registration Open
    | Choose whether new users/admins are allowed to register.
    | This will show the Register button on the login page and allow access to the
    | Register functions in AuthController.
    |
    | By default the registration is open only on localhost.
"""
REGISTRATION_OPEN = True

""" Routing
    // The prefix used in all base routes (the 'admin' in admin/dashboard)
    // You can make sure all your URLs use this prefix by using the backpack_url() helper instead of url()
"""
ROUTE_PREFIX = 'admin'

"""
    // The web middleware (group) used in all base & CRUD routes
    // If you've modified your "web" middleware group (ex: removed sessions), you can use a different
    // route group, that has all the the middleware listed below in the comments.
"""
WEB_MIDDLEWARE = 'web'

# Or you can comment the above, and uncomment the complete list below.
# 'web_middleware' => [
#    \App\Http\Middleware\EncryptCookies::class,
#    \Illuminate\Cookie\Middleware\AddQueuedCookiesToResponse::class,
#    \Illuminate\Session\Middleware\StartSession::class,
#    \Illuminate\View\Middleware\ShareErrorsFromSession::class,
#    \App\Http\Middleware\VerifyCsrfToken::class,
#  ]

"""
    // Set this to false if you would like to use your own AuthController and PasswordController
    // (you then need to setup your auth routes manually in your routes.php file)
    // Warning: if you disable this, the password recovery routes (below) will be disabled too!
"""
SETUP_AUTH_ROUTES = True

"""
    // Set this to false if you would like to skip adding the password recovery routes
    // (you then need to manually define the routes in your web.php)
"""
SETUP_PASSWORD_RECOVERY_ROUTES = True

"""
    // Set this to false if you would like to skip adding the dashboard routes
    // (you then need to overwrite the login route on your AuthController)
"""
SETUP_DASHBOARD_ROUTES = True

"""
    // Set this to false if you would like to skip adding "my account" routes
    // (you then need to manually define the routes in your web.php)
"""
SETUP_MY_ACCOUNT_ROUTES = True

""" Authentication
"""

# Fully qualified namespace of the User model
USER_MODEL_FQN = User

"""
    // The classes for the middleware to check if the visitor is an admin
    // Can be a single class or an array of classes
"""
MIDDLEWARE_CLASS = [

]

# Alias for that middleware
MIDDLEWARE_KEY = 'admin'
# Note: It's recommended to use the backpack_middleware() helper everywhere, which pulls this key for you.

"""
    // Username column for authentication
    // The Backpack default is the same as the Laravel default (email)
    // If you need to switch to username, you also need to create that column in your db
"""
AUTHENTICATION_COLUMN = 'email'
AUTHENTICATION_COLUMN_NAME = 'Email'

"""
    // The guard that protects the Backpack admin panel.
    // If null, the config.auth.defaults.guard value will be used.
"""
GUARD = 'backpack'

"""
    // The password reset configuration for Backpack.
    // If null, the config.auth.defaults.passwords value will be used.
"""
PASSWORDS = 'backpack'

"""
    // What kind of avatar will you like to show to the user?
    // Default: gravatar (automatically use the gravatar for his email)
    // Other options:
    // - placehold (generic image with his first letter)
    // - example_method_name (specify the method on the User model that returns the URL)
"""
AVATAR_TYPE = 'gravatar'