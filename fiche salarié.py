import flet as ft
from datetime import datetime
from flet import (
    UserControl,
    Column,
    Container,
    Row,
    Text,
    TextButton,
    TextField,
    DatePicker,
    border_radius,
    colors,
    padding,
    margin,
)

# Fonction de validation de date
def validate_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Classe pour la barre latérale
class Sidebar(UserControl):
    def __init__(self, app_layout, page):
        super().__init__()
        self.app_layout = app_layout
        self.page = page

    def build(self):
        self.view = Container(
            content=Column([
                Row([Text("Workspace", size=20, color=colors.WHITE)]),
                Container(
                    bgcolor=colors.BLACK26,
                    border_radius=border_radius.all(30),
                    height=1,
                    width=220
                ),
                TextButton(
                    text="Boards",
                    on_click=lambda e: self.navigate_to("Boards"),
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,
                        padding=padding.all(10),
                    ),
                ),
                TextButton(
                    text="Members",
                    on_click=lambda e: self.navigate_to("Members"),
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,
                        padding=padding.all(10),
                    ),
                ),
                Container(
                    bgcolor=colors.BLACK26,
                    border_radius=border_radius.all(30),
                    height=1,
                    width=220
                ),
            ], tight=True),
            padding=padding.all(15),
            margin=margin.all(0),
            width=250,
            height=1000,
            bgcolor=colors.GREY_600,
        )
        return self.view

    def navigate_to(self, destination):
        self.page.controls[1].content = Text(f"You are viewing {destination}")
        self.page.update()

# Formulaire principal de modification d'employé
def build_employee_form(page):
    # Création du groupe pour le conjoint
    conjoint_group = ft.Column([
        ft.Text("Conjoint:"),
        ft.TextField(label="Nom"),
        ft.TextField(label="Prénoms"),
        DatePicker()
    ], visible=False)

    # Fonction pour créer des lignes avec étiquettes et TextFields alignés
    def create_labeled_row(label, on_submit=None):
        return Row([
            Text(label, width=150),
            TextField(on_submit=on_submit)
        ], expand=True)

    # Création des lignes pour le formulaire
    Matricule_row = create_labeled_row("Matricule:")
    civilite_row = create_labeled_row("Civilité:")
    Nom_row = Row([
        Text("Nom:", width=150),
        TextField(),
        Text("Prénoms:", width=100),
        TextField()
    ], expand=True)

    date_de_naiss_row = Row([
        Text("Date de naissance:", width=150),
        DatePicker(),
        Text("Lieu de naissance:", width=150),
        TextField()
    ], expand=True)

    # Séparation de N°CIN, Date CIN et Lieu CIN
    N_CIN_row = Column([
        Row([Text("N°CIN:", width=150), TextField()]),
        Row([Text("Date CIN:", width=150), DatePicker()]),
        Row([Text("Lieu CIN:", width=150), TextField()])
    ])

    duplicata_date_row = Row([
        Text("Duplicata:", width=150),
        Text("Date:", width=100),
        DatePicker(),
        Text("Lieu:", width=100),
        TextField()
    ], expand=True)

    adresse_row = create_labeled_row("Adresse:")
    E_mail_row = create_labeled_row("E-mail:")
    N_telephone_row = create_labeled_row("N°téléphone:")

    # Fonctionnalités de nationalité et situation matrimoniale
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

    nationality_row = Row([
        Text("Nationalité:", width=150),
        nationality_dropdown
    ], expand=True)

    nationality_input = TextField(
        label="Saisir une autre nationalité",
        visible=False,
        on_submit=add_new_nationality
    )

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

    situation_matrimoniale_row = Row([
        Text("Situation matrimoniale:", width=150),
        situation_dropdown
    ], expand=True)

    situation_input = TextField(
        label="Saisir une autre situation matrimoniale",
        visible=False,
        on_submit=add_new_situation
    )

    # Groupe enfant
    enfant_group = ft.Column([])

    def update_enfants(nb_enfants):
        enfant_group.controls.clear()
        for i in range(nb_enfants):
            enfant_group.controls.append(
                Column([
                    Text(f"Enfant {i + 1}: "),
                    TextField(label="Nom de l'enfant"),
                    TextField(label="Prénoms de l'enfant"),
                    TextField(label="Sexe de l'enfant"),
                    DatePicker(),
                    ft.Checkbox(label="Enfant à charge")
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

    enfant_counter_field = Row([Text("Nombre d'enfant"), TextField(value="0", on_change=on_enfant_number_change)], expand=True)

    photo_id_container = Container(
        content=ft.Image(src="1dc1f7e37b9e4991b1bb0e3400808f45.jpg", width=150, height=150),
        alignment=ft.alignment.center,
        border_radius=border_radius.all(10),
        width=150,
        height=150,
        bgcolor=colors.GREY_400,
        padding=padding.all(10),
    )

    col = Column([
        Matricule_row,
        civilite_row,
        Nom_row,
        date_de_naiss_row,
        N_CIN_row,
        duplicata_date_row,
        adresse_row,
        E_mail_row,
        N_telephone_row,
        nationality_row,
        nationality_input,
        situation_matrimoniale_row,
        situation_input,
        conjoint_group,
        enfant_counter_field,
        enfant_group
    ], expand=True)

    buttons_row = Row([
        ft.ElevatedButton(text="Enregistrer", on_click=save_data),
        ft.ElevatedButton(text="Enregistrer et ajouter un nouveau", on_click=save_and_new),
        ft.ElevatedButton(text="Enregistrer et continuer", on_click=save_and_continue),
        ft.ElevatedButton(text="Supprimer", on_click=delete_data),
    ], alignment=ft.MainAxisAlignment.END, expand=True)

    col.controls.append(buttons_row)

    return Container(
        content=Row([
            col,
            Container(
                content=photo_id_container,
                alignment=ft.alignment.top_right,
            )
        ], expand=True),
        width=1000,
        height=1000,
        bgcolor=ft.colors.GREY_800,
        padding=ft.padding.all(10),
    )

def save_data(e):
    print("Data saved")

def save_and_new(e):
    print("Data saved and new")

def save_and_continue(e):
    print("Data saved and continue")

def delete_data(e):
    print("Data deleted")

def main(page):
    page.title = "Employee Form"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.controls.append(
        ft.Row([
            Sidebar(None, page),
            build_employee_form(page)
        ], expand=True)
    )
    page.update()

ft.app(target=main)