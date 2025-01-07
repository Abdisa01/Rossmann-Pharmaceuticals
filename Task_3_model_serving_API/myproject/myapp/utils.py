import pickle

def load_model():
    with open('C:\\Users\\Abdilala\\Documents\\GitHub\\Rossmann-Pharmaceuticals\\Task_2_prediction\\06-01-2025-22-21-32-199.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Load the model once
model = load_model()