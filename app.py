from flask import Flask, render_template
from flask_assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

# Define the SASS bundle
sass_bundle = Bundle('sass/pages/main.scss', filters='libsass', output='gen/main.css')

# Register the SASS bundle
assets.register('sass_bundle', sass_bundle)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project1')
def project1():
    return render_template('project1.html')

@app.route('/project2')
def project2():
    return render_template('project2.html')

if __name__ == '__main__':
    app.run(debug=True)
