from reactpy import component, html, hooks


@component
def PopUpImage1():
    experienceItemImageStyle = {
        "width": "80%",
        "border-radius": "10px",
        "cursor": "pointer",
        "transition": "transform 0.3s ease"
    }

    popUpImageCaption = ""

    # State to handle popup visibility
    is_visible, set_visible = hooks.use_state(False)
    
    def toggle_popup(event):
        set_visible(not is_visible)

    return html.div(
        {
            "style": {
                "width": "30%",
                "display": "flex",
                "justify-content": "flex-end",
                "fontFamily": "Arial, sans-serif",
            }
        },
        html.img(
            {
                    "style": experienceItemImageStyle,
                    "class_name": "zoom-image-exp1",
                    "alt": "Image",
                    "src": "https://media.licdn.com/dms/image/v2/C4D22AQHZmRYvg4064Q/feedshare-shrink_2048_1536/feedshare-shrink_2048_1536/0/1676291949097?e=2147483647&v=beta&t=d6fu7g0sNf0DYQjymgW0039TChTXoUY8G44WItF7yTk",
                    "onClick": toggle_popup,
            },
        ),
        html.div(
            {
                "style": {
                    "display": "block" if is_visible else "none",
                    "position": "fixed",
                    "top": "50%",
                    "left": "50%",
                    "transform": "translate(-50%, -50%)",
                    "width": "80%",
                    "maxWidth": "800px",
                    "backgroundColor": "#DCDCDC",
                    "boxShadow": "0px 8px 16px rgba(0, 0, 0, 0.2)",
                    "borderRadius": "20px",
                    "zIndex": "1000",
                    "padding": "16px",
                },
            },
            html.div(
                {
                    "style": {
                        "display": "flex",
                        "flexDirection": "row",
                        "gap": "16px",
                    },
                },
                html.div(
                    {
                        "style": {
                            "flex": "1",
                        },
                    },
                    html.img(
                        {
                            "src": "https://media.licdn.com/dms/image/v2/C4D22AQHZmRYvg4064Q/feedshare-shrink_2048_1536/feedshare-shrink_2048_1536/0/1676291949097?e=2147483647&v=beta&t=d6fu7g0sNf0DYQjymgW0039TChTXoUY8G44WItF7yTk",
                            "alt": "Popup Image",
                            "style": {
                                "width": "100%",
                                "borderRadius": "10px",
                            },
                        },
                    ),
                    html.p(
                        {
                            "style": {
                                "textAlign": "center",
                                "marginTop": "8px",
                                "fontWeight": "bold",
                            }
                        },
                        "This is the caption for the image.",
                    ),
                ),
                html.div(
                    {
                        "style": {
                            "flex": "1",
                            "display": "flex",
                            "flexDirection": "column",
                            "justifyContent": "center",
                            "textAlign": "justify",
                        }
                    },
                    html.p(
                        "This is some descriptive text on the right side of the popup. "
                        "You can write anything here to complement the image and its caption."
                    ),
                ),
            ),
            html.button(
                {
                    "style": {
                        "position": "absolute",
                        "top": "8px",
                        "right": "8px",
                        "backgroundColor": "gray",
                        "color": "#fff",
                        "border": "none",
                        "borderRadius": "50%",
                        "width": "30px",
                        "height": "30px",
                        "cursor": "pointer",
                        "fontWeight": "bold",
                    },
                    "onClick": toggle_popup,
                },
                "×",
            ),
        ),
        html.div(
            {
                "style": {
                    "display": is_visible and "block" or "none",
                    "position": "fixed",
                    "top": "0",
                    "left": "0",
                    "width": "100%",
                    "height": "100%",
                    "backgroundColor": "rgba(0, 0, 0, 0.5)",
                    "zIndex": "999",
                },
                "onClick": toggle_popup,
            },
        ),
    )    


