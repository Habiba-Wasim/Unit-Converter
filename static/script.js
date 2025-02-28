// function convert() {
//     let category = document.getElementById("category").value;
//     let fromUnit = document.getElementById("fromUnit").value;
//     let toUnit = document.getElementById("toUnit").value;
//     let value = parseFloat(document.getElementById("value").value);
    
//     let conversionFactors = {
//         "length": { "Meter": 1, "Kilometer": 0.001, "Centimeter": 100 },
//         "weight": { "Gram": 1, "Kilogram": 0.001, "Pound": 0.00220462 },
//         "temperature": { "Celsius": 1, "Fahrenheit": 33.8, "Kelvin": 274.15 }
//     };
    
//     let result = (value * conversionFactors[category][toUnit]) / conversionFactors[category][fromUnit];
//     document.getElementById("result").innerText = `Converted Value: ${result.toFixed(2)} ${toUnit}`;
// }

// function toggleDarkMode() {
//     document.body.classList.toggle("dark-mode");
// }











































const units = {
    length: { "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701 },
    weight: { "Gram": 1, "Kilogram": 0.001, "Pound": 0.00220462, "Ounce": 0.035274, "Ton": 0.000001 },
    temperature: { "Celsius": 1, "Fahrenheit": 33.8, "Kelvin": 274.15 }
};

function populateUnits() {
    let category = document.getElementById("category").value;
    let fromUnit = document.getElementById("fromUnit");
    let toUnit = document.getElementById("toUnit");
    fromUnit.innerHTML = toUnit.innerHTML = "";
    for (let unit in units[category]) {
        fromUnit.innerHTML += `<option value="${unit}">${unit}</option>`;
        toUnit.innerHTML += `<option value="${unit}">${unit}</option>`;
    }
}

function convert() {
    let category = document.getElementById("category").value;
    let fromUnit = document.getElementById("fromUnit").value;
    let toUnit = document.getElementById("toUnit").value;
    let value = parseFloat(document.getElementById("value").value);
    let result = 0;

    if (category === "temperature") {
        if (fromUnit === "Celsius" && toUnit === "Fahrenheit") {
            result = (value * 9/5) + 32;
        } else if (fromUnit === "Fahrenheit" && toUnit === "Celsius") {
            result = (value - 32) * 5/9;
        } else if (fromUnit === "Celsius" && toUnit === "Kelvin") {
            result = value + 273.15;
        } else if (fromUnit === "Kelvin" && toUnit === "Celsius") {
            result = value - 273.15;
        } else {
            result = value;
        }
    } else {
        result = (value * units[category][toUnit]) / units[category][fromUnit];
    }
    document.getElementById("result").value = result.toFixed(2);
}

function clearFields() {
    document.getElementById("value").value = "";
    document.getElementById("result").value = "";
}

function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
    let button = document.querySelector(".dark-mode-toggle");
    button.textContent = document.body.classList.contains("dark-mode") ? "🌙" : "☀️";
}

function showFormula() {
    alert("Formula: Multiply or divide the value according to the selected unit conversion.");
}

populateUnits();
