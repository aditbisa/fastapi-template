from a2wsgi import ASGIMiddleware

from .main import app


wsgi_app = ASGIMiddleware(app)
