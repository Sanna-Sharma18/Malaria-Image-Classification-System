# Malaria Cell Image Classification Using Deep Learning

An AI-based malaria cell image classification system developed using **Custom Convolutional Neural Networks (CNN)** and **ResNet50 Transfer Learning**, with an interactive **Streamlit web application** for image-based predictions.

---

## Project Overview

Malaria is a mosquito-borne infectious disease that can be identified through the examination of blood smear samples. This project explores the application of deep learning techniques to classify microscopic blood cell images into two categories:

- **Parasitized:** Cells containing malaria parasites.
- **Uninfected:** Cells without malaria parasites.

The project implements two deep learning approaches: a Custom CNN developed from scratch and ResNet50 using transfer learning. Their performance is evaluated and compared using multiple classification metrics.

An interactive Streamlit dashboard is also developed to allow users to upload cell images, select a trained model, and view the predicted classification along with its confidence score.

## Project Objectives

- Develop a deep learning-based system for malaria cell image classification.
- Build a Custom CNN architecture for image classification.
- Apply transfer learning using the pre-trained ResNet50 architecture.
- Evaluate both models using standard classification metrics.
- Compare the performance of the two approaches.
- Develop an interactive web application for image-based predictions.

## Models Implemented

### 1. Custom Convolutional Neural Network (CNN)

A CNN architecture developed from scratch to learn relevant visual features from microscopic cell images.

### 2. ResNet50 – Transfer Learning

ResNet50 is used as a pre-trained feature extraction architecture with ImageNet weights. A custom classification head is added for the binary classification task.

Both models are trained to classify images into Parasitized and Uninfected categories.

## Model Performance

The models were evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- ROC-AUC Score

### Performance Comparison

| Evaluation Metric | Custom CNN | ResNet50 |
|---|---:|---:|
| Accuracy | 94.34% | 93.35% |
| ROC-AUC | 0.9826 | 0.9845 |

### Classification Results

**Custom CNN**

| Class | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| Uninfected | 0.95 | 0.94 | 0.94 |
| Parasitized | 0.94 | 0.95 | 0.94 |

**ResNet50**

| Class | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| Uninfected | 0.91 | 0.97 | 0.94 |
| Parasitized | 0.96 | 0.90 | 0.93 |

The Custom CNN achieved higher classification accuracy in the reported evaluation, while ResNet50 achieved a slightly higher ROC-AUC score.

## Interactive Streamlit Application

An interactive dashboard was developed using Streamlit to demonstrate the trained models.

### Key Features

- Upload microscopic blood cell images.
- Choose between Custom CNN and ResNet50.
- Generate predictions for uploaded images.
- Display the predicted class.
- Display the model confidence score.
- Compare the implemented models.

## Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Deep Learning | TensorFlow, Keras |
| Image Processing | NumPy, Pillow |
| Data Analysis | Pandas |
| Machine Learning Evaluation | Scikit-learn |
| Visualization | Matplotlib, Seaborn |
| Web Application | Streamlit |
| Development Environment | VS Code, Jupyter Notebook |
| Model Hosting | Hugging Face |
| Version Control | Git, GitHub |

## Project Structure

```text
Malaria-Image-Classification-System/
│
├── models/
│   ├── best_cnn.keras
│   └── best_resnet50.keras
│
├── notebooks/
│   └── Model training and evaluation notebooks
│
├── results/
│   └── Evaluation results and visualizations
│
├── app.py
├── main.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

**Note:** The trained model files are hosted separately on Hugging Face because of GitHub's individual file-size restrictions. Download the required models and place them inside the `models/` directory before running the application.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd Malaria-Image-Classification-System
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Download the Trained Models

Download the required model files from the Hugging Face repository:

- `best_cnn.keras`
- `best_resnet50.keras`

Place both files inside the `models/` directory.

**Hugging Face Models:** YOUR_HUGGING_FACE_REPOSITORY_URL

### 7. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your default web browser.

## Dataset Information

The project uses a malaria cell image dataset containing **27,558 microscopic cell images** across two categories:

| Category | Number of Images |
|---|---:|
| Parasitized | 13,779 |
| Uninfected | 13,779 |
| **Total** | **27,558** |

The dataset was divided into training, validation, and testing subsets:

| Dataset Split | Percentage | Number of Images |
|---|---:|---:|
| Training | 70% | 19,290 |
| Validation | 15% | 4,134 |
| Testing | 15% | 4,134 |
| **Total** | **100%** | **27,558** |

Images were resized to 224 × 224 pixels for model input.

## Results and Analysis

Both architectures demonstrated the ability to classify microscopic blood cell images into the two target categories.

The Custom CNN achieved an accuracy of 94.34%, while ResNet50 achieved an accuracy of 93.35% in the reported evaluations.

The ROC-AUC scores of both models indicate strong class-separation performance on their respective evaluation results.

This comparison highlights how a custom-built CNN and a pre-trained deep learning architecture can approach the same image classification problem using different learning strategies.

## Future Scope

Potential improvements and extensions include:

- Experimenting with additional CNN architectures.
- Hyperparameter optimization.
- Improving model generalization.
- Expanding the dataset for more robust evaluation.
- Deploying the Streamlit application online.
- Exploring explainable AI techniques such as Grad-CAM to visualize important image regions.

## Project Information

**Project Title:** Malaria Cell Image Classification Using Deep Learning

**Models:** Custom CNN and ResNet50

**Application:** Streamlit Interactive Dashboard

**Repository:** GitHub

**Model Hosting:** Hugging Face

## Disclaimer

This project is developed for educational and experimental purposes. Its predictions are not intended to replace professional medical examination, laboratory testing, or diagnosis by qualified healthcare professionals.

---

**Built with Python, TensorFlow, Keras and Streamlit.**
