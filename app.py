import os
from flask import Flask, request, jsonify
#from flask_wtf.csrf import CSRFProtect
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

app = Flask(__name__)
#csrf = CSRFProtect(app)
groq = Groq(api_key=groq_api_key)


@app.route('/')
def index():
    return "Llama Helper"

@app.route('/get_chat_completion', methods=['POST'])
def get_chat_completion():
    data = request.json
    message = data['message']
        # Use the Groq SDK to get chat completion
    chat_completion = groq.chat.completions.create(
        model= "llama2-70b-4096",
        messages=[{"role": "user", "content": message}]
    )

    return jsonify({"completion": chat_completion.choices[0].message.content})

#    except ValueError as e:
#        return jsonify({"error": str(e)}), 400
#   except Exception as e:
#       return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8001)
