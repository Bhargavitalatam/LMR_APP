# 🌍 Landmark Classification Using Deep Learning

## Overview

This project is a deep learning-based image classification system that identifies landmarks from uploaded images. A Convolutional Neural Network (CNN) was trained on a subset of the Google Landmarks Dataset to learn visual patterns and classify landmark images into their corresponding landmark IDs.

## Features

* Upload landmark images through a web interface
* Deep learning-based image classification
* Real-time prediction using TensorFlow/Keras
* Interactive Streamlit web application
* End-to-end machine learning workflow from training to deployment

## Dataset

The model was trained using the Google Landmarks Dataset (Micro Version), which contains landmark images along with landmark identifiers.

## Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Pillow (PIL)
* Streamlit
* GitHub

## Project Workflow

1. Data preprocessing and image resizing
2. CNN model development and training
3. Model evaluation and prediction
4. Saving the trained model
5. Building a Streamlit application
6. Deployment using Streamlit Cloud

## Running the Project Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Output

The application predicts the Landmark ID corresponding to the uploaded image.

Example:

```
Predicted Landmark ID: 482
```

## Deployment

The project is deployed using Streamlit Cloud and can be accessed through the live application link.

Live at - https://lmrapp-mfk6x8j4fnqi3x7ehwjrk9.streamlit.app/

## Future Improvements

* Use the full Google Landmarks Dataset
* Add landmark name mapping instead of only landmark IDs
* Improve model accuracy using transfer learning
* Display prediction confidence scores

## Author

Satya Bhargavi

Deep Learning & Computer Vision Project
