# DJP
## Documenting the creation process

- `django-admin startproject [name]`
The first command you always run. This produces a series of directories and python files.
1. manage.py
CLI utility that lets you interact with the project
2. inner [site]
package used for imports e.g. `[site].urls`
3. __init__.py
Tells python that the dir should be considered a package
4. settings.py
Project settings and configuration
5. urls.py
URL declarations for project
6. wsgi.py

### Running Server
Once in the outer [site] directory (whichever has manage.py) run `python manage.py runserver [port]`. You can now visit the debug page.

### Starting a new app
A project is a collection of apps. Each different aspect of your webapp is an app. to make a new app, run `python manage.py startapp [app name]`. This will lay out a new directory named `[app name]`;

### Writing a view
A view is what the user sees. Once you have defined your view in `views.py`, you need to map the the view to a URL, for which we need a URL conf. Create it in the `[app name]` directory. Next, you need to to point the root URL confs to the `[app name]` module.

Once you have done that, navigating to that URL should return the HttpResponse. 
