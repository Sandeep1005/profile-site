import reactpy as rp
from reactpy import html
from reactpy import hooks


def SignaturePad():
    return html.div(
        {"class_name": "canvas-container"},
        html.canvas(
            {"class_name": "drawingCanvas",
             "style": {
                 "width": "500px",
                 "height": "500px"
             }},
            html.div(
                html.button(
                    {"id": "clearBtn",
                     "class_name": "clear-btn"}
                )
            )
        ),
    html.script("""
        const canvas = document.getElementById("drawingCanvas");
        const ctx = canvas.getContext("2d");
        const colorPicker = document.getElementById("colorPicker");
        const clearBtn = document.getElementById("clearBtn");

        let drawing = false;
        let currentColor = "#000000";

        // Set up drawing functionality
        canvas.addEventListener("mousedown", (e) => {
        drawing = true;
        ctx.beginPath(); // Reset the drawing path
        draw(e);
        });

        canvas.addEventListener("mousemove", (e) => {
        if (drawing) {
            draw(e);
        }
        });

        canvas.addEventListener("mouseup", () => {
        drawing = false;
        });

        // Function to draw on canvas
        function draw(e) {
        ctx.lineWidth = 5;
        ctx.lineCap = "round";
        ctx.strokeStyle = currentColor;
        
        const rect = canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        ctx.lineTo(x, y);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(x, y);
        }

        // Change color based on the color picker
        colorPicker.addEventListener("input", (e) => {
        currentColor = e.target.value;
        });

        // Clear the canvas
        clearBtn.addEventListener("click", () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.beginPath(); // Reset the path when canvas is cleared
        });
        """
        )
    )

# Rendering the layout component
rp.run(SignaturePad)
