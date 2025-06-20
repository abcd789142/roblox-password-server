from flask import Flask, request

app = Flask(__name__)
password = "123456"  # 初始密码

@app.route('/password', methods=['GET'])
def get_password():
    return password

@app.route('/password', methods=['POST'])
def set_password():
    global password
    password = request.data.decode('utf-8')
    return "Password updated"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)