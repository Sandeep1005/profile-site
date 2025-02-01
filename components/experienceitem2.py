from reactpy import component, html, hooks


@component
def PopUpImage1():
    experienceItemImageStyle = {
        "width": "100%",
        "border-radius": "10px",
        "cursor": "pointer",
        "transition": "transform 0.3s ease"
    }

    # State to handle popup visibility
    is_visible, set_visible = hooks.use_state(False)
    
    def toggle_popup(event):
        set_visible(not is_visible)

    popupListStyle = {
        "width": "100%",
        "margin": "0px 5px 0px 5px",
        "padding": "0px 0px 0px 0px",
        "font-size": "18px",
        "color": "black",
        "font-family": "Arial, sans-serif",

        "list-style-type": "none",
        # "background-color": "#f8f9fa",
        "border-radius": "8px",
        # "box-shadow": "0 2px 4px rgba(0, 0, 0, 0.1)",
    }
    listItemStyle = {
        "padding": "10px 15px",
        "border-bottom": "1px solid #fff",
        "font-size": "16px",
        "color": "#333",
        # "cursor": "pointer",
        "transition": "background-color 0.3s"
    }
    lastListItemStyle = {
        "padding": "10px 15px",
        # "border-bottom": "1px solid #ddd",
        "font-size": "16px",
        "color": "#333",
        # "cursor": "pointer",
        "transition": "background-color 0.3s"
    }
    markStyle = {
        "background-color": "#0D98BA",
        "color": "#fff",
        "padding": "2px 4px",
        "border-radius": "4px",
        "font-weight": "bold"
    }

    return html.div(
        {
            "style": {
                "width": "20%",
                "display": "flex",
                "justify-content": "flex-end",
                "fontFamily": "Arial, sans-serif",
            }
        },
        html.img(
            {
                    "style": experienceItemImageStyle,
                    "class_name": "zoom-image-exp2",
                    "alt": "Image",
                    "src": "https://internshala.com/uploads/student_certificates/62a2fd419b68f1654848833.png",
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
                            "src": "https://internshala.com/uploads/student_certificates/62a2fd419b68f1654848833.png",
                            "alt": "Popup Image",
                            "style": {
                                "width": "100%",
                                "borderRadius": "10px",
                            },
                        },
                    )
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
                    html.ul(
                        {"style": popupListStyle},
                        html.li(
                            {"style": listItemStyle},
                            "Got the internship through Internshala"
                        ),
                        html.li(
                            {"style": lastListItemStyle},
                            "Can be verified with: ",
                            html.mark({"style": markStyle},
                                      html.a(
                                          {
                                              "style": {"text-decoration": "none",
                                                        "color": "#fff"},
                                              "target": "_blank",
                                              "href": "https://internshala.com/student/certificate/87186093/FDC05493-E773-5511-0909-3EC76F81C503"
                                          },
                                          "Internshala"
                                      ) 
                                     )
                        )
                    )
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
def ExperienceItem2():
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
    experienceItemListStyle = {
        "width": "100%",
        "margin": "0px 0px 20px 20px",
        "padding": "0px 80px 0px 80px",
        "font-size": "18px",
        "color": "black",
        "font-family": "Arial, sans-serif",

        "list-style-type": "none",
        # "background-color": "#f8f9fa",
        "border-radius": "8px",
        # "box-shadow": "0 2px 4px rgba(0, 0, 0, 0.1)",
    }
    listItemStyle = {
        "padding": "10px 15px",
        "border-bottom": "1px solid #ddd",
        "font-size": "16px",
        "color": "#333",
        # "cursor": "pointer",
        "transition": "background-color 0.3s"
    }
    lastListItemStyle = {
        "padding": "10px 15px",
        # "border-bottom": "1px solid #ddd",
        "font-size": "16px",
        "color": "#333",
        # "cursor": "pointer",
        "transition": "background-color 0.3s"
    }
    markStyle = {
        "background-color": "#0D98BA",
        "color": "#fff",
        "padding": "2px 4px",
        "border-radius": "4px",
        "font-weight": "bold"
    }

    imageHoverZoomJavaScript = """
    // Select all image elements with the class 'zoom-image-exp2'
    const images = document.querySelectorAll('.zoom-image-exp2');

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
            "Python Developer Intern - ",
            html.a({"href": "https://practworks.com/",
                    "target": "_blank",
                    "style": {
                        "text-decoration": "none"
                    }}, "PractWorks"),
            html.a({"style": {
                "font-size": "14px",
            }}, "  (Oct 2021 - Apr 2022)")
        ),
        html.div(
            {"style": experienceItemContentDivStyle},
            html.ul(
                {"style": experienceItemListStyle},
                html.li({"style": listItemStyle}, 
                        "My task is to write ",
                        html.mark(
                            {"style": markStyle},
                            "LaTeX"
                        ),
                        " generator using Python to make non-repetitive mathematics questions for school students"),
                html.li({"style": listItemStyle}, 
                        "Python code generates Latex code that has question, answer with diagrams (dynamiaclly generated)"),
                html.li(
                            {"style": lastListItemStyle}, 
                            "Got expertise in using ",
                            html.mark(
                                {"style": markStyle},
                                "Git"
                            ),
                            ", ",
                            html.mark(
                                {"style": markStyle},
                                "GitHub"
                            ),
                            ", ",
                            html.mark(
                                {"style": markStyle},
                                "OOP"
                            ), " (Object Oriented Programming)"
                        )
            ),
            PopUpImage1(),
        ),
        html.script(imageHoverZoomJavaScript)
    )
