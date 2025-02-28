# from flask import Flask, request, jsonify, render_template

# app = Flask(__name__)

# # Conversion factors
# units = {
#     "length": {
#         "Meter": 1,
#         "Centimeter": 100,
#         "Kilometer": 0.001,
#         "Inch": 39.3701,
#         "Foot": 3.28084,
#         "Yard": 1.09361,
#         "Mile": 0.000621371,
#     },
#     "weight": {
#         "Gram": 1,
#         "Kilogram": 0.001,
#         "Pound": 0.00220462,
#         "Ounce": 0.035274,
#         "Ton": 0.000001,
#     },
#     "temperature": {}
# }

# history = []

# def save_history(entry):
#     history.insert(0, entry)
#     if len(history) > 5:
#         history.pop()

# def convert(category, from_unit, to_unit, value):
#     if category == "temperature":
#         if from_unit == "Celsius" and to_unit == "Fahrenheit":
#             return (value * 9) / 5 + 32
#         elif from_unit == "Fahrenheit" and to_unit == "Celsius":
#             return ((value - 32) * 5) / 9
#         elif from_unit == "Celsius" and to_unit == "Kelvin":
#             return value + 273.15
#         elif from_unit == "Kelvin" and to_unit == "Celsius":
#             return value - 273.15
#         else:
#             return value
#     else:
#         return (value * units[category][to_unit]) / units[category][from_unit]

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/convert", methods=["POST"])
# def convert_units():
#     data = request.json
#     category = data["category"]
#     from_unit = data["from_unit"]
#     to_unit = data["to_unit"]
#     value = data["value"]
    
#     result = convert(category, from_unit, to_unit, value)
#     entry = f"{value} {from_unit} = {round(result, 2)} {to_unit}"
#     save_history(entry)
    
#     return jsonify({"converted_value": round(result, 2), "history": history})

# @app.route("/history")
# def get_history():
#     return jsonify({"history": history})

# if __name__ == "__main__":
#     app.run(debug=True)








# from fastapi import FastAPI
# from pydantic import BaseModel
# from langchain_openai import OpenAI
# from dotenv import load_dotenv
# import os
# import json

# # Load environment variables
# load_dotenv()
# api_key = os.getenv("OPENAI_API_KEY")

# app = FastAPI()
# llm = OpenAI(api_key=api_key)  # API key from .env

# # Conversion factors
# units = {
#     "length": {
#         "Meter": 1,
#         "Centimeter": 100,
#         "Kilometer": 0.001,
#         "Inch": 39.3701,
#         "Foot": 3.28084,
#         "Yard": 1.09361,
#         "Mile": 0.000621371,
#         "Millimeter": 1000,
#         "Micrometer": 1000000,
#         "Nanometer": 1000000000,
#     },
#     "weight": {
#         "Gram": 1,
#         "Kilogram": 0.001,
#         "Pound": 0.00220462,
#         "Ounce": 0.035274,
#         "Ton": 0.000001,
#         "Milligram": 1000,
#         "Microgram": 1000000,
#     },
#     "temperature": {}  # Special case handled in function
# }

# history = []

# def save_history(entry):
#     history.insert(0, entry)
#     if len(history) > 5:
#         history.pop()

# def clear_history():
#     history.clear()

# class ConversionRequest(BaseModel):
#     category: str
#     from_unit: str
#     to_unit: str
#     value: float

# def convert(category: str, from_unit: str, to_unit: str, value: float):
#     if category == "temperature":
#         if from_unit == "Celsius" and to_unit == "Fahrenheit":
#             return (value * 9) / 5 + 32
#         elif from_unit == "Fahrenheit" and to_unit == "Celsius":
#             return ((value - 32) * 5) / 9
#         elif from_unit == "Celsius" and to_unit == "Kelvin":
#             return value + 273.15
#         elif from_unit == "Kelvin" and to_unit == "Celsius":
#             return value - 273.15
#         elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
#             return ((value - 32) * 5) / 9 + 273.15
#         elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
#             return ((value - 273.15) * 9) / 5 + 32
#         else:
#             return value
#     else:
#         return (value * units[category][to_unit]) / units[category][from_unit]

# @app.post("/convert")
# def convert_units(request: ConversionRequest):
#     result = convert(request.category, request.from_unit, request.to_unit, request.value)
#     entry = f"{request.value} {request.from_unit} = {round(result, 2)} {request.to_unit}"
#     save_history(entry)
#     return {"converted_value": round(result, 2), "history": history}

# @app.get("/history")
# def get_history():
#     return {"history": history}

# @app.delete("/history")
# def delete_history():
#     clear_history()
#     return {"message": "History cleared."}

# @app.post("/explain")
# def explain_conversion(request: ConversionRequest):
#     prompt = f"Explain why {request.value} {request.from_unit} equals {convert(request.category, request.from_unit, request.to_unit, request.value)} {request.to_unit}."
#     response = llm.invoke(prompt)  # Updated method
#     return {"explanation": response}

# # Run using: uvicorn app:app --reload














# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, render_template

# app = Flask(__name__, static_folder="static", template_folder="templates")

# @app.route("/")
# def home():
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)






































from flask import Flask, render_template, request, jsonify # type: ignore
import os
from waitress import serve  # type: ignore # Use Waitress for production deployment

app = Flask(__name__)

# Conversion factors
units = {
    "length": {
        "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000,
        "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701
    },
    "weight": {
        "Gram": 1, "Kilogram": 0.001, "Pound": 0.00220462, "Ounce": 0.035274, "Ton": 0.000001
    },
    "temperature": {}
}

# Function to convert units
def convert(category, from_unit, to_unit, value):
    if category == "temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        else:
            return value  # Same unit
    else:
        return (value * units[category][to_unit]) / units[category][from_unit]

# Home route (renders the HTML page)
@app.route("/")
def home():
    return render_template("index.html")

# API route for conversion
@app.route("/convert", methods=["POST"])
def convert_units():
    try:
        data = request.json
        category = data.get("category")
        from_unit = data.get("from_unit")
        to_unit = data.get("to_unit")
        value = float(data.get("value"))

        if category not in units or from_unit not in units[category] or to_unit not in units[category]:
            return jsonify({"error": "Invalid unit selection"}), 400

        result = convert(category, from_unit, to_unit, value)
        return jsonify({"converted_value": round(result, 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Deployment Fix: Use Waitress for Cloud Hosting (Render/Vercel/Heroku)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use environment port or default 5000
    serve(app, host="0.0.0.0", port=8501)
