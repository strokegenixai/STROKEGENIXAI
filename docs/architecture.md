# StrokeGenixAI Architecture

## Overview
StrokeGenixAI is a platform designed to enable early stroke detection using AI and the Solana blockchain. The system combines AI-driven predictive analytics with blockchain technology to provide a secure, decentralized, and efficient solution for healthcare providers and patients. The current version includes a simulated AI model, with plans to integrate real medical data, improve the model, and build a full platform for healthcare interaction.

## System Architecture

### 1. Data Layer
The data layer is responsible for collecting and managing health data used for stroke risk prediction.

- **Current Implementation (Simulated Data):**
  - The `StrokeDetectionModel` class simulates health data with the following attributes:
    - Age: Randomly generated between 20 and 80.
    - Blood Pressure: Randomly generated between 110 and 180 mmHg.
    - Cholesterol Level: Randomly generated between 150 and 250 mg/dL.
    - Smoking Status: Randomly set as True or False.
    - Diabetes Status: Randomly set as True or False.
  - Code snippet from `stroke_detection_model.py`:
    ```python
    def load_data(self):
        return {
            "age": random.randint(20, 80),
            "blood_pressure": random.randint(110, 180),
            "cholesterol_level": random.randint(150, 250),
            "smoking": random.choice([True, False]),
            "diabetes": random.choice([True, False])
        }
    ```
- **Future Plans:**
  - Replace simulated data with real patient data sourced from healthcare providers.
  - Ensure data privacy and security by storing encrypted data on the Solana blockchain.
  - Implement data preprocessing pipelines to clean and standardize medical data for AI analysis.

### 2. AI Model Layer
The AI model layer processes health data to predict stroke risk.

- **Current Implementation (Simulated Model):**
  - The `predict_risk` method in `StrokeDetectionModel` calculates a risk score based on weighted factors:
    - Age > 60: +30 points
    - Blood Pressure > 160: +40 points
    - Cholesterol Level > 240: +20 points
    - Smoking: +25 points
    - Diabetes: +15 points
  - The `run_model` method evaluates the risk score and categorizes it into:
    - Low Risk: Score ≤ 50
    - Moderate Risk: Score 51–80
    - High Risk: Score > 80
  - Example output:
    ```
    Low risk detected. Risk Score: 45
    Moderate risk detected. Risk Score: 65
    Warning: High stroke risk detected! Risk Score: 95
    ```
- **Future Plans:**
  - Replace the rule-based model with a machine learning model (e.g., logistic regression, neural networks) trained on real medical datasets.
  - Incorporate additional risk factors such as family history, BMI, and lifestyle metrics.
  - Improve prediction accuracy through continuous model retraining and validation.

### 3. Blockchain Layer (Solana Integration)
The blockchain layer ensures secure and decentralized data storage and sharing.

- **Current Implementation:**
  - The current model does not yet integrate with Solana but is designed with future blockchain integration in mind.
- **Future Plans:**
  - Use Solana's high-performance blockchain for storing encrypted patient data, ensuring data integrity and immutability.
  - Implement smart contracts to automate data access permissions, allowing patients, healthcare providers, and researchers to securely share data.
  - Leverage Solana's fast transaction speeds (up to 65,000 transactions per second) to enable real-time data updates and alerts.

### 4. Application Layer
The application layer will provide an interface for users to interact with the StrokeGenixAI system.

- **Current Implementation:**
  - The current model runs as a Python script (`stroke_detection_model.py`) with a command-line interface for simulation purposes.
- **Future Plans:**
  - Develop a web-based platform where healthcare providers can input patient data, receive stroke risk predictions, and manage alerts.
  - Build a patient-facing interface for individuals to monitor their stroke risk and receive personalized recommendations.
  - Integrate with healthcare systems via APIs for seamless data exchange.

### 5. Workflow
The flowchart (`flowchart_STROKEGENIXAI.jpg`) illustrates the high-level workflow:
1. **Data Collection:** Health data is collected (currently simulated, future: real patient data).
2. **AI Analysis:** The AI model processes the data to predict stroke risk.
3. **Blockchain Storage:** Data and predictions are securely stored on the Solana blockchain.
4. **Alerts:** Healthcare providers receive real-time alerts for high-risk patients.
5. **Action:** Providers and patients take proactive measures to prevent strokes.

## Technology Stack
- **AI Model:** Python (current: rule-based, future: machine learning with libraries like TensorFlow or PyTorch).
- **Blockchain:** Solana for secure, decentralized data storage and smart contracts.
- **Frontend (Future):** React.js for the web platform.
- **Backend (Future):** Node.js with APIs for data integration.
- **Database (Future):** Integration with Solana for decentralized storage, with potential use of a traditional database (e.g., PostgreSQL) for metadata.

## Future Work
- **Real Medical Data Integration:** Transition from simulated data to real patient datasets, ensuring compliance with healthcare regulations (e.g., HIPAA).
- **Model Improvement:** Use advanced machine learning techniques and larger datasets for better prediction accuracy.
- **Platform Development:** Build a full web platform for healthcare providers and patients to interact with the model.
- **Scalability:** Optimize the system to handle large-scale data processing and global deployment.

## Contributing
We welcome contributions to improve our architecture! Please see our [CONTRIBUTING.md](../CONTRIBUTING.md) file for guidelines on how to contribute.

## License
This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.
