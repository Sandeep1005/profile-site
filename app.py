from reactpy import component, html, run

from components.intropage import IntroPage
from components.mainpage import MainPage


@component
def RootComponent():
    return html.div(
        IntroPage(),
        MainPage()
    )


if __name__ == '__main__':
    run(RootComponent)
    