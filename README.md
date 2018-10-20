# DJP
## Documenting the creation process

- `django-admin startproject [name]`
The first command you always run. This produces a series of directories and python files.
1. manage.py
CLI utility that lets you interact with the project
2. inner [site]
package used for imports e.g. [site].urls
3. __init__.py
Tells python that the dir should be considered a package
4. settings.py
Project settings and configuration
5. urls.py
URL declarations for project
6. wsgi.py

### Running Server
Once in the outer [site] directory (whichever has manage.py) run `python manage.py runserver [port]`. You can now visit the debug page.
