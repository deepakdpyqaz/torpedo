import streamlit as st
from model import Model

st.title("Demo with streamlit")

model = Model()

st.write("Select the choices from the dropdowns below")
selections = {}
for prop in model.procedure:
    selections[prop] = st.multiselect(prop.capitalize(), getattr(model, prop))


def make_prediction():
    search_terms = []
    for value in selections.values():
        search_terms.extend(value)
    data = model.predict(search_terms, indices=False)
    st.dataframe(
        data[
            [
                "Category",
                "Category in detail",
                "Pureesha pareeksha",
                "Search Term for Feature of pureesha",
            ]
        ]
    )


if st.button("Predict"):
    make_prediction()
