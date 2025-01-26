from reactpy import component, html

from components.educationitem1 import EducationItem1
from components.educationitem2 import EducationItem2


@component
def EducationSection():
    educationSectionHeaderText = "Education"
    educationSectionStyle = {
        "borderRadius": "20px",
        "backgroundColor": "#DCDCDC",
        "padding": "0px 10px 20px 10px"
    }
    
    educationHeaderStyle = {
        "padding": "20px 50px 0px 50px"
    }
    return html.div(
        {"style":educationSectionStyle,
        "id": "education"},
        html.h1(
            {"style": educationHeaderStyle},
            educationSectionHeaderText
        ),
        # education 1
        EducationItem1(),
        EducationItem2()
    )
