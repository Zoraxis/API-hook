from flask import Flask, request, jsonify
from lingua import Language, LanguageDetectorBuilder

languages = [Language.ENGLISH, Language.GERMAN]
detector = LanguageDetectorBuilder.from_languages(*languages).build()

app = Flask(__name__)

def getLangData(text):
    confidence = detector.compute_language_confidence_values(text)[0]
    isEnglish = confidence.language == Language.ENGLISH
    response = {"isEnglish": isEnglish, "language": confidence.language.name, "confidence": confidence.value}
    print(response)
    return response

@app.route('/lang-detect', methods=['POST'])
def handle_post():
    data = request.get_json()
    text = data["detailedMessage"]["text"]
    response = getLangData(text)
    return jsonify(response), 200

@app.route('/', methods=['GET'])
def handle_get():
    data = {"message": "TEST"} 
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)