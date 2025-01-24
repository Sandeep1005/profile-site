from reactpy import component, html, run


@component
def LeftHalf():
    left_section_style = {
        "flex": "1",
        "display": "flex",
        "flexDirection": "column",  # Stack children vertically
        "justifyContent": "center",
        "alignItems": "center",
        "backgroundColor": "#0D98BA",
        "borderRadius": "15px 0px 0px 15px",
        "position": "relative",  # Set position to relative for absolute positioning of child elements
        "transition": "transform 0.35s, opacity 0.35s"
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

    return html.div(
            {"style": left_section_style,
             "className": "container_left"},
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
            )
        )


@component
def RightHalf():

    right_section_style = {
        "flex": "1",
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "backgroundColor": "#00CEC8",
        "borderRadius": "0px 15px 15px 0px",
        "position": "relative",  # Set position to relative for absolute positioning of child elements
        "transition": "transform 0.35s, opacity 0.35s"
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

    return html.div(
            {"style": right_section_style,
             "className": "container_right"},
            html.img(
                {
                    "src": "",
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
            )
        )


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

    # Component structure
    return html.div(
        {"style": container_style},
        LeftHalf(),
        RightHalf(),
        html.script("""
            document.addEventListener('scroll', () => {
                const scrollY = window.scrollY;
                const viewportHeight = window.innerHeight;

                const leftBox = document.querySelector('.container_left');
                const rightBox = document.querySelector('.container_right');

                if (scrollY > viewportHeight * 0.1) {
                    leftBox.style.transform = 'translateX(-50vw)';
                    leftBox.style.opacity = '0';

                    rightBox.style.transform = 'translateX(50vw)';
                    rightBox.style.opacity = '0';
                } else {
                    leftBox.style.transform = 'translateX(0)';
                    leftBox.style.opacity = '1';

                    rightBox.style.transform = 'translateX(0)';
                    rightBox.style.opacity = '1';
                }
            });
                    """),
    )


if __name__ == "__main__":
    run(IntroPage)
