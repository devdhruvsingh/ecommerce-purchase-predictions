const API_URL = "https://ecommerce-purchase-api.onrender.com/predict";

const form = document.getElementById("prediction-form");
const resultContainer = document.getElementById("result");
const predictionElement = document.getElementById("prediction");
const probabilityElement = document.getElementById("probability");
const errorElement = document.getElementById("error");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    // Hide previous result messages
    resultContainer.classList.add("hidden");
    errorElement.classList.add("hidden");

    // Get form data
    const formData = new FormData(form);

    // Safely extract numeric and string fields
    const getNum = (key) => {
        const val = formData.get(key);
        return val !== null && val !== "" ? Number(val) : 0;
    };

    const getStr = (key) => (formData.get(key) || "").toString();

    // Create payload object matching the backend model inputs
    const data = {
        Administrative: getNum("Administrative"),
        Administrative_Duration: getNum("Administrative_Duration"),
        Informational: getNum("Informational"),
        Informational_Duration: getNum("Informational_Duration"),
        ProductRelated: getNum("ProductRelated"),
        ProductRelated_Duration: getNum("ProductRelated_Duration"),
        BounceRates: getNum("BounceRates"),
        ExitRates: getNum("ExitRates"),
        PageValues: getNum("PageValues"),
        SpecialDay: getNum("SpecialDay"),
        Month: getStr("Month"),
        OperatingSystems: getNum("OperatingSystems"),
        Browser: getNum("Browser"),
        Region: getNum("Region"),
        TrafficType: getNum("TrafficType"),
        VisitorType: getStr("VisitorType"),
        Weekend: formData.get("Weekend") === "true" || formData.get("Weekend") === "on",
        TotalPages: getNum("TotalPages"),
        TotalDuration: getNum("TotalDuration"),
        AvgTimePerPage: getNum("AvgTimePerPage"),
        ProductEngagementRatio: getNum("ProductEngagementRatio"),
        ProductTimeRatio: getNum("ProductTimeRatio")
    };

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        // Parse json payload safely
        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.error || result.message || `HTTP ${response.status} Error`);
        }

        // Display prediction statement
        const isPurchase = result.prediction === true || result.prediction === 1;
        predictionElement.textContent = isPurchase ? "Purchase Likely" : "Purchase Unlikely";

        // Display probability score safely
        const rawProb = result.purchase_probability ?? result.probability ?? 0;
        const probability = Number(rawProb) * 100;
        probabilityElement.textContent = `Purchase Probability: ${probability.toFixed(2)}%`;

        // Show result section
        resultContainer.classList.remove("hidden");

    } catch (error) {
        console.error("Prediction API Error:", error);

        errorElement.textContent = `Error: ${error.message}`;
        errorElement.classList.remove("hidden");
    }
});