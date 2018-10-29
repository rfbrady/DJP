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

### Database / models
The default db configuration is sqlite, but this can be changed in `[app name]/settings.py`. Also, take a look at the default installed applications to get an idea of what an application is in the D framework. Since some of these apps use databases, lets initialize them with the command `python manage.py migrate`.

Models represent the fields and behaviors, and layout of your database/data. Once you've created a new model, make sure that your new application is installed in `settings.py`. Then run the command `python manage.py makemigrations [app name]`. Typically `migrate` will manage your dbs for you, but you can check with the command `sqlmigrate [app name] [migrate #]`. The command `check` will check for errors before you migrate.
1. `makemigrations`
2. `migrate`

### Shell / API
Use `manage.py shell` to invoke the python shell. This uses your django package as the local environment, so you can interact with your models etc. You will need to `[object].save()` any change you make to the db in the shell. `[Model].objects.all()` returns a query set that you can iterate over.

#RCT
### Tic Tac Toe in RCT
Learning the fundamentals of RCT by building a tic tac toe app. Begin by removing anything that comes preloaded in the src directory `rm -f src/*`


The entirety of this readme are based on tutorials that are written officially by Django and React, and can be found at (django link here),https://reactjs.org/tutorial/tutorial.html
