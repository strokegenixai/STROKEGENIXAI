import random
import json

# Script to generate sample health data for testing
def generate_sample_data(num_samples=10):
    data_samples = []
    for _ in range(num_samples):
        sample = {
            "age": random.randint(20, 80),
            "blood_pressure": random.randint(110, 180),
            "cholesterol_level": random.randint(150, 250),
            "smoking": random.choice([True, False]),
            "diabetes": random.choice([True, False])
        }
        data_samples.append(sample)
    
    # Save to a JSON file
    with open("sample_data.json", "w") as f:
        json.dump(data_samples, f, indent=4)
    print(f"Generated {num_samples} sample data points in sample_data.json")

if __name__ == "__main__":
    generate_sample_data()
