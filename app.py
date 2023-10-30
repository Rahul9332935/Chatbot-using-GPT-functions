from flask import Flask, jsonify, request,render_template
from dataAI import run_conversation 


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("chatbot.html")

@app.route("/api/chat",methods=['POST'])
def chat_bot():
  query= request.json
  response = run_conversation(query['data'])
  return jsonify({"response": response})

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080, debug=True)
