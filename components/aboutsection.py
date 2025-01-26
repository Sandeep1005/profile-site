from reactpy import component, html


@component
def AboutSection():
    aboutSectionHeaderText = "About Me"
    aboutSectionContentText = """
    I am an engineer passionate about technology in general, specifically Data Science, Robotics and Automation. Currently I am working as a Data Scientist at Decimal Point Analytics Pvt. Ltd.
"""

    aboutSectionStyle = {
        "borderRadius": "20px",
        "backgroundColor": "#DCDCDC"
    }
    aboutHeaderStyle = {
        "padding": "20px 50px 20px 50px"
    }
    aboutContentDivStyle = {
        "display": "flex",
        "flexDirection": "row",
        "gap": "16px",
        "justifyContent": "flex-start",
        "alignItems": "center",
        "padding": "10px",
    }
    aboutContentStyle = {
        "width": "30%",
        "padding": "20px",
        "margin": "0px 100px 30px 100px",
        "font-size": "18px",
        "color": "black",
        "font-family": "Arial, sans-serif",
        "borderRadius": "20px",
        "backgroundColor": "#00CEC8"
    }
    aboutImageStyle = {
        "width": "40%",
        "padding": "20px",
        "borderRadius": "20px",
        "margin": "20px"
    }
    return html.div(
        {"style": aboutSectionStyle,
         "id": "about"},
        html.h1(
            {"style": aboutHeaderStyle},
            aboutSectionHeaderText
        ),
        html.div(
            {"style": aboutContentDivStyle},
            html.p(
                {"style": aboutContentStyle},
                aboutSectionContentText
            ),
            # html.img(
            #     {
            #         "src": "https://www.datasciencecentral.com/wp-content/uploads/2023/06/AdobeStock_552748421-scaled-e1714159983483.jpeg",
            #         "alt": "About Image",
            #         "style": aboutImageStyle,
            #     }
            # ),
        
        )
    )
