import flet as ft

def main(page: ft.Page):
    page.title = "Fiche d'identité d'un employé"
    
    # Informations de l'employé
    info = ft.Column(
        controls=[
            ft.TextField(label="Type", value="John Doe", disabled=True),
            ft.TextField(label="Type", value="John Doe", disabled=True),
            ft.TextField(label="Type", value="John Doe", disabled=True),
            ft.TextField(label="Type", value="John Doe", disabled=True),
            ft.TextField(label="Type", value="John Doe", disabled=True)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )
    
    # Photo d'identité
    photo = ft.Image(
        src="1dc1f7e37b9e4991b1bb0e3400808f45.jpg",  # Remplace par l'URL ou chemin local de la photo
        width=150,
        height=150
    )

    # Agencement horizontal : infos à gauche, photo à droite
    layout = ft.Row(
        controls=[info, photo],
        alignment=ft.MainAxisAlignment.START,
        spacing=20,
    )
    
    # Ajout du layout dans la page
    page.add(layout)

# Lancement de l'application Flet
ft.app(target=main)
