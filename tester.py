import flet as ft

def main(page: ft.Page):
    
    def switch_to_signup(e):
        signin_container.visible = False
        signup_container.visible = True
        page.update()

    def switch_to_signin(e):
        signup_container.visible = False
        signin_container.visible = True
        page.update()

    # Sign In Container
    signin_container = ft.Container(
        content=ft.Column([
            ft.Text("Sign In", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
            ft.TextField(label="Email"),
            ft.TextField(label="Password", password=True),
            ft.ElevatedButton("Continue", icon=ft.icons.ARROW_FORWARD),
            ft.TextButton("Don't have an account? Sign up", on_click=switch_to_signup),
        ], alignment=ft.MainAxisAlignment.CENTER),
        padding=20,
        width=300,
        height=300,
        visible=True,
        alignment=ft.alignment.center,
        animate_opacity=300
    )

    # Sign Up Container
    signup_container = ft.Container(
        content=ft.Column([
            ft.Text("Sign Up", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
            ft.TextField(label="Full Name"),
            ft.TextField(label="Email"),
            ft.TextField(label="Password", password=True),
            ft.ElevatedButton("Sign Up", icon=ft.icons.ARROW_FORWARD),
            ft.TextButton("Already have an account? Sign in", on_click=switch_to_signin),
        ], alignment=ft.MainAxisAlignment.CENTER),
        padding=20,
        width=300,
        height=300,
        visible=False,
        alignment=ft.alignment.center,
        animate_opacity=300
    )

    # Adding both forms to the page
    page.add(ft.Column([
        signin_container,
        signup_container
    ], alignment=ft.MainAxisAlignment.CENTER))

ft.app(target=main)
