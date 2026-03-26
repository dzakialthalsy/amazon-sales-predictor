# Amazon Sales Predictor

A web application that predicts Amazon product sales using a Random Forest Machine Learning model.

## Features

- 🎯 ML-powered sales prediction using Random Forest Regressor
- 🌐 Modern and responsive web interface
- 🔌 RESTful API endpoint for programmatic access
- 📊 Real-time predictions

## Requirements

- Python 3.8+
- Flask
- scikit-learn
- joblib
- numpy

## Model Storage (Hugging Face)

Model disimpan di Hugging Face Hub karena ukurannya yang besar (>100MB).

### Download Model

1. Edit `download_model.py` dan pastikan `REPO_ID` sudah benar (saat ini: `dz4ic7/amazon-sales-predictor`)
2. Jalankan:
```bash
python download_model.py
```

Atau download manual dari: https://huggingface.co/dz4ic7/amazon-sales-predictor/resolve/main/model.joblib

---

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd amazon-sales-predictor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download the model from Hugging Face:
```bash
python download_model.py
```

Or manually place your trained `model.joblib` file in the project directory.

## Usage

### Running the Application

```bash
python app.py
```

The application will be available at:
- Local: http://127.0.0.1:5000
- Network: http://0.0.0.0:5000

### Web Interface

1. Open your browser and navigate to `http://127.0.0.1:5000`
2. Fill in the input fields:
   - **Stock**: Current inventory stock level
   - **index_sales_int**: Sales performance index
   - **PCS**: Number of product pieces/units
   - **RATE**: Product price rate
   - **GROSS AMT**: Total gross amount
   - **Qty**: Order/sales quantity
   - **ship-postal-code**: Shipping destination postal code
3. Click "Predict Sales" to get the prediction

### API Endpoint

For programmatic access, use the `/predict-api` endpoint:

```bash
POST http://localhost:5000/predict-api
Content-Type: application/json

{
    "Stock": 100,
    "index_sales_int": 50,
    "PCS": 10,
    "RATE": 25.5,
    "GROSS AMT": 255.0,
    "Qty": 20,
    "ship-postal-code": 12345
}
```

Response:
```json
{
    "prediction": 1234.56,
    "features": {
        "Stock": 100,
        "index_sales_int": 50,
        "PCS": 10,
        "RATE": 25.5,
        "GROSS AMT": 255.0,
        "Qty": 20,
        "ship-postal-code": 12345
    }
}
```

## Project Structure

```
amazon-sales-predictor/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore file
├── README.md             # This file
└── templates/
    └── index.html        # Web interface template
```

## Model Information

- **Model Type**: Random Forest Regressor
- **Features**: 7 input features
- **Training**: Built with scikit-learn

## Deployment

### Production Deployment with Gunicorn

For production, use Gunicorn as the WSGI server:

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Cloud Deployment

This application can be deployed to:
- Heroku
- Google Cloud Run
- AWS Elastic Beanstalk
- Railway
- Render

## License

MIT License

## Author

Your Name

---

Built with Flask and scikit-learn 🚀
