from src.stroke_detection_model import StrokeDetectionModel

# Example script showing how to use StrokeDetectionModel
def main():
    print("Running StrokeGenixAI basic usage example...")
    
    # Initialize the model
    model = StrokeDetectionModel()
    
    # Simulate running the model with custom data
    custom_data = {
        "age": 65,
        "blood_pressure": 170,
        "cholesterol_level": 250,
        "smoking": True,
        "diabetes": True
    }
    
    # Override the default random data with custom data
    model.data = custom_data
    
    # Run the model
    model.run_model()

if __name__ == "__main__":
    main()
