from flask import render_template, request

def register_routes(app, db, bcrypt):

    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')