import flet as ft

def main(page: ft.Page):
    page.title = "Animated Login Page"

    # Variable to track the current form (sign_in_form or sign_up_form)
    current_form = "sign_in"

    def toggle_forms(e):
        nonlocal current_form
        # Toggle between 'sign_in' and 'sign_up'
        if current_form == "sign_in":
            current_form = "sign_up"
        else:
            current_form = "sign_in"
        update_form()

    # Sign In Form
    sign_in_form = ft.Container(
        content=ft.Column(
            [
                ft.Text("Welcome User!", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Sign In if you already have an account."),
                ft.TextField(label="Email", width=300),
                ft.TextField(label="Password", width=300, password=True),
                ft.ElevatedButton(text="Sign In", on_click=lambda e: print("Sign In")),
                ft.TextButton("Don't have an account? Sign Up", on_click=toggle_forms)
            ],
            alignment="center",
            horizontal_alignment="center"
        ),
        alignment=ft.alignment.center,
        width=400,
        height=400,
        border_radius=10,
        bgcolor=ft.colors.RED_ACCENT
    )

    # Sign Up Form
    sign_up_form = ft.Container(
        content=ft.Column(
            [
                ft.Text("Create Account", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Sign Up for a new account."),
                ft.TextField(label="Name", width=300),
                ft.TextField(label="Email", width=300),
                ft.TextField(label="Password", width=300, password=True),
                ft.ElevatedButton(text="Sign Up", on_click=lambda e: print("Sign Up")),
                ft.TextButton("Already have an account? Sign In", on_click=toggle_forms)
            ],
            alignment="center",
            horizontal_alignment="center"
        ),
        alignment=ft.alignment.center,
        width=400,
        height=400,
        border_radius=10,
        bgcolor=ft.colors.BLUE_ACCENT
    )

    # Function to update the form displayed with animation
    def update_form():
        if current_form == "sign_in":
            page.controls[0].content = sign_in_form
        else:
            page.controls[0].content = sign_up_form
        page.update()

    # Adding AnimatedSwitcher with the initial form (sign in)
    page.add(
        ft.AnimatedSwitcher(
            content=sign_in_form,
            transition=ft.AnimatedSwitcherTransition.SCALE,
            duration=500,
            reverse_duration=500,
        )
    )

ft.app(target=main)