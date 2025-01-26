from reactpy import component, html


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
        "justify-content": "space-between",
        "align-items": "center"
    }
    experienceItemParagraphStyle = {
        "width": "50%",
        "margin": "0px 20px 20px 20px",
        "padding": "0px 80px 0px 80px",
        "font-size": "18px",
        "color": "black",
        "font-family": "Arial, sans-serif",
    }
    experienceItemImageStyle = {
        "width": "13%",
        "margin": "10px",
        "border-radius": "10px",
        "aligh-items": "center",
        "cursor": "pointer",
        "transition": "transform 0.3s ease"
    }

    imageHoverZoomJavaScript = """
    // Select all image elements with the class 'zoom-image-exp2'
    const images = document.querySelectorAll('.zoom-image-exp2');

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
                {"style": experienceItemParagraphStyle},
                html.li("some words about this experience"),
                html.li("some words about this experience"),
                html.li("some words about this experience"),
                html.li("some words about this experience"),
                html.li("some words about this experience"),
            ),
            # html.p(
            #     {"style": experienceItemParagraphStyle},
            #     "some words about this experience"
            # ),
            html.img(
                {
                    "style": experienceItemImageStyle,
                    "class_name": "zoom-image-exp2",
                    "alt": "Image",
                    "src": "https://internshala.com/uploads/student_certificates/62a2fd419b68f1654848833.png"
                },
            )
        ),
        html.script(imageHoverZoomJavaScript)
    )
