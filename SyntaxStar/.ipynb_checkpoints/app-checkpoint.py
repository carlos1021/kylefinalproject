from flask import Flask, render_template, send_from_directory
import os
app = Flask(__name__)

# Define a route to serve your index.html file
@app.route('/')
def index():
    return render_template('index.html')

# Define a route to serve other HTML files
@app.route('/<filename>')
def serve_html(filename):
    return render_template(filename)

# Define a route to serve CSS and JS files from the respective folders
@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('css', filename)

@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('js', filename)

@app.route('/img/<path:filename>')
def serve_image(filename):
    return send_from_directory('img', filename)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico')

if __name__ == '__main__':
    app.run(debug=True)
