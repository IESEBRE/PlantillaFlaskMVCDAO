import atexit

from flask import Flask

app = Flask(__name__)

# Register blueprints
controler=None  #ElMeuController('blueprint', __name__, template_folder='view/templates') --> controlador que posarem al paquet dels controller
app.register_blueprint(controler)

@atexit.register
def save():
    controler.save()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
