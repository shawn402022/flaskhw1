from app import app

@app.route('/')
def home():
    return 'hello world'

@app.route('/about')
def about():
    return 'About'