@component
def PopUpImage2():
    experienceItemImageStyle = {
        "width": "80%",
        "border-radius": "10px",
        "cursor": "pointer",
        "transition": "transform 0.3s ease"
    }

    popUpImageCaption = ""

    # State to handle popup visibility
    is_visible, set_visible = hooks.use_state(False)
    
    def toggle_popup(event):
        set_visible(not is_visible)

    return html.div(
        {
            "style": {
                "width": "30%",
                "display": "flex",
                "justify-content": "flex-end",
                "fontFamily": "Arial, sans-serif",
            }
        },
        html.img(
            {
                    "style": experienceItemImageStyle,
                    "class_name": "zoom-image-exp1",
                    "alt": "Image",
                    "src": "https://media.licdn.com/dms/image/v2/C4D22AQHZmRYvg4064Q/feedshare-shrink_2048_1536/feedshare-shrink_2048_1536/0/1676291949097?e=2147483647&v=beta&t=d6fu7g0sNf0DYQjymgW0039TChTXoUY8G44WItF7yTk",
                    "onClick": toggle_popup,
            },
        ),
        html.div(
            {
                "style": {
                    "display": "block" if is_visible else "none",
                    "position": "fixed",
                    "top": "50%",
                    "left": "50%",
                    "transform": "translate(-50%, -50%)",
                    "width": "80%",
                    "maxWidth": "800px",
                    "backgroundColor": "#DCDCDC",
                    "boxShadow": "0px 8px 16px rgba(0, 0, 0, 0.2)",
                    "borderRadius": "20px",
                    "zIndex": "1000",
                    "padding": "16px",
                },
            },
            html.div(
                {
                    "style": {
                        "display": "flex",
                        "flexDirection": "row",
                        "gap": "16px",
                    },
                },
                html.div(
                    {
                        "style": {
                            "flex": "1",
                        },
                    },
                    html.img(
                        {
                            "src": "https://media.licdn.com/dms/image/v2/C4D22AQHZmRYvg4064Q/feedshare-shrink_2048_1536/feedshare-shrink_2048_1536/0/1676291949097?e=2147483647&v=beta&t=d6fu7g0sNf0DYQjymgW0039TChTXoUY8G44WItF7yTk",
                            "alt": "Popup Image",
                            "style": {
                                "width": "100%",
                                "borderRadius": "10px",
                            },
                        },
                    ),
                    html.p(
                        {
                            "style": {
                                "textAlign": "center",
                                "marginTop": "8px",
                                "fontWeight": "bold",
                            }
                        },
                        "This is the caption for the image.",
                    ),
                ),
                html.div(
                    {
                        "style": {
                            "flex": "1",
                            "display": "flex",
                            "flexDirection": "column",
                            "justifyContent": "center",
                            "textAlign": "justify",
                        }
                    },
                    html.p(
                        "This is some descriptive text on the right side of the popup. "
                        "You can write anything here to complement the image and its caption."
                    ),
                ),
            ),
            html.button(
                {
                    "style": {
                        "position": "absolute",
                        "top": "8px",
                        "right": "8px",
                        "backgroundColor": "gray",
                        "color": "#fff",
                        "border": "none",
                        "borderRadius": "50%",
                        "width": "30px",
                        "height": "30px",
                        "cursor": "pointer",
                        "fontWeight": "bold",
                    },
                    "onClick": toggle_popup,
                },
                "×",
            ),
        ),
        html.div(
            {
                "style": {
                    "display": is_visible and "block" or "none",
                    "position": "fixed",
                    "top": "0",
                    "left": "0",
                    "width": "100%",
                    "height": "100%",
                    "backgroundColor": "rgba(0, 0, 0, 0.5)",
                    "zIndex": "999",
                },
                "onClick": toggle_popup,
            },
        ),
    )    


@component
def ExperienceItem1():
    experienceItemstyle = {
        "background-color": "#00CEC8",
        "padding": "10px 20px 10px 20px",
        "margin": "15px",
        "border-radius": "20px"
    }
    experienceItemHeaderStyle = {
        "padding": "0px 50px 20px 50px"
    }
    experienceItemContentDivStyle = {
        "display": "flex",
        "flex-direction": "row",
        "justify-content": "flex-start",
        "align-items": "center"
    }
    experienceItemParagraphStyle = {
        "width": "100%",
        "margin": "0px 20px 20px 20px",
        "padding": "0px 80px 0px 80px",
        "font-size": "18px",
        "color": "black",
        "font-family": "Arial, sans-serif",
    }

    imageHoverZoomJavaScript = """
    // Select all image elements with the class 'zoom-image-exp1'
    const images = document.querySelectorAll('.zoom-image-exp1');

    // Loop through each image and attach event listeners
    images.forEach((image, index) => {
        image.addEventListener('mouseover', () => {
            image.style.transform = 'scale(1.1)'; // Apply the zoom effect
        });

        image.addEventListener('mouseout', () => {
            image.style.transform = 'scale(1)'; // Reset to the original size
        });
    });

    """

    return html.div(
        {"style": experienceItemstyle},
        html.h2(
            {"style": experienceItemHeaderStyle},
            "Data Scientist - ",
            html.a({"href": "https://www.decimalpointanalytics.com/",
                    "target": "_blank",
                    "style": {
                        "text-decoration": "none"
                    }}, "Decimal Point Analytics"),
            html.a({"style": {
                "font-size": "14px",
            }}, "  (June 2022 - Present)")
        ),
        html.div(
            {"style": experienceItemContentDivStyle},
            html.ul(
                {"style": experienceItemParagraphStyle},
                html.li("some words about this experience some words about this experience"),
                html.li("some words about this experience some words about this experience"),
                html.li("some words about this experience some words about this experience"),
                html.li("some words about this experience some words about this experience"),
                html.li("some words about this experience some words about this experience"),
            ),
            PopUpImage1(),
            PopUpImage2()
        ),
        html.script(imageHoverZoomJavaScript)
    )
