import random
import time

class StrokeDetectionModel:
    def __init__(self):
        self.data = self.load_data()
    
    def load_data(self):
        # Simulating the loading of medical data
        return {
            "age": random.randint(20, 80),
            "blood_pressure": random.randint(110, 180),
            "cholesterol_level": random.randint(150, 250),
            "smoking": random.choice([True, False]),
            "diabetes": random.choice([True, False])
        }

    def predict_risk(self, data):
        risk_score = 0
        if data["age"] > 60:
            risk_score += 30
        if data["blood_pressure"] > 160:
            risk_score += 40
        if data["cholesterol_level"] > 240:
            risk_score += 20
        if data["smoking"]:
            risk_score += 25
        if data["diabetes"]:
            risk_score += 15
        
        return risk_score

    def run_model(self):
        print("Simulating stroke detection...")
        time.sleep(2)  # Simulating processing time
        
        risk = self.predict_risk(self.data)
        
        if risk > 80:
            print(f"Warning: High stroke risk detected! Risk Score: {risk}")
        elif 50 < risk <= 80:
            print(f"Moderate risk detected. Risk Score: {risk}")
        else:
            print(f"Low risk detected. Risk Score: {risk}")

# Simulate the AI model
if __name__ == "__main__":
    model = StrokeDetectionModel()
    model.run_model()
