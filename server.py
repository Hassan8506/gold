from flask import Flask, request, jsonify

app = Flask(__name__)

# استقبال البيانات وتحديث السعر
@app.route("/update-price", methods=["POST"])
def update_price():
    data = request.json
    print("Data received from local server:", data)
    return jsonify({"message": "Price updated successfully!"})

# للحصول على البيانات الحالية
@app.route("/get-price", methods=["GET"])
def get_price():
    return jsonify({
        "price_data": "Symbol: XAUUSD\nAsk: 2630.15000\nBid: 2629.97000\n"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
