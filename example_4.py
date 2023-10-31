from reactpy import html, run, component

@component
def Photo():

    layout = html.div(
        html.h1("My Todo List"),
        html.ul(
            html.li("Build a cool new app"),
            html.li("Share it with the world!")
        ),
    html.img(
        {
            "src": "https://picsum.photos/id/237/500/300",
            "class_name": "img-fluid",
            "style": {"width": "50%", "margin_left": "0%"},
            "alt": "Billie Holiday",
        }
    )
    )
    return layout

@component
def Gallery():
    return html.section(
        html.h1("Famous Musicians"),
        Photo(),
        Photo(),
        Photo()
    )
run(Gallery)