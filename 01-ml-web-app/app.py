"""A tiny web app that predicts an iris species from four measurements."""
import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


# Train the model once and remember it, so we don't retrain on every click.
@st.cache_resource
def load_model():
    iris = load_iris(as_frame=True)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(iris.data, iris.target)
    return model, iris.target_names, list(iris.feature_names)


model, species_names, feature_names = load_model()

# ---- The page ----
st.title("🌸 Iris Flower Predictor")
st.write(
    "Move the sliders to describe a flower, and I'll guess its species. "
    "Built with scikit-learn and Streamlit."
)

st.subheader("Your flower's measurements")
sepal_length = st.slider("Sepal length (cm)", 4.0, 8.0, 5.4)
sepal_width = st.slider("Sepal width (cm)", 2.0, 4.5, 3.4)
petal_length = st.slider("Petal length (cm)", 1.0, 7.0, 1.3)
petal_width = st.slider("Petal width (cm)", 0.1, 2.5, 0.2)

# Collect the four numbers into a one-row table whose column names
# match what the model was trained on. This keeps scikit-learn happy.
features = pd.DataFrame(
    [[sepal_length, sepal_width, petal_length, petal_width]],
    columns=feature_names,
)

if st.button("Predict species"):
    prediction = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0]

    st.success(f"This looks like **{species_names[prediction]}** 🌸")

    st.subheader("How confident is the model?")
    for name, prob in zip(species_names, probabilities):
        st.write(f"{name}: {prob:.0%}")
        st.progress(float(prob))
