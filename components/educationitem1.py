from reactpy import component, html


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
    educationItemParagraphStyle = {
        "width": "50%",
        "margin": "0px 20px 20px 20px",
        "padding": "0px 80px 0px 80px",
        "font-size": "18px",
        "color": "black",
        "font-family": "Arial, sans-serif",
    }
    educationItemImageStyle = {
        "width": "13%",
        "margin": "10px",
        "border-radius": "10px",
        "aligh-items": "center",
        "cursor": "pointer",
        "transition": "transform 0.3s ease"
    }

    imageHoverZoomJavaScript = """
    // Select all image elements with the class 'zoom-image-edu1'
    const images = document.querySelectorAll('.zoom-image-edu1');

    // Define a URL list
    const urlList = [
        'https://www.linkedin.com/posts/bysandeep_i-want-to-thank-decimal-point-analytics-for-activity-7030878035490783233-EJXp?utm_source=share&utm_medium=member_desktop',
        'https://example.com/page2'
    ];

    // Loop through each image and attach event listeners
    images.forEach((image, index) => {
        image.addEventListener('mouseover', () => {
            image.style.transform = 'scale(1.1)'; // Apply the zoom effect
        });

        image.addEventListener('mouseout', () => {
            image.style.transform = 'scale(1)'; // Reset to the original size
        });

        image.addEventListener('click', () => {
            const url = urlList[index]; // Get the URL corresponding to the image's index
            window.open(url, '_blank'); // Open the URL in a new tab
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
                {"style": educationItemParagraphStyle},
                html.li("some words about this education"),
                html.li("some words about this education"),
                html.li("some words about this education"),
                html.li("some words about this education"),
                html.li("some words about this education"),
            ),
            html.img(
                {
                    "style": educationItemImageStyle,
                    "class_name": "zoom-image-edu1",
                    "alt": "Image",
                    "src": "https://media.licdn.com/dms/image/v2/C4D22AQHZmRYvg4064Q/feedshare-shrink_2048_1536/feedshare-shrink_2048_1536/0/1676291949097?e=2147483647&v=beta&t=d6fu7g0sNf0DYQjymgW0039TChTXoUY8G44WItF7yTk"
                },
            ),
            html.img(
                {
                    "style": educationItemImageStyle,
                    "class_name": "zoom-image-edu1",
                    "alt": "Image",
                    "src": "https://media.licdn.com/dms/image/v2/C4D22AQHZmRYvg4064Q/feedshare-shrink_2048_1536/feedshare-shrink_2048_1536/0/1676291949097?e=2147483647&v=beta&t=d6fu7g0sNf0DYQjymgW0039TChTXoUY8G44WItF7yTk"
                }
            )
        ),
        html.script(imageHoverZoomJavaScript)
    )
