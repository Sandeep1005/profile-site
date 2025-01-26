from reactpy import component, html, run

from components.intropage import IntroPage
from components.stickymenu import StickyMenu
from components.aboutsection import AboutSection
from components.contactsection import ContactSection
from components.experiencesection import ExperienceSection
from components.educationsection import EducationSection


@component
def RootComponent():
    return html.div(
        IntroPage(),
        html.div(
            StickyMenu(),
            AboutSection(),
            ExperienceSection(),
            EducationSection(),
            ContactSection()
        )
    )


if __name__ == '__main__':
    run(RootComponent)
    