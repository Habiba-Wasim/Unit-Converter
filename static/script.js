
document.addEventListener("DOMContentLoaded", function () {
    const themeToggle = document.querySelector(".dark-mode-toggle");

    // Load dark mode preference
    if (localStorage.getItem("dark-mode") === "enabled") {
        document.body.classList.add("dark-mode");
        themeToggle.textContent = "🌙";
    }

    themeToggle.addEventListener("click", function () {
        document.body.classList.toggle("dark-mode");

        if (document.body.classList.contains("dark-mode")) {
            localStorage.setItem("dark-mode", "enabled");
            themeToggle.textContent = "🌙";
        } else {
            localStorage.removeItem("dark-mode");
            themeToggle.textContent = "☀️";
        }
    });
});

function convert() {
    let category = document.getElementById("category").value;
    let fromUnit = document.getElementById("fromUnit").value;
    let toUnit = document.getElementById("toUnit").value;
    let value = parseFloat(document.getElementById("value").value);
    
    fetch("/convert", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ category, from_unit: fromUnit, to_unit: toUnit, value })
    })
    .then(response => response.json())
    .then(data => { document.getElementById("result").value = data.converted_value; });
}

populateUnits();
