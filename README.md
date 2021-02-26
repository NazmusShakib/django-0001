# django-p1
## _This let you work quickly, Ever_
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

django-p1 is a cloud-enabled, mobile-ready, offline-storage compatible,
django-powered web project.

✨Magic ✨


## Features

- Import a HTML file and watch it magically convert to Markdown
- Drag and drop images (requires your Dropbox account be linked)
- Import and save files from GitHub, Dropbox, Google Drive and One Drive
- Drag and drop markdown and HTML files into Django-p1
- Export documents as Markdown, HTML and PDF


## Tech

This project uses Django v2.2.4 and uses a number of open source modules to work properly:

- [Python] - lets you work quickly and integrate systems more effectively!
- [MySQL] - fully managed database service
- [markdown-it] - Markdown parser done right. Fast and easy to extend.
- [Twitter Bootstrap] - great UI boilerplate for modern web apps
- [Gulp] - the streaming build system
- [Breakdance](https://breakdance.github.io/breakdance/) - HTML
to Markdown converter
- [jQuery] - duh


## Installation

Django-p1 requires [python](https://www.python.org/downloads/) v3+ to run.

Install the dependencies and devDependencies and start the server.

```sh
git clone https://github.com/NazmusShakib/django-0001.git
cd django-0001
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

![django-01](/static/img/sample-done.png "Simply done - magic")

For production environments...

```sh
$
```

## Plugins

Django-p1 is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

## Development

Want to contribute? Great!


#### Building for source

For production release:


## Docker

Django-p1 is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.


## License

MIT

**Free Software, Hell Yeah!**