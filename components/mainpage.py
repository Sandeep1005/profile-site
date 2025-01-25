from reactpy import component, html, run, hooks


@component
def StickyMenu():
    navBarItemsList = ['About', 'Contact']

    stickyMenuStyle = {
        "position": "sticky",
        "top": "0",
        "background": "rgba(13, 152, 186, 0)",  # First color
        "padding": "15px 0",  # Add some padding for spacing
        "z-index": "1000",
    }
    navBarStyle = {
        "background": "#0D98BA",
        "margin": "0% 0% 0% 50%",
        "padding": "10px 0px 10px 0px",
        "borderRadius": "50px 0px 0px 50px",
        "text-align": "center" 
    }
    navBarItemStyle = {
        "margin": "20px",  # Equal margin between items
        "font-weight": "bold",  # Bold text
        "font-size": "20px",  # Bigger font size
        "color": "black",
        "text-decoration": "none",  # Remove underline from links
    }

    navchildren = [
        html.a(
            {"style": navBarItemStyle,
            "href": "#"+item.lower()},
            item
        ) for item in navBarItemsList
    ]

    return html.div(
            {"style": stickyMenuStyle},
            html.nav(
                {"style":navBarStyle},
                *navchildren
            )
        )


@component
def AboutSection():
    aboutSectionHeaderText = "About Me"
    aboutSectionContentText = """
    I am an engineer passionate about technology in general, specifically Data Science, Robotics and Automation. Currently I am working as a Data Scientist at Decimal Point Analytics Pvt. Ltd.
"""

    aboutSectionStyle = {
        "borderRadius": "20px",
        "background": "#DCDCDC"
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
        "background": "#00CEC8"
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


@component
def ContactSection():
    samplecontent = """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
"""

    contactSectionHeaderText = "Contact"
    contactSectionContentText = samplecontent*5

    contactSectionStyle = {

    }
    contactHeaderStyle = {

    }
    contactContentStyle = {

    }
    return html.div(
        {"style": contactSectionStyle,
         "id": "contact"},
        html.h1(
            {"style": contactHeaderStyle},
            contactSectionHeaderText
        ),
        html.p(
            {"style": contactContentStyle},
            contactSectionContentText
        )
    )


@component
def MainSection():
    samplecontent = """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
"""

    return html.div(
        StickyMenu(),
        AboutSection(),
        ContactSection()
    )


@component
def MainPage():
    return html.div(MainSection())
