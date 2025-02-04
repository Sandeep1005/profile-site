from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from reactpy import component, html
from reactpy.backend.fastapi import configure

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


app = FastAPI()

# Serve static files (replace with your actual directory)
app.mount("/static", StaticFiles(directory="static/"), name="static")

# Configure ReactPy with FastAPI
configure(app, RootComponent)
