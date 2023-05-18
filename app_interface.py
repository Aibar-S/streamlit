import streamlit as st
from PIL import Image, ImageDraw, ImageFont

def main():
    st.set_page_config(page_title="Picture Description App", layout="wide")

    st.sidebar.title("Tabs")
    tabs = ["Picture", "About"]
    selected_tab = st.sidebar.selectbox("Select a tab", tabs)

    if selected_tab == "Picture":
        st.title("Picture")

        # Define the parts of the picture and their descriptions
        parts = {
            "Part A": "Description of Part A.",
            "Part B": "Description of Part B.",
            "Part C": "Description of Part C.",
        }

        # Load the picture
        picture_path = 'drilling_rig.JPG'  # Replace with the path to your picture
        picture = Image.open(picture_path)

        # Calculate the maximum width and height to fit inside the window
        max_width = st.sidebar.width - 50  # Subtracting some padding
        max_height = st.sidebar.height - st.title.height - 100  # Subtracting title height and some padding

        # Rescale the picture to fit inside the window
        picture.thumbnail((max_width, max_height), Image.ANTIALIAS)

        # Create a drawing object
        draw = ImageDraw.Draw(picture)

        # Define the arrow start and end points
        arrow_start_points = [(100, 200), (300, 400), (500, 600)]  # Replace with the coordinates of your arrows
        arrow_end_points = [(150, 250), (350, 450), (550, 650)]  # Replace with the coordinates of your arrows

        # Define the font for the part names
        font = ImageFont.truetype("ArianaVioleta-dz2K.ttf", size=16)  # Replace with the path to your font file and desired font size

        # Draw arrows and part names on the picture
        for i, (start_point, end_point) in enumerate(zip(arrow_start_points, arrow_end_points)):
            part_name = list(parts.keys())[i]

            # Draw arrow
            draw.line(start_point + end_point, fill="red", width=3)
            draw.polygon([end_point, (end_point[0] - 10, end_point[1] + 5), (end_point[0] + 10, end_point[1] + 5)], fill="red")

            # Draw part name
            text_width, text_height = draw.textsize(part_name, font=font)
            text_position = (start_point[0] + (end_point[0] - start_point[0]) // 2 - text_width // 2, start_point[1] - text_height - 10)
            draw.text(text_position, part_name, font=font, fill="black")

        # Display the picture with arrows and part names
        st.image(picture, use_column_width=True)

        st.write("Click on the names to view the description of each part.")

        # Display the descriptions
        for i, (start_point, end_point) in enumerate(zip(arrow_start_points, arrow_end_points)):
            part_name = list(parts.keys())[i]

            # Get the description of the part when its name is clicked
            if st.button(part_name):
                st.write(parts[part_name])

    else:
        st.title("About")
        st.write("This app was created by [Your Name] as a
