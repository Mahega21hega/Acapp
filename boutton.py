import flet as ft

def create_neon_button(text, on_click=None):
        button_container = ft.Container(
            content=ft.Text(text, weight=ft.FontWeight.BOLD, color="white"),
            width=220,
            height=50,
            border_radius=ft.border_radius.all(10),  # Corrected: ft.border_radius.all
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["redaccent700", "transparent"]
            ),
            border=ft.Border(
                left=ft.BorderSide(1, ft.colors.BLUE),
                top=ft.BorderSide(1, ft.colors.BLUE),
                right=ft.BorderSide(1, ft.colors.BLUE),
                bottom=ft.BorderSide(1, ft.colors.BLUE)
            ),  # Define each side of the border
            padding=10,
            alignment=ft.alignment.center,
            animate_opacity=300,  # Smooth fade in/out when hovered
            opacity=0.9
        )

        # Define hover event behavior
        def on_hover(e):
            new_border_color = ft.colors.YELLOW if e.data == "true" else ft.colors.BLUE
            button_container.border = ft.Border(
                left=ft.BorderSide(1, new_border_color),
                top=ft.BorderSide(1, new_border_color),
                right=ft.BorderSide(1, new_border_color),
                bottom=ft.BorderSide(1, new_border_color)
            )  # Change border color on hover
            button_container.opacity = 1 if e.data == "true" else 0.8
            button_container.update()

        # Attach hover event listener
        button_container.on_hover = on_hover
        button_container.on_click = on_click

        return button_container

