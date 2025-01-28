from reactpy import component, html, hooks, run


@component
def ImagePopup():
    # State to handle popup visibility and animation
    is_visible, set_visible = hooks.use_state(False)
    is_animating, set_animating = hooks.use_state(False)
    
    def open_popup(event):
        set_visible(True)  # Show the popup
        set_animating(True)  # Start the animation
    
    def close_popup(event):
        set_animating(False)  # Start closing animation
        
        # Use a delayed effect to hide the popup after the animation ends
        hooks.use_effect(lambda: hooks.delayed_effect(lambda: set_visible(False), 300))
    
    return html.div(
        {
            "style": {
                "position": "relative",
                "fontFamily": "Arial, sans-serif",
                "textAlign": "center",
            }
        },
        # Thumbnail image
        html.img(
            {
                "src": "https://via.placeholder.com/200",
                "alt": "Thumbnail",
                "style": {
                    "cursor": "pointer",
                    "borderRadius": "8px",
                    "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.2)",
                },
                "onClick": open_popup,
            },
        ),
        # Popup container with animation
        html.div(
            {
                "style": {
                    "display": "block" if is_visible else "none",  # Control visibility
                    "position": "fixed",
                    "top": "50%",
                    "left": "50%",
                    "transform": "translate(-50%, -50%)"
                    + (" scale(1)" if is_animating else " scale(0.9)"),
                    "opacity": "1" if is_animating else "0",
                    "transition": "opacity 0.3s ease, transform 0.3s ease",  # Smooth animations
                    "width": "80%",
                    "maxWidth": "600px",
                    "backgroundColor": "#fff",
                    "boxShadow": "0px 8px 16px rgba(0, 0, 0, 0.2)",
                    "borderRadius": "8px",
                    "zIndex": "1000",
                    "padding": "16px",
                },
            },
            html.div(
                {
                    "style": {
                        "display": "flex",
                        "flexDirection": "row",
                        "justifyContent": "flex-start",
                        "gap": "16px",
                    },
                },
                # Left side with image and caption
                html.div(
                    {
                        "style": {"flex": "1"},
                    },
                    html.img(
                        {
                            "src": "https://via.placeholder.com/300",
                            "alt": "Popup Image",
                            "style": {
                                "width": "100%",
                                "borderRadius": "8px",
                            },
                        },
                    ),
                    html.p(
                        {
                            "style": {
                                "textAlign": "center",
                                "marginTop": "8px",
                                "fontWeight": "bold",
                            }
                        },
                        "This is the caption for the image.",
                    ),
                ),
                # Right side with descriptive text
                html.div(
                    {
                        "style": {
                            "flex": "1",
                            "display": "flex",
                            "flexDirection": "column",
                            "justifyContent": "flex-start",
                            "textAlign": "justify",
                        }
                    },
                    html.p(
                        "This is some descriptive text on the right side of the popup. "
                        "You can write anything here to complement the image and its caption."
                    ),
                ),
            ),
            # Close button
            html.button(
                {
                    "style": {
                        "position": "absolute",
                        "top": "8px",
                        "right": "8px",
                        "backgroundColor": "red",
                        "color": "#fff",
                        "border": "none",
                        "borderRadius": "50%",
                        "width": "30px",
                        "height": "30px",
                        "cursor": "pointer",
                        "fontWeight": "bold",
                    },
                    "onClick": close_popup,
                },
                "×",
            ),
        ),
        # Backdrop with animation
        html.div(
            {
                "style": {
                    "display": "block" if is_visible else "none",  # Only show backdrop if visible
                    "position": "fixed",
                    "top": "0",
                    "left": "0",
                    "width": "100%",
                    "height": "100%",
                    "backgroundColor": "rgba(0, 0, 0, 0.5)",
                    "opacity": "1" if is_animating else "0",
                    "transition": "opacity 0.3s ease",
                    "zIndex": "999",
                },
                "onClick": close_popup,  # Close popup when clicking outside
            },
        ),
    )


if __name__ == '__main__':
    run(ImagePopup)