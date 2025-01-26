from reactpy import component, html

from components.experienceitem1 import ExperienceItem1
from components.experienceitem2 import ExperienceItem2


@component
def ExperienceSection():
    experienceSectionHeaderText = "Experience"
    experienceSectionStyle = {
        "borderRadius": "20px",
        "backgroundColor": "#DCDCDC",
        "padding": "0px 10px 20px 10px"
    }
    
    experienceHeaderStyle = {
        "padding": "20px 50px 0px 50px"
    }
    return html.div(
        {"style":experienceSectionStyle,
        "id": "experience"},
        html.h1(
            {"style": experienceHeaderStyle},
            experienceSectionHeaderText
        ),
        # Experience 1
        ExperienceItem1(),
        ExperienceItem2()
    )
