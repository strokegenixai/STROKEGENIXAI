# Sample Data Description

This folder is a placeholder for sample health data that will be used to train and test the StrokeGenixAI model in future versions. Currently, the model uses simulated data (see `src/stroke_detection_model.py` for details). 

## Planned Data Structure
- **File Format:** CSV or JSON
- **Fields:**
  - Age (integer)
  - Blood Pressure (integer, mmHg)
  - Cholesterol Level (integer, mg/dL)
  - Smoking Status (boolean)
  - Diabetes Status (boolean)
  - Additional fields like BMI, family history, etc., in future iterations.

## Future Plans
- Replace simulated data with anonymized real patient data.
- Ensure compliance with healthcare regulations (e.g., HIPAA).
- Use Solana blockchain to securely store and manage real data.
