from flask import Flask, request, jsonify, render_template
 
 
app = Flask(__name__, static_folder='public', template_folder='views')
 
 
@app.route('/')
def index():
    return render_template('index.html')
 
 
 
if __name__ == '__main__':

    app.run(debug=True)