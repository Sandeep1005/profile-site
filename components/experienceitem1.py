from reactpy import component, html, hooks


@component
def PopUpImage1():
    experienceItemImageStyle = {
        "width": "80%",
        "border-radius": "10px",
        "cursor": "pointer",
        "transition": "transform 0.3s ease"
    }

    # State to handle popup visibility
    is_visible, set_visible = hooks.use_state(False)

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
                    # html.p(
                    #     {
                    #         "style": {
                    #             "textAlign": "center",
                    #             "marginTop": "8px",
                    #             "fontWeight": "bold",
                    #         }
                    #     },
                    #     # "Certificate of recognition",
                    # ),
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
                    # html.p(
                    #     "This is some descriptive text on the right side of the popup. "
                    #     "You can write anything here to complement the image and its caption."
                    # ),
                    html.ul(
                        {"style": popupListStyle},
                        html.li(
                            {"style": listItemStyle},
                            "This is the certificate of recognition for adding me to Fast Track Career program."
                        ),
                        html.li(
                            {"style": listItemStyle},
                            "It involves getting more responsibilities, and more growth opportunities"
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
                                              "href": "https://www.linkedin.com/posts/bysandeep_i-want-to-thank-decimal-point-analytics-for-activity-7030878035490783233-EJXp?utm_source=share&utm_medium=member_desktop"
                                          },
                                          "LinkedIn post"
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
            "Senior Data Scientist - ",
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
                {"style": experienceItemListStyle},
                html.li({"style": listItemStyle}, 
                        "Finetuning LLMs (",
                        html.mark({"style": markStyle}, "Llama"), 
                        " 7B, 13B) using LoRA, QLoRA, building ",
                        html.mark({"style": markStyle}, "RAG"),
                        " architecture for QA tasks"),
                html.li({"style": listItemStyle}, 
                        "Forecasting financial indicators and traffic volume using deep learning: TiDE, SOFTS, etc."),
                html.li({"style": listItemStyle}, 
                        "Stock trend prediction using Reinforcement Learning - DQN, DDPG, PPO"),
                html.li({"style": listItemStyle}, 
                        "MLOps infra: ", 
                        html.mark({"style": markStyle}, "MLFlow"), ", ", 
                        html.mark({"style": markStyle}, "DVC"), ", ", 
                        html.mark({"style": markStyle}, "Jenkins"), ", ",
                        html.mark({"style": markStyle}, "Docker"), " (private repo), ",
                        html.mark({"style": markStyle}, "OCI GPUs"),
                        " and local GPUs"),
                html.li({"style": listItemStyle}, 
                        "Recognised by the company by Fast Track Career program"),
                html.li({"style": lastListItemStyle}, 
                        "Won an internal hackathon in financial domain (ideation, plannning, MVP)"),
            ),
            PopUpImage1(),
            # PopUpImage2()
        
        ),
        html.script(imageHoverZoomJavaScript)
    )
