import flet as ft

def main(page: ft.Page):
    page.title = "Fiche d'identité d'un employé"
    page.padding = 20
    page.spacing = 20
    page.theme_mode = "dark"

    # Style personnalisé pour les champs d'informations
    def create_info_row(icon, label, value):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(icon, size=24, color=ft.colors.BLUE),
                    ft.Column(
                        [
                            ft.Text(label, weight="bold", color=ft.colors.BLACK87),
                            ft.Text(value, color=ft.colors.BLACK54)
                        ],
                        spacing=2
                    )
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
            padding=10,
            border_radius=10,
            bgcolor=ft.colors.BLUE_GREY_200,
            
        )

    # Liste des informations avec des icônes et une présentation plus attrayante
    info = ft.Column(
        controls=[
            create_info_row(ft.icons.PERSON, "Nom", "John Doe"),
            create_info_row(ft.icons.WORK, "Poste", "Développeur"),
            create_info_row(ft.icons.APARTMENT, "Département", "Informatique"),
            create_info_row(ft.icons.EMAIL, "Email", "john.doe@example.com"),
            create_info_row(ft.icons.PHONE, "Téléphone", "+261 34 00 000 00")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    # Photo d'identité avec un cadre arrondi et ombre
    photo = ft.Container(
        content=ft.Image(
            src="1dc1f7e37b9e4991b1bb0e3400808f45.jpg",  # Remplacer par l'URL ou chemin local de la photo
            width=150,
            height=150,
            fit=ft.ImageFit.COVER,
        ),
        border_radius=ft.border_radius.all(75),
        width=150,
        height=150,
        padding=5,
        bgcolor=ft.colors.GREY_200,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=10,
            color=ft.colors.with_opacity(0.2,'black'),
            offset=ft.Offset(3, 3)
        )
    )

    # Agencement responsive : infos à gauche, photo à droite
    layout = ft.ResponsiveRow(
        controls=[
            ft.Column(
                [info],
                col={"xs": 12, "md": 8},  # Prend 8 colonnes sur 12 en mode desktop et tout l'espace sur mobile
            ),
            ft.Column(
                [photo],
                col={"xs": 12, "md": 4},  # Prend 4 colonnes sur desktop et tout l'espace sur mobile
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=30,
    )

    # Ajout du layout dans la page
    page.add(layout)

# Lancement de l'application Flet
ft.app(target=main)
