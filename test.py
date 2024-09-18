import flet as ft

def main(page: ft.Page):
    page.title = "Fiche d'identité d'un employé"
    page.padding = 20
    page.spacing = 20
    page.theme_mode = "dark"
    
    # Informations de l'employé avec des bordures et du style
    info = ft.Column(
        controls=[
            ft.TextField(label="Nom", value="John Doe", disabled=True, width=300, border_radius=5, filled=True),
            ft.TextField(label="Poste", value="Développeur", disabled=True, width=300, border_radius=5, filled=True),
            ft.TextField(label="Département", value="Informatique", disabled=True, width=300, border_radius=5, filled=True),
            ft.TextField(label="Email", value="john.doe@example.com", disabled=True, width=300, border_radius=5, filled=True),
            ft.TextField(label="Téléphone", value="+261 34 00 000 00", disabled=True, width=300, border_radius=5, filled=True),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15,
    )
    
    # Photo d'identité avec un cadre arrondi et ombre
    photo = ft.Container(
        content=ft.Image(
            src="1dc1f7e37b9e4991b1bb0e3400808f45.jpg",  # Remplacer par l'URL ou chemin local de la photo
            width=200,
            height=200,
            fit=ft.ImageFit.COVER,
        ),
        border_radius=ft.border_radius.all(10),
        width=200,
        height=200,
        padding=5,
        bgcolor=ft.colors.WHITE70,
        alignment=ft.alignment.top_left,
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=10,
            color=ft.colors.with_opacity(0.2, 'BLACK'),
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
