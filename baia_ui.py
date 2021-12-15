import streamlit as st

from baia import Molecule


st.title("baia")

molecule_name = st.text_input("Enter the name of the molecule", "aspirin")

st.image(Molecule.from_name(molecule_name).draw2d(as_numpy=True))

