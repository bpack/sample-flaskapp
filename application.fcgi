#!/home/user/virtualenv/venv_name/3.5/bin/python
from flup.server.fcgi import WSGIServer
from flaskapp import create_app

if __name__ == '__main__':
    app = create_app()
    WSGIServer(app).run()

