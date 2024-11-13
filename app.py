import streamlit as st

# Function to convert length to different units
def convert_length(length, unit_from, unit_to):
    # Conversion to meters (base unit)
    if unit_from == 'Meters':
        length_in_meters = length
    elif unit_from == 'Kilometers':
        length_in_meters = length * 1000
    elif unit_from == 'Centimeters':
        length_in_meters = length / 100
    elif unit_from == 'Millimeters':
        length_in_meters = length / 1000
    elif unit_from == 'Inches':
        length_in_meters = length * 0.0254
    elif unit_from == 'Feet':
        length_in_meters = length * 0.3048

    # Convert from meters to the target unit
    if unit_to == 'Meters':
        return length_in_meters
    elif unit_to == 'Kilometers':
        return length_in_meters / 1000
    elif unit_to == 'Centimeters':
        return length_in_meters * 100
    elif unit_to == 'Millimeters':
        return length_in_meters * 1000
    elif unit_to == 'Inches':
        return length_in_meters / 0.0254
    elif unit_to == 'Feet':
        return length_in_meters / 0.3048

# Title of the app
st.title("Length Converter and Calculator")

# Sidebar for options
st.sidebar.header("Choose Your Units")

# Input fields
length = st.number_input("Enter the length", min_value=0.0, value=1.0, step=0.1)
unit_from = st.selectbox("Select the unit of your length", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet"])
unit_to = st.selectbox("Select the unit to convert to", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet"])

# Calculate and display the converted length
if st.button("Convert"):
    converted_length = convert_length(length, unit_from, unit_to)
    st.write(f"{length} {unit_from} is equal to {converted_length:.2f} {unit_to}")
