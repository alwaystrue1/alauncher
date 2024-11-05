from flask import Flask, send_from_directory, request

app = Flask(__name__)

@app.route('/')
def home():
    if request.args.get('minecraft') == 'yes':
        return send_from_directory('serverfiles', 'minecraft.html')
    else:
        return send_from_directory('serverfiles', "sw.html")
if __name__ == '__main__':
    app.run(port=4000)