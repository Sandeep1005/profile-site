from reactpy import component, html, run, hooks


@component
def MainSection():
    samplecontent = """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
"""

    return html.div(
        html.div(
            {"style": {
                "position": "sticky",
                "top": "0",
                "background": "rgba(13, 152, 186, 0)",  # First color
                "padding": "15px 0",  # Add some padding for spacing
                "z-index": "1000",
            }},
            html.nav(
                {"style":{
                    "background": "#ECECEC",
                    "margin": "0% 0% 0% 50%",
                    "padding": "10px 0px 10px 0px",
                    "borderRadius": "50px 0px 0px 50px",
                    "text-align": "center" 
                }},
                html.a(
                    {"style": {
                        "margin": "20px",  # Equal margin between items
                        "font-weight": "bold",  # Bold text
                        "font-size": "20px",  # Bigger font size
                        "color": "#0D98BA",
                        "text-decoration": "none",  # Remove underline from links
                        },
                    "href": "#home"},
                    "Home"
                ),
                html.a(
                    {"style":{
                        "margin": "20px",  # Equal margin between items
                        "font-weight": "bold",  # Bold text
                        "font-size": "20px",  # Bigger font size
                        "color": "#0D98BA",
                        "text-decoration": "none",  # Remove underline from links
                    },
                    "href": "#about"},
                    "About"
                ),
                html.a(
                    {"style": {
                        "margin": "20px 40px 20px 20px",  # Equal margin between items
                        "font-weight": "bold",  # Bold text
                        "font-size": "20px",  # Bigger font size
                        "color": "#0D98BA",
                        # "background": "#00CEC8",
                        "text-decoration": "none",  # Remove underline from links
                    },
                    "href": "#contact"},
                    "Contact"
                )
            )
        ),
        # Sections with headers and text
        html.section(
            {"id": "home"},
            html.h2("Home Section"),
            html.p(samplecontent*5)
        ),
        html.section(
            {"id": "about"},
            html.h2("About Section"),
            html.p(samplecontent*5)
        ),
        html.section(
            {"id": "contact"},
            html.h2("Contact Section"),
            html.p(samplecontent*5)
        ),
    )


@component
def MainPage():
    return html.div(MainSection())
