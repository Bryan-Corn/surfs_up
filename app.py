# Import Flask dependency
from flask import Flask
# Create Flask App Instance
app = Flask(__name__)
# Create Flask Routes
@app.route('/')
def hello_wprld():
    return 'It Works!'

