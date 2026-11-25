import numpy as np
import tensorflow as tf
from PIL import Image
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Malaria Detection System",
    page_icon="🧬",
    layout="wide"
)

# ---------------- CUSTOM STYLING ----------------

st.markdown("""
<style>
.main {
    background-color: #f5f8fc;
}
h1 {
    color: #17365D;
}
h2, h3 {
    color: #24476B;
}
.metric-card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #e0e7ef;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

st.sidebar.title("🧬 Malaria AI")
st.sidebar.write("Malaria Detection System")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Malaria Detection", "Model Comparison", "About"]
)

# ---------------- MODEL LOADING ----------------

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"

@st.cache_resource
def load_cnn_model():
    model_path = MODEL_DIR / "best_cnn.keras"
    return tf.keras.models.load_model(
        model_path,
        compile=False
    )


@st.cache_resource
def load_resnet_model():
    model_path = MODEL_DIR / "best_resnet50.keras"

    return tf.keras.models.load_model(
        model_path,
        custom_objects={
            "preprocess_input":
                tf.keras.applications.resnet50.preprocess_input
        },
        compile=False
    )

# ---------------- HOME PAGE ----------------

if page == "Home":

    st.title("🧬 Malaria Detection System")

    st.write(
        "An AI-powered system for classifying blood cell "
        "images into Parasitized and Uninfected categories."
    )

    st.divider()

    st.subheader("Project Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("CNN Accuracy", "94%")
    col2.metric("ResNet50 Accuracy", "93%")
    col3.metric("Models Trained", "2")

    st.divider()

    st.subheader("Available Deep Learning Models")

    col1, col2 = st.columns(2)

    with col1:
        st.info("### Custom CNN")
        st.write("A convolutional neural network trained for malaria cell classification.")
        st.write("ROC-AUC: 0.9826")

    with col2:
        st.success("### ResNet50")
        st.write("A pretrained ResNet50 architecture fine-tuned for malaria classification.")
        st.write("ROC-AUC: 0.9845")


# ---------------- DETECTION PAGE ----------------

elif page == "Malaria Detection":

    st.title("Malaria Cell Detection")

    st.write(
        "Upload a blood cell image and select a trained "
        "deep learning model to classify it."
    )

    st.divider()

    uploaded_file = st.file_uploader(
        "Upload Blood Cell Image",
        type=["jpg", "jpeg", "png"]
    )

    model_choice = st.selectbox(
        "Select Model",
        ["Custom CNN", "ResNet50"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file).convert("RGB")

        st.subheader("Uploaded Image")

        st.image(image, width=300)

        st.divider()

        if st.button("🔍 Check Image", type="primary"):

            try:
                # Resize image
                image_resized = image.resize((224, 224))

                # Convert to NumPy array
                image_array = np.array(image_resized)

                # Add batch dimension
                image_array = np.expand_dims(
                    image_array, axis=0
                ).astype("float32")

                # Load selected model
                with st.spinner("Analyzing image..."):

                    if model_choice == "Custom CNN":
                        model = load_cnn_model()

                    else:
                        model = load_resnet_model()

                    # Generate prediction
                    prediction = model.predict(
                        image_array,
                        verbose=0
                    )

                    probability = float(
                        np.asarray(prediction).reshape(-1)[0]
                    )

                # Class mapping:
                # 0 = Uninfected
                # 1 = Parasitized

                if probability >= 0.5:

                    result = "Parasitized"
                    confidence = probability * 100

                else:

                    result = "Uninfected"
                    confidence = (1 - probability) * 100

                # Display result
                st.divider()

                st.subheader("Prediction Result")

                if result == "Parasitized":

                    st.error("⚠️ Predicted: PARASITIZED")

                else:

                    st.success("✅ Predicted: UNINFECTED")

                st.metric(
                    "Prediction Confidence",
                    f"{confidence:.2f}%"
                )

                st.progress(confidence / 100)

                st.caption(
                    f"Model used: {model_choice}"
                )

                st.warning(
                    "This is an experimental AI prediction, "
                    "not a medical diagnosis."
                )

            except Exception as e:

                st.error("Prediction failed.")

                st.exception(e)


# ---------------- COMPARISON PAGE ----------------

elif page == "Model Comparison":

    st.title("CNN vs ResNet50")

    data = pd.DataFrame({
        "Model": ["Custom CNN", "ResNet50"],
        "Accuracy": [94, 93],
        "ROC-AUC": [0.9826, 0.9845]
    })

    st.subheader("Performance Comparison")

    st.dataframe(data, use_container_width=True)

    st.subheader("Accuracy Comparison")

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.bar(
        data["Model"],
        data["Accuracy"]
    )

    ax.set_ylabel("Accuracy (%)")
    ax.set_ylim(0, 100)
    ax.set_title("CNN vs ResNet50 Accuracy")

    st.pyplot(fig)

    st.subheader("ROC-AUC Comparison")

    fig2, ax2 = plt.subplots(figsize=(8, 4))

    ax2.bar(
        data["Model"],
        data["ROC-AUC"]
    )

    ax2.set_ylim(0, 1)
    ax2.set_ylabel("ROC-AUC")
    ax2.set_title("CNN vs ResNet50 ROC-AUC")

    st.pyplot(fig2)

# ---------------- ABOUT PAGE ----------------

elif page == "About":

    st.title("About the Project")

    st.write("""
    This project uses deep learning techniques to classify
    malaria-infected and uninfected blood cell images.

    Two architectures are investigated:

    1. Custom Convolutional Neural Network (CNN)
    2. ResNet50 Transfer Learning

    The models are evaluated using accuracy, precision,
    recall, F1-score, confusion matrices and ROC-AUC.
    """)

    st.warning(
        "This is an educational research prototype, "
        "not a clinically validated diagnostic system."
    )

# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "Malaria Detection System | Deep Learning Project"
)
