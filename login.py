import flet as ft
import time
import entreprise  # Assurez-vous que entreprise.py est dans le même répertoire

def main(page: ft.Page):
    page.title = "Login"
    page.theme_mode = ft.ThemeMode.SYSTEM

    # Fixer la taille minimale de la fenêtre
    page.window.width = 350
    page.window.height = 400
    page.window.resizable = False
    page.window.maximizable = False
    page.window.minimizable = False
    page.window.center()

    # Styles personnalisés
    def apply_styles(textfield):
        textfield.border_color = ft.colors.BLUE_GREY_300
        textfield.focused_border_color = ft.colors.BLUE_500
        textfield.filled = True
        textfield.filled_color = ft.colors.WHITE
        textfield.color = ft.colors.BLACK

    # Indicateur de chargement pour la connexion
    loading_indicator = ft.ProgressBar(width=300, visible=False)

    # Widgets pour afficher les erreurs, invisibles par défaut
    username_error = ft.Text("", color=ft.colors.RED_500, size=12, visible=False)
    password_error = ft.Text("", color=ft.colors.RED_500, size=12, visible=False)

    # Vérification des identifiants
    def verifier_identifiants(e):
        username = username_field.value
        password = password_field.value

        # Réinitialiser les messages d'erreur et les rendre invisibles
        username_error.value = ""
        password_error.value = ""
        username_error.visible = False
        password_error.visible = False

        if username == "" or password == "":
            if username == "":
                username_error.value = "Le nom d'utilisateur est requis"
                username_error.visible = True
            if password == "":
                password_error.value = "Le mot de passe est requis"
                password_error.visible = True
        elif username != "admin" or password != "12345":
            username_error.value = "Nom d'utilisateur ou mot de passe incorrect"
            username_error.visible = True
        else:
            # Effacer la page actuelle et ouvrir la page entreprise si tout est correct
            page.clean()
            entreprise.ouvrir_page_entreprise(page)

        page.update()

    # Page d'inscription
    def afficher_page_inscription(e):
        page.clean()
        username_signup_field = ft.TextField(label="Nom d'utilisateur", width=300)
        password_signup_field = ft.TextField(label="Mot de passe", password=True, can_reveal_password=True, width=300)
        confirm_password_field = ft.TextField(label="Confirmer mot de passe", password=True, can_reveal_password=True, width=300)

        # Messages d'erreur pour l'inscription, invisibles par défaut
        signup_username_error = ft.Text("", color=ft.colors.RED_500, size=12, visible=False)
        signup_password_error = ft.Text("", color=ft.colors.RED_500, size=12, visible=False)

        apply_styles(username_signup_field)
        apply_styles(password_signup_field)
        apply_styles(confirm_password_field)

        signup_button = ft.ElevatedButton(
            text="S'inscrire",
            on_click=lambda e: inscrire_utilisateur(username_signup_field, password_signup_field, confirm_password_field, signup_username_error, signup_password_error),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=15),
                bgcolor=ft.colors.BLUE_500,
                color=ft.colors.WHITE,
                padding=10,
                elevation=4,
            )
        )

        page.add(
            ft.Column(
                [
                    ft.Text("S'inscrire", style=ft.TextThemeStyle.HEADLINE_SMALL, color=ft.colors.BLUE_500),
                    username_signup_field,
                    signup_username_error,  # Afficher le message d'erreur sous le champ
                    password_signup_field,
                    confirm_password_field,
                    signup_password_error,  # Afficher le message d'erreur pour le mot de passe
                    signup_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,  # Réduire l'espace vertical
            )
        )

    # Gestion de l'inscription utilisateur
    def inscrire_utilisateur(username_field, password_field, confirm_password_field, signup_username_error, signup_password_error):
        signup_username_error.value = ""
        signup_password_error.value = ""
    
        if username_field.value == "" or password_field.value == "" or confirm_password_field.value == "":
            if username_field.value == "":
                signup_username_error.value = "Le nom d'utilisateur est requis"
                signup_username_error.visible = True
            if password_field.value == "" or confirm_password_field.value == "":
                signup_password_error.value = "Le mot de passe est requis"
                signup_password_error.visible = True
            elif password_field.value != confirm_password_field.value:
                signup_password_error.value = "Les mots de passe ne correspondent pas"
                signup_password_error.visible = True
        else:
            page.clean()
            page.add(ft.Text("Inscription réussie !", color=ft.colors.GREEN_500))
            time.sleep(1)
            main(page)  # Retour à la page de connexion après succès

        page.update()


    # Champs de saisie et boutons pour la page de connexion
    username_field = ft.TextField(label="Nom d'utilisateur", width=300, prefix_icon=ft.Icon(ft.icons.PERSON))
    password_field = ft.TextField(label="Mot de passe", password=True, can_reveal_password=True, width=300, prefix_icon=ft.Icon(ft.icons.LOCK))

    apply_styles(username_field)
    apply_styles(password_field)

    login_button = ft.ElevatedButton(
        text="Connexion",
        on_click=verifier_identifiants,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=15),
            bgcolor=ft.colors.GREEN_500,
            color=ft.colors.WHITE,
            padding=10,
            elevation=4,
        )
    )

    signup_button = ft.TextButton(
        text="S'inscrire",
        on_click=afficher_page_inscription,
        style=ft.ButtonStyle(
            color=ft.colors.BLUE_500,
            padding=10,
        )
    )

    # Interface utilisateur centrée et responsive
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Connexion", style=ft.TextThemeStyle.HEADLINE_MEDIUM, color=ft.colors.BLUE_500),
                    username_field,
                    username_error,  # Afficher le message d'erreur sous le champ username
                    password_field,
                    password_error,  # Afficher le message d'erreur sous le champ password
                    login_button,
                    signup_button,
                    loading_indicator,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,  # Réduire l'espace vertical
                expand=True
            ),
            padding=ft.padding.all(20),
            width=page.window.width,
            height=page.window.height,
            alignment=ft.alignment.center,
        )
    )

# Lancer l'application
ft.app(target=main)

