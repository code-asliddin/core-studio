import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')

# API Sozlamalari
import os API_KEY = os.getenv("GROQ_API_KEY")
URL = "https://api.groq.com/openai/v1/chat/completions"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    user_query = request.form.get('query')
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": "Sen aqlli va foydali yordamchisan. Faqat o'zbek tilida javob ber."},
            {"role": "user", "content": user_query}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(URL, headers=headers, json=data)
        res_json = response.json()
        
        if 'choices' in res_json:
            answer = res_json['choices'][0]['message']['content']
            return jsonify({"result": answer})
        else:
            # Xatolikni aniqroq ko'rsatish
            msg = res_json.get('error', {}).get('message', 'Noma\'lum xato')
            return jsonify({"result": f"Xatolik: {msg}"})
    except Exception as e:
        return jsonify({"result": f"Tizim xatosi: {str(e)}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

