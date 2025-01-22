from reactpy import component, html, run

@component
def IntroPage():
    # Inline styles for the container and sections
    container_style = {
        "display": "flex",
        "flexDirection": "row",
        "height": "100vh",  # Full vertical height of the window
        "width": "95vw",  # Full horizontal width of the window
        "overflow": "hidden",
    }

    left_section_style = {
        "flex": "1",
        "display": "flex",
        "flexDirection": "column",  # Stack the content vertically
        "justifyContent": "flex-start",  # Start at the top
        "backgroundColor": "#2F4F4F",  # Light gray background for contrast
        "borderRadius": "20px",  # Curved edges
        "padding": "20px",
    }

    right_section_style = {
        "flex": "1",
        "display": "flex",
        "flexDirection": "column",  # Stack the content vertically
        "justifyContent": "flex-start",  # Start at the top
        "backgroundColor": "#B0E0E6",  # White background
        "borderRadius": "20px",  # Curved edges
        "padding": "20px",
    }

    menu_style = {
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "backgroundColor": "#d9d9d9",  # Light gray for the menu bar
        "padding": "10px",
        "borderRadius": "10px",  # Rounded edges for the menu
        "width": "100%",  # Ensure the menu spans across the width
        "position": "absolute",  # Position it at the bottom of the section
        "bottom": "0",  # Align to the bottom of the section
        "left": "0",  # Align to the left side
    }

    menu_item_style = {
        "padding": "10px 20px",
        "backgroundColor": "#ffffff",  # White background for menu items
        "border": "1px solid #cccccc",
        "borderRadius": "5px",  # Curved edges
        "cursor": "pointer",
    }

    image_style = {
        "maxWidth": "90%",  # Scale the image to fit within 90% of the section
        "maxHeight": "90%",  # Ensure the image scales properly
        "objectFit": "contain",
    }

    # Component structure
    return html.div(
        {"style": container_style},
        html.div(
            {"style": left_section_style},
            html.h1(
                {"style": {"textAlign": "center"}},
                "Welcome to the Intro Page!"
            ),
            html.div(
                {"style": menu_style},
                html.div({"style": menu_item_style}, "Menu Item 1"),
                html.div({"style": menu_item_style}, "Menu Item 2"),
            ),
        ),
        html.div(
            {"style": right_section_style},
            html.img(
                {
                    "src": "/static/images/intro_image.png",  # Update the path to your image
                    "alt": "Intro Image",
                    "style": image_style,
                }
            ),
            html.div(
                {"style": menu_style},
                html.div({"style": menu_item_style}, "Menu Item 1"),
                html.div({"style": menu_item_style}, "Menu Item 2"),
            ),
        ),
    )

if __name__ == "__main__":
    run(IntroPage)
