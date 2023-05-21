from flask import Flask, render_template
app = Flask(__name__)

print(__name__)  # Wyświetlenie wartości zmiennej __name__

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/name/<name>')
def hello_name(name):
  return render_template('index.html',name=name)

if __name__ == '__main__':
  app.run()
