from reactpy import component, html, run, hooks


@component
def StickyMenu():
    navBarItemsList = ['About', 'Experience', 'Education', 'Contact']

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
