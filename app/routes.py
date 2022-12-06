from app import app

@app.route('/')
def home():
    return 'hello world'

@app.route('/about')
def about():
    return 'About'


@app.route('/login')
def login():
    return 'login'

@app.route('/blog')
def blog():
    return 'blog'

@app.route('/register')
def register():
    return 'register'
