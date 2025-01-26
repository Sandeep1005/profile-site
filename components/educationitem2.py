from reactpy import component, html


@component
def EducationItem2():
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
    // Select all image elements with the class 'zoom-image-edu2'
    const images = document.querySelectorAll('.zoom-image-edu2');

    // Define a URL list
    const urlList = [
        'https://internshala.com/student/certificate/87186093/FDC05493-E773-5511-0909-3EC76F81C503'
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
            "B.Tech - ",
            html.a({"href": "https://www.iitp.ac.in/",
                    "target": "_blank",
                    "style": {
                        "text-decoration": "none"
                    }}, "IIT Patna"),
            html.a({"style": {
                "font-size": "14px",
            }}, "  (Aug 2015 - May 2019)")
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
                    "class_name": "zoom-image-edu2",
                    "alt": "Image",
                    "src": "https://internshala.com/uploads/student_certificates/62a2fd419b68f1654848833.png"
                },
            )
        ),
        html.script(imageHoverZoomJavaScript)
    )
