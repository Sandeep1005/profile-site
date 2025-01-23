from reactpy import component, html, run

from intropage import IntroPage


@component
def MainComponent():
    return html.div(
        IntroPage()
    )


if __name__ == '__main__':
    run(MainComponent)
    