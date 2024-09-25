import flet as ft
from flet import (
    Column,
    Container,
    Row,
    Text,
    ElevatedButton,
    TextField,
    alignment,
    border_radius,
    colors,
    padding,
    margin,
)

def build_employee_form(page):
    conjoint_group = ft.Column([
        ft.Text("Conjoint:"),
        ft.Row([ft.Text("Nom:",width=120),ft.TextField("")]),
        ft.Row([ft.Text("Prénom:",width=120),ft.TextField("")]),
        ft.Row([ft.Text("Date de naissance:",width=120),ft.TextField("")])
    ], visible=False)

    # Fonction pour gérer l'affichage de nationalités personnalisées
    def on_nationality_change(e):
        nationality_input.visible = e.control.value == "Autre"
        page.update()

    def add_new_nationality(e):
        new_nationality = nationality_input.value
        if new_nationality:
            nationality_dropdown.options.append(ft.dropdown.Option(new_nationality))
            nationality_dropdown.value = new_nationality
            nationality_input.value = ""
            nationality_input.visible = False
        page.update()

    nationality_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Malgache"),
            ft.dropdown.Option("Français(e)"),
            ft.dropdown.Option("Anglais(e)"),
            ft.dropdown.Option("Autre")
        ],
        on_change=on_nationality_change
    )

    nationality_input = ft.TextField(
        label="Saisir une autre nationalité",
        visible=False,
        on_submit=add_new_nationality
    )

    # Fonction pour gérer l'affichage des conjoints et de la situation personnalisée
    def on_situation_change(e):
        conjoint_group.visible = e.control.value == "Marié(e)"
        situation_input.visible = e.control.value == "Autre"
        page.update()

    def add_new_situation(e):
        new_situation = situation_input.value
        if new_situation:
            situation_dropdown.options.append(ft.dropdown.Option(new_situation))
            situation_dropdown.value = new_situation
            situation_input.value = ""
            situation_input.visible = False
        page.update()

    situation_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Marié(e)"),
            ft.dropdown.Option("Célibataire"),
            ft.dropdown.Option("Autre")
        ],
        on_change=on_situation_change
    )

    situation_input = ft.TextField(
        label="Saisir une autre situation matrimoniale",
        visible=False,
        on_submit=add_new_situation
    )

    enfant_group = ft.Column([])

    def update_enfants(nb_enfants):
        enfant_group.controls.clear()
        for i in range(nb_enfants):
            enfant_group.controls.append(
                ft.Column([
                    ft.Text(f"Enfant {i + 1}: "),
                    ft.Row([ft.Text("Nom:",width=120),ft.TextField("")]),
                    ft.Row([ft.Text("Prénoms:",width=120),ft.TextField("")]),
                    ft.Row([ft.Text("Sexe:",width=120),ft.TextField("")]),
                    ft.Row([ft.Text("Date de naissance:",width=120),ft.TextField("")]),
                    ft.Row([ft.Text("Enfant à charge:"), ft.Checkbox(label="Oui"),ft.Checkbox("Non")])
                ], expand=True)
            )
        enfant_group.update()

    def on_enfant_number_change(e):
        try:
            nb_enfants = int(e.control.value)
            update_enfants(nb_enfants)
        except ValueError:
            enfant_group.controls.clear()
            enfant_group.update()

    enfant_counter_field = ft.Row([
        ft.Text("Nombre d'enfant:",width=120),
        ft.TextField(value="0", on_change=on_enfant_number_change)
    ], expand=True)

    # Sections principales du formulaire
    form_fields = [
        ft.Row([ft.Text("Matricule:",width=120), ft.TextField()], expand=True),
        ft.Row([ft.Text("Civilité:",width=120), ft.TextField()], expand=True),
        ft.Row([ft.Text("Nom:",width=120), ft.TextField(), ft.Text("Prénoms:",width=120), ft.TextField()], expand=True),
        ft.Row([ft.Text("Date de naissance:",width=120), ft.TextField(), ft.Text("Lieu de naissance:",width=120), ft.TextField()], expand=True),
        ft.Row([ft.Text("N°CIN:",width=120), ft.TextField(), ft.Text("Date CIN:",width=120), ft.TextField(), ft.Text("Lieu CIN:"), ft.TextField()], expand=True),
        ft.Row([ft.Text("Duplicata:"), ft.Text("Date:",width=50), ft.TextField(), ft.Text("Lieu:",width=120), ft.TextField()], expand=True),
        ft.Row([ft.Text("Adresse:",width=120), ft.TextField()], expand=True),
        ft.Row([ft.Text("E-mail:",width=120), ft.TextField()], expand=True),
        ft.Row([ft.Text("N°téléphone:",width=120), ft.TextField()], expand=True),
        ft.Row([ft.Text("Nationalité:",width=120), nationality_dropdown], expand=True),
        nationality_input,
        ft.Row([ft.Text("Situation matrimoniale:",width=120), situation_dropdown], expand=True),
        situation_input,
        conjoint_group,
        enfant_counter_field,
        enfant_group
    ]

    # Cadre de la photo avec bordure et espace
    photo_id_container = ft.Container(
        content=ft.Image(src="1dc1f7e37b9e4991b1bb0e3400808f45.jpg", width=150, height=150),
        alignment=alignment.center,
        border_radius=border_radius.all(10),
        width=150,
        height=150,
        bgcolor=colors.GREY_400,
        padding=padding.all(10),
    )

    # Formulaire avec scroll si nécessaire et espacement entre sections
    form_column = ft.Column(form_fields, expand=True, spacing=20)

    # Boutons d'action avec styles améliorés
    buttons_row = ft.Row([
        ElevatedButton(text="Enregistrer", on_click=save_data, bgcolor=colors.GREEN_400, color=colors.WHITE),
        ElevatedButton(text="Ajouter nouveau", on_click=save_and_new, bgcolor=colors.BLUE_400, color=colors.WHITE),
        ElevatedButton(text="Continuer", on_click=save_and_continue, bgcolor=colors.ORANGE_400, color=colors.WHITE),
        ElevatedButton(text="Supprimer", on_click=delete_data, bgcolor=colors.RED_400, color=colors.WHITE),
    ], alignment=ft.MainAxisAlignment.END, expand=True)

    # Ajouter les boutons à la fin du formulaire
    form_column.controls.append(buttons_row)

    # Conteneur principal du formulaire
    return ft.Container(
        content=ft.Column([
            ft.Container(
                content=photo_id_container,
                alignment=alignment.top_right,
                expand=True,
                margin=ft.margin.all(0),  # Pour être bien dans le coin
            ),
            ft.Row(
                [form_column], expand=True
            ),
        ]),
        padding=ft.padding.all(20),
        expand=True,
        bgcolor=colors.GREY_800,
    )

# Fonctions d'action sur les boutons
def save_data(e):
    print("Enregistrer les modifications")

def save_and_new(e):
    print("Enregistrer et ajouter un nouveau")

def save_and_continue(e):
    print("Enregistrer et continuer les modifications")

def delete_data(e):
    print("Supprimer")

# Fonction principale pour lancer l'application Flet
def main(page: ft.Page):
    page.title = "Fiche salarié(e)"
    page.scroll = "adaptive"  # Scroll activé si nécessaire
    page.window_maximized = True  # Maximiser la fenêtre automatiquement
    employee_form = build_employee_form(page)

    # Agencement principal sans la barre latérale
    page.add(employee_form)
    page.update()

# Lancer l'application Flet
ft.app(target=main)
