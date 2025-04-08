from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    a = request.args.get('a', default=0, type=float)
    b = request.args.get('b', default=0, type=float)

    suma = a + b
    prediction = 1 if suma > 5.8 else 0

    return jsonify({
        "features": {"a": a, "b": b},
        "prediction": prediction
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
