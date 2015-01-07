from flask import Flask
from cms.views import cms

app = Flask(__name__)
app.register_blueprint(cms, url_prefix='/admin') 
app.register_blueprint(logger,url_prefix='/analytics')