from reactpy import component, html, run


@component
def IntroPage():
    # Inline styles for the container and sections
    container_style = {
        "display": "flex",
        "flexDirection": "row",
        "height": "98vh",  # Full vertical height of the window
        "width": "98vw",  # Full horizontal width of the window
        "overflow": "hidden",
    }

    left_section_style = {
        "flex": "1",
        "display": "flex",
        "flexDirection": "column",  # Stack children vertically
        "justifyContent": "center",
        "alignItems": "center",
        "backgroundColor": "#0D98BA",  # Light gray background for contrast
        "borderRadius": "15px 0px 0px 15px",
        "position": "relative",  # Set position to relative for absolute positioning of child elements
    }

    right_section_style = {
        "flex": "1",
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "backgroundColor": "#00CEC8",  # White background
        "borderRadius": "0px 15px 15px 0px",
        "position": "relative",  # Set position to relative for absolute positioning of child elements
    }

    button_style = {
        "width": "150px",
        "position": "absolute",
        "padding": "15px 20px",
        "border": "none",
        "color": "#000",
        "fontWeight": "bold",
        "cursor": "pointer",
        "boxShadow": "0 2px 5px rgba(0, 0, 0, 0.2)",
    }

    left_button_style = {
        **button_style,
        "backgroundColor": "#00CEC8",
        "borderRadius": "30px 0px 0px 30px",
        "bottom": "40px",
        "right": "0px",  # Button at bottom-right of left section
    }

    right_button_style = {
        **button_style,
        "backgroundColor": "#0D98BA",
        "borderRadius": "0px 30px 30px 0px",
        "bottom": "40px",
        "left": "0px",  # Button at bottom-left of right section
    }

    image_style = {
        "maxWidth": "50%",  # Scale the image to fit within 90% of the section
        "maxHeight": "50%",  # Ensure the image scales properly
        "objectFit": "contain",
    }

    # Component structure
    return html.div(
        {"style": container_style},
        html.div(
            {"style": left_section_style},
            html.h1(
                {"style": {"textAlign": "center"}},
                "Hello.. from Sandeep"
            ),
            html.h2(
                {"style": {"textAlign": "center"}},
                "Welcome to my corner of the internet"
            ),
            html.button(
                {
                    "style": left_button_style,
                    "onClick": lambda event: print("Left button clicked!"),
                },
                "Explore"
            ),
        ),
        html.div(
            {"style": right_section_style},
            html.img(
                {
                    "src": "https://media.licdn.com/dms/image/v2/C4D03AQEFayXPqVO5Ew/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1649922047754?e=1743033600&v=beta&t=n-zNwy16CGkqw6Z-iepbsj7iFhR2phU8bltI99VZbsU",
                    "alt": "Intro Image",
                    "style": image_style,
                }
            ),
            html.button(
                {
                    "style": right_button_style,
                    "onClick": lambda event: print("Right button clicked!"),
                },
                "Guide"
            ),
        ),
    )


if __name__ == "__main__":
    run(IntroPage)
