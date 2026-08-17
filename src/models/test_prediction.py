import pandas as pd

from src.models.predict import predict_purchase


sample = pd.DataFrame([{
    "Administrative": 2,
    "Administrative_Duration": 50.0,
    "Informational": 1,
    "Informational_Duration": 20.0,
    "ProductRelated": 10,
    "ProductRelated_Duration": 500.0,
    "BounceRates": 0.02,
    "ExitRates": 0.05,
    "PageValues": 10.0,
    "SpecialDay": 0.0,
    "Month": "Nov",
    "OperatingSystems": 2,
    "Browser": 2,
    "Region": 1,
    "TrafficType": 2,
    "VisitorType": "Returning_Visitor",
    "Weekend": False,
    "TotalPages": 13,
    "TotalDuration": 570.0,
    "AvgTimePerPage": 43.85,
    "ProductEngagementRatio": 0.77,
    "ProductTimeRatio": 0.88,
}])


prediction, probability = predict_purchase(sample)

print("Prediction:", prediction[0])
print("Purchase probability:", probability[0])
