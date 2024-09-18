import flet as ft

def main(page: ft.Page):

    page.title = "NavigationBar Example"
    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Explore",
            ),
        ]
    )
    page.add(
        ft.Column(
            [
                nav_bar,
                ft.Text("Body!")
                
            ]
        )
    )

ft.app(main)