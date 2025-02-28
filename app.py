
import streamlit as st

# Set page config (title + layout)
st.set_page_config(page_title="Unit Converter", layout="centered")

# Available Units
units = {
    "Length": {
        "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000,
        "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701
    },
    "Weight": {
        "Gram": 1, "Kilogram": 0.001, "Pound": 0.00220462, "Ounce": 0.035274, "Ton": 0.000001
    },
    "Temperature": {
        "Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"
    }
}

# Conversion Logic
def convert(category, from_unit, to_unit, value):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        else:
            return value
    else:
        return (value * units[category][to_unit]) / units[category][from_unit]

# UI Layout
st.title("🔢 Unit Converter")

# Sidebar for category selection
category = st.sidebar.selectbox("Select Category", list(units.keys()))

# Dropdowns for unit selection
col1, col2, col3 = st.columns(3)
with col1:
    from_unit = st.selectbox("From", list(units[category].keys()))
with col2:
    st.write("➡")
with col3:
    to_unit = st.selectbox("To", list(units[category].keys()))

# Input field for value
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

# Convert button
if st.button("Convert"):
    result = convert(category, from_unit, to_unit, value)
    st.success(f"Converted Value: {round(result, 2)} {to_unit}")

