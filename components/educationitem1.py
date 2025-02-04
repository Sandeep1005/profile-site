from reactpy import component, html, hooks, run


@component
def PopUpImage1():
    educationItemImageStyle = {
        "width": "80%",
        "border-radius": "10px",
        "cursor": "pointer",
        "transition": "transform 0.3s ease"
    }

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
        "transition": "background-color 0.3s",
        "text-align": "center"
    }
    lastListItemStyle = {
        "padding": "10px 15px",
        # "border-bottom": "1px solid #ddd",
        "font-size": "16px",
        "color": "#333",
        # "cursor": "pointer",
        "transition": "background-color 0.3s",
        "text-align": "center"
    }
    markStyle = {
        "background-color": "#0D98BA",
        "color": "#fff",
        "padding": "2px 4px",
        "border-radius": "4px",
        "font-weight": "bold"
    }

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
                    "style": educationItemImageStyle,
                    "class_name": "zoom-image-edu1",
                    "alt": "Image",
                    "src": "/static/images/paperImage.png",
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
                        "flexDirection": "column",
                        "gap": "16px",
                    },
                },
                html.div(
                    {
                        "style": {
                            "flex": "1",
                        },
                    },
                    html.iframe(
                        {"src": "/static/pdfs/TIM_paper.pdf",
                        "style": {
                            "width": "100%",
                            "height": "100%",
                            "borderRadius": "10px",
                        }}
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
                    html.ul(
                        {"style": popupListStyle},
                        html.li(
                            {"style": lastListItemStyle},
                            "IEEE TIM: (Impact Factor 5.6), DOI: ",
                            html.mark({"style": markStyle},
                                      html.a(
                                          {
                                              "style": {"text-decoration": "none",
                                                        "color": "#fff"},
                                              "target": "_blank",
                                              "href": "https://ieeexplore.ieee.org/document/10616098"
                                          },
                                          "10.1109/TIM.2024.3436119"
                                      )),
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
def PopUpDemoDigitRecognizer():
    demoImageStyle = {
        "width": "80%",
        "border-radius": "10px",
        "cursor": "pointer",
        "transition": "transform 0.3s ease"
    }
    return html.div(
        html.img(
            {"style": demoImageStyle,
             "src": "https://media.licdn.com/dms/image/v2/C4D22AQHZmRYvg4064Q/feedshare-shrink_2048_1536/feedshare-shrink_2048_1536/0/1676291949097?e=2147483647&v=beta&t=d6fu7g0sNf0DYQjymgW0039TChTXoUY8G44WItF7yTk",
             "alt": "Click to scribble",
             "onclick": "openPopup()"}
        ),
        html.div(
            {"class_name": "overlay",
             "id": "overlay",
             "onclick": "closePopup()",
             "style": {
                 "display": "none",
            "position": "fixed",
            "top": "0",
            "left": "0",
            "width": "100%",
            "height": "100%",
            "background": "rgba(0, 0, 0, 0.5)",
            "z-index": "999",
             }}
        ),
        html.div(
            {"class_name": "popup",
             "id": "popup",
             "style": {
                 "display": "none",
                "position": "fixed",
                "top": "50%",
                "left": "50%",
                "transform": "translate(-50%, -50%)",
                "background": "white",
                "border": "2px solid black",
                "padding": "20px",
                "box-shadow": "0 0 10px rgba(0, 0, 0, 0.5)",
                "z-index": "1000",
             }},
             html.canvas(
                 {"id": "scribblePad",
                  "width": "200px",
                  "height": "200px",
                  "style": {
                      "border": "1px solid black",
                    "cursor": "crosshair",
                  }}
             ),
             html.br(),
             html.button(
                 {"onclick": "clearCanvas()"},
                 "clear"
             ),
             html.button(
                 {"onclick": "closePopup()"},
                 "Close"
             )
        ),
        html.script(
            """
            let canvas = document.getElementById("scribblePad");
            let ctx = canvas.getContext("2d");
            let drawing = false;
            
            canvas.addEventListener("mousedown", (event) => {
                drawing = true;
                ctx.beginPath(); // Start a new path on mouse down
                ctx.moveTo(event.offsetX, event.offsetY);
            });
            
            canvas.addEventListener("mouseup", () => drawing = false);
            canvas.addEventListener("mousemove", draw);
            
            function draw(event) {
                if (!drawing) return;
                ctx.lineWidth = 3;
                ctx.lineCap = "round";
                ctx.strokeStyle = "black";
                ctx.lineTo(event.offsetX, event.offsetY);
                ctx.stroke();
                ctx.beginPath();
                ctx.moveTo(event.offsetX, event.offsetY);
            }
            
            function clearCanvas() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                ctx.beginPath(); // Reset path to prevent line continuation
            }
            
            function openPopup() {
                document.getElementById("popup").style.display = "block";
                document.getElementById("overlay").style.display = "block";
            }
            
            function closePopup() {
                document.getElementById("popup").style.display = "none";
                document.getElementById("overlay").style.display = "none";
            }
"""
        )
    )


@component
def PopUpImage2():
    educationItemImageStyle = {
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
                    "style": educationItemImageStyle,
                    "class_name": "zoom-image-edu1",
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
def EducationItem1():
    educationItemstyle = {
        "background-color": "#00CEC8",
        "padding": "10px 20px 10px 20px",
        "margin": "15px",
        "border-radius": "20px"
    }
    educationItemHeaderStyle = {
        "padding": "0px 50px 20px 50px"
    }
    educationItemContentDivStyle = {
        "display": "flex",
        "flex-direction": "row",
        "justify-content": "space-between",
        "align-items": "center"
    }
    educationItemListStyle = {
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
    // Select all image elements with the class 'zoom-image-edu1'
    const images = document.querySelectorAll('.zoom-image-edu1');

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
        {"style": educationItemstyle},
        html.h2(
            {"style": educationItemHeaderStyle},
            "M.Tech - ",
            html.a({"href": "https://www.iitk.ac.in/",
                    "target": "_blank",
                    "style": {
                        "text-decoration": "none"
                    }}, "IIT Kanpur"),
            html.a({"style": {
                "font-size": "14px",
            }}, "  (Aug 2020 - May 2022)")
        ),
        html.div(
            {"style": educationItemContentDivStyle},
            html.ul(
                {"style": educationItemListStyle},
                html.li({"style": listItemStyle},
                        "For my thesis, I designed and made the components of a cost-effective, portable, not-destructive method to measure prestress in beams."),
                html.li({"style": listItemStyle},
                        "DIC for displacement measurement with time -> FFT for natural frequency -> analytical relations for prestress"),
                html.li({"style": listItemStyle},
                        "Published this work in ",
                        html.mark({"style": markStyle},
                                  "IEEE TIM"),
                        " (Transactions in Instrumentation and Measurement) journal"),
                html.li({"style": lastListItemStyle},
                        "Did a course on fundamentals of AI/ML. As a part of course work, built a digit recognizer from scratch including back-propagation"),
            ),
            PopUpImage1(),
            PopUpImage2()
            # PopUpDemoDigitRecognizer()
        ),
        html.script(imageHoverZoomJavaScript)
    )


if __name__ == "__main__":
    run(PopUpDemoDigitRecognizer)
