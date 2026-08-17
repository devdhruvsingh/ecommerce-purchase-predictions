const form = document.getElementById("predictionForm");

const result = document.getElementById("result");
const predictionText = document.getElementById("prediction");
const probabilityText = document.getElementById("probability");

const error = document.getElementById("error");


form.addEventListener("submit", async function (event) {

    event.preventDefault();

    result.classList.add("hidden");
    error.classList.add("hidden");


    const data = {

        Administrative: Number(
            document.getElementById("Administrative").value
        ),

        Administrative_Duration: Number(
            document.getElementById("Administrative_Duration").value
        ),

        Informational: Number(
            document.getElementById("Informational").value
        ),

        Informational_Duration: Number(
            document.getElementById("Informational_Duration").value
        ),

        ProductRelated: Number(
            document.getElementById("ProductRelated").value
        ),

        ProductRelated_Duration: Number(
            document.getElementById("ProductRelated_Duration").value
        ),

        BounceRates: Number(
            document.getElementById("BounceRates").value
        ),

        ExitRates: Number(
            document.getElementById("ExitRates").value
        ),

        PageValues: Number(
            document.getElementById("PageValues").value
        ),

        SpecialDay: Number(
            document.getElementById("SpecialDay").value
        ),

        Month: document.getElementById("Month").value,

        OperatingSystems: Number(
            document.getElementById("OperatingSystems").value
        ),

        Browser: Number(
            document.getElementById("Browser").value
        ),

        Region: Number(
            document.getElementById("Region").value
        ),

        TrafficType: Number(
            document.getElementById("TrafficType").value
        ),

        VisitorType: document.getElementById("VisitorType").value,

        Weekend:
            document.getElementById("Weekend").value === "true",

        TotalPages: Number(
            document.getElementById("TotalPages").value
        ),

        TotalDuration: Number(
            document.getElementById("TotalDuration").value
        ),

        AvgTimePerPage: Number(
            document.getElementById("AvgTimePerPage").value
        ),

        ProductEngagementRatio: Number(
            document.getElementById("ProductEngagementRatio").value
        ),

        ProductTimeRatio: Number(
            document.getElementById("ProductTimeRatio").value
        )
    };


    try {

        const response = await fetch(
            "https://ecommerce-purchase-api.onrender.com",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(data)
            }
        );


        const responseData = await response.json();


        if (!response.ok) {

            error.textContent =
                responseData.error || "Something went wrong.";

            error.classList.remove("hidden");

            return;
        }


        predictionText.textContent =
            responseData.prediction
                ? "Purchase predicted: YES"
                : "Purchase predicted: NO";


        probabilityText.textContent =
            "Purchase probability: " +
            (responseData.purchase_probability * 100).toFixed(2) +
            "%";


        result.classList.remove("hidden");

    }

    catch (err) {

        error.textContent =
            "Could not connect to the prediction API.";

        error.classList.remove("hidden");

    }

});