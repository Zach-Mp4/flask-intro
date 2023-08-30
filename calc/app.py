import operations
from flask import Flask, request

app = Flask(__name__)


@app.route("/<operation>")
def math(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(operations.funcs.get(operation)(a,b))


    
