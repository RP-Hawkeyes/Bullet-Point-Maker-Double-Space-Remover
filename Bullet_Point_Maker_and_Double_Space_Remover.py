import streamlit as st

def format_bullet_points(text):
    # Split the text by lines
    lines = text.split('\n')

    # Initialize an empty list to store formatted lines
    formatted_lines = []

    # Iterate through each line
    for line in lines:
        # Check if the line is not empty
        if line.strip():
            # Add a bullet point at the beginning of the line
            formatted_lines.append(f"• {line.strip()}")

    # Join the formatted lines with newline characters
    formatted_text = '\n'.join(formatted_lines)

    return formatted_text

def remove_double_spaces(text):
    # Replace double spaces with single spaces
    cleaned_text = text.replace("  ", " ")

    return cleaned_text

def main():
    st.title("Bullet Point Maker & Double Space Remover")

    # Text input area
    text_input = st.text_area("Enter your text here:", "")

    if st.button("Format Bullet Points"):
        # Format bullet points
        formatted_text = format_bullet_points(text_input)
        st.text_area("Formatted Text (with Bullet Points):", formatted_text)

    if st.button("Remove Double Spaces"):
        # Remove double spaces
        cleaned_text = remove_double_spaces(text_input)
        st.text_area("Cleaned Text (Double Spaces Removed):", cleaned_text)

if __name__ == "__main__":
    main()
