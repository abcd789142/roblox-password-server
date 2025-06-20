from flask import Flask, request
     from serverless_wsgi import handle_request

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

     # Vercel serverless 入口
     def handler(event, context):
         return handle_request(app, event, context)
