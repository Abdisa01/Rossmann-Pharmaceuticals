# myapp/views.py
from django.shortcuts import render
from .utils import load_model
import pandas as pd

# Load the model once when the module is loaded
model = load_model()

def home_view(request):
    return render(request, 'myapp/home.html')

def predict_view(request):
    prediction = None
    if request.method == 'POST':
        store = request.POST.get('store')
        sales = request.POST.get('sales')
        customers = request.POST.get('customers')

        if store and sales and customers:
            try:
                input_data = [[int(store), float(sales), float(customers)]]
                predicted_sales = model.predict(input_data)[0]  # Assuming the model returns a list
                predicted_customers = customers  # Adjust if needed

                prediction = {
                    'Store': store,
                    'Predicted_Sales': predicted_sales,
                    'Predicted_Customers': predicted_customers
                }

                # Optionally save prediction to CSV
                save_prediction_to_csv(prediction)

            except ValueError as e:
                print(f"Error: {e}")

    return render(request, 'myapp/predict.html', {'prediction': prediction})

def save_prediction_to_csv(prediction):
    df = pd.DataFrame([prediction])  # Create DataFrame from prediction dict
    df.to_csv('predicted_sales.csv', mode='a', header=False, index=False)  # Append to CSV