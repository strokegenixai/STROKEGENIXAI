# Stroke Risk Factors Research Notes

This folder contains research notes and references that inform the development of StrokeGenixAI's AI model for stroke detection.

## Key Risk Factors for Stroke
Our model currently considers the following risk factors, based on established medical research:
- **Age:** Risk increases significantly after 60 years due to vascular changes (Source: American Heart Association).
- **Blood Pressure:** Hypertension (blood pressure > 160 mmHg) is a leading cause of stroke (Source: CDC Stroke Statistics).
- **Cholesterol Level:** High cholesterol (> 240 mg/dL) contributes to artery blockages (Source: National Institutes of Health).
- **Smoking:** Smoking doubles stroke risk by damaging blood vessels (Source: World Health Organization).
- **Diabetes:** Diabetes increases stroke risk by affecting blood sugar and vascular health (Source: American Diabetes Association).

## AI Model Design Considerations
- **Current Model:** The `StrokeDetectionModel` assigns weighted scores to each risk factor based on their relative impact on stroke likelihood. For example, high blood pressure has a higher weight (+40 points) due to its strong correlation with stroke risk.
- **Future Improvements:** We plan to incorporate additional risk factors, such as:
  - Family history of stroke.
  - Body Mass Index (BMI).
  - Lifestyle factors (e.g., physical activity, diet).
- **Machine Learning Transition:** Future models will use machine learning algorithms (e.g., logistic regression, neural networks) trained on real medical datasets to improve prediction accuracy.

## References
- American Heart Association: Stroke Risk Factors (https://www.heart.org/en/health-topics/stroke/stroke-risk-factors)
- CDC Stroke Statistics: Hypertension and Stroke (https://www.cdc.gov/stroke/facts.htm)
- National Institutes of Health: Cholesterol and Cardiovascular Disease (https://www.nih.gov/news-events/news-releases/high-cholesterol)
- World Health Organization: Smoking and Stroke (https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds))
- American Diabetes Association: Diabetes and Stroke Risk (https://www.diabetes.org/diabetes/complications/stroke)

We welcome contributions to expand our research and improve our model’s accuracy!
