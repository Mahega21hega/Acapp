import flet as ft

def main(page: ft.Page):
    page.bgcolor=ft.colors.GREY_800
    # Fonction pour gérer la soumission du formulaire

    # Création des champs de formulaire
    carte_field = ft.Row([ft.Text("carte d'adhésion:",width=130),ft.TextField("",expand=True)])
    visite_field = ft.Row([ft.Text("Visite d'embauche:",width=130),ft.TextField("",expand=True)])
    systé_field = ft.Row([ft.Text("Visite systématique:",width=130),ft.TextField("",expand=True)])

    # Ajout des éléments au formulaire
    page.add(
        ft.Column(
            controls=[
                carte_field,
                visite_field,
                systé_field
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

# Lancer l'application
ft.app(target=main)
