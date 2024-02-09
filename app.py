from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = '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'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    message = request.json.get("message")
    
    if message.lower() == "hi":
        return "Hi Mathew! How can I assist you?"
    if message.lower() == "what is 5*7":
        return "5*7 = 35"
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message}
        ]
    )
    
    if completion.choices[0].message is not None:
        return completion.choices[0].message
    else:
        return 'Failed to generate response!'

if __name__ == '__main__':
    app.run()
