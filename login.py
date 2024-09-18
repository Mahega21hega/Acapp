import flet as ft
import entreprise  # Assurez-vous que entreprise.py est dans le même répertoire

def main(page: ft.Page):
    page.title = "Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.window_width = 500
    page.window_height = 500

    def verifier_identifiants(e):
        username = username_field.value
        password = password_field.value

        if username == "admin" and password == "12345":
            page.clean()  # Effacer le contenu de la page actuelle
            entreprise.ouvrir_page_entreprise(page)  # Ouvrir la page entreprise
        else:
            page.add(ft.Text("Identifiants incorrects", color="red"))

    # Champs de saisie et bouton de connexion
    username_field = ft.TextField(label="Nom d'utilisateur", width=300)
    password_field = ft.TextField(label="Mot de passe", password=True, can_reveal_password=True, width=300)
    login_button = ft.ElevatedButton(text="Connexion", on_click=verifier_identifiants)

    # Ajout des composants à la page
    page.add(
        ft.Column(
            [
                username_field,
                password_field,
                login_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# Lancer l'application
ft.app(target=main)
