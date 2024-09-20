import flet as ft
from datetime import datetime
from flet import (
    UserControl,
    Column,
    Container,
    Row,
    Text,
    TextButton,
    alignment,
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
        # Contenu principal de la barre latérale avec des boutons texte cliquables
        self.view = Container(
            content=Column([
                Row([Text("Workspace", size=20, color=colors.WHITE)]),
                # Séparateur
                Container(
                    bgcolor=colors.BLACK26,
                    border_radius=border_radius.all(30),
                    height=1,
                    alignment=alignment.center_right,
                    width=220
                ),
                # TextButton pour "Boards"
                TextButton(
                    text="Boards",
                    on_click=lambda e: self.navigate_to("Boards"),
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,  # Couleur du texte
                        padding=padding.all(10),
                    ),
                ),
                TextButton(
                    text="Members",
                    on_click=lambda e: self.navigate_to("Members"),
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,  # Couleur du texte
                        padding=padding.all(10),
                    ),
                ),
                # Séparateur
                Container(
                    bgcolor=colors.BLACK26,
                    border_radius=border_radius.all(30),
                    height=1,
                    alignment=alignment.center_right,
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
        # Fonction qui gère la navigation lorsque l'on clique sur un TextButton
        self.page.controls[1].content = Text(f"You are viewing {destination}")
        self.page.update()


# Formulaire principal de modification d'employé
def build_employee_form(page):
    # Création du groupe pour le conjoint
    conjoint_group = ft.Column([
        ft.Text("Conjoint:"),
        ft.TextField(label="Nom"),
        ft.TextField(label="Prénoms"),
        ft.TextField(label="Date de naissance", on_submit=lambda e: validate_date(e.control.value))
    ], visible=False)

    # Fonction pour afficher ou cacher le groupe conjoint
    
    # Créer les éléments de l'interface avec les labels à côté des TextField
    Matricule_row = ft.Row([ft.Text("Matricule:"), ft.TextField()], expand=True)
    civilite_row = ft.Row([ft.Text("Civilité:"), ft.TextField()], expand=True)
    Nom_row = ft.Row([ft.Text("Nom:"), ft.TextField(), ft.Text("Prénoms:"), ft.TextField()], expand=True)
    date_de_naiss_row = ft.Row([ft.Text("Date de naissance:"), ft.TextField(on_submit=lambda e: validate_date(e.control.value)), ft.Text("Lieu de naissance:"), ft.TextField()], expand=True)
    N_CIN_row = ft.Row([ft.Text("N°CIN:"), ft.TextField(), ft.Text("Date CIN:"), ft.TextField(on_submit=lambda e: validate_date(e.control.value)), ft.Text("Lieu CIN:"), ft.TextField()], expand=True)
    duplicata_date_row = ft.Row([ft.Text("Duplicata:"), ft.Text("Date:"), ft.TextField(on_submit=lambda e: validate_date(e.control.value)), ft.Text("Lieu:"), ft.TextField()], expand=True)
    adresse_row = ft.Row([ft.Text("Adresse:"), ft.TextField()], expand=True)
    E_mail_row = ft.Row([ft.Text("E-mail:"), ft.TextField()], expand=True)
    N_telephone_row = ft.Row([ft.Text("N°téléphone:"), ft.TextField()], expand=True)
    
    def on_nationality_change(e):
        if e.control.value == "Autre":
            nationality_input.visible = True
        else:
            nationality_input.visible = False
        page.update()
        
    def add_new_nationality(e):
        new_nationality = nationality_input.value
        if new_nationality:  # Si une nouvelle valeur est saisie
            nationality_dropdown.options.append(ft.dropdown.Option(new_nationality))  # Ajouter à la liste déroulante
            nationality_dropdown.value = new_nationality  # Sélectionner la nouvelle valeur
            nationality_input.value = ""  # Réinitialiser le champ de saisie
            nationality_input.visible = False  # Masquer le champ après l'ajout
        page.update()    
    
    nationality_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Malgache"),
            ft.dropdown.Option("Français(e)"),
            ft.dropdown.Option("Anglais(e)"),
            ft.dropdown.Option("Autre")  # Option pour ajouter une nationalité personnalisée
        ],
        on_change=on_nationality_change
    )

    nationality_row = ft.Row([
        ft.Text("Nationalité:"),
        nationality_dropdown
    ], expand=True)

    # TextField pour saisir une nationalité personnalisée
    nationality_input = ft.TextField(
        label="Saisir une autre nationalité",
        visible=False,
        on_submit=add_new_nationality  # Ajout dynamique
    )

    def on_situation_change(e):
        conjoint_group.visible = e.control.value == "Marié(e)"
        if e.control.value == "Autre":
            situation_input.visible = True
        else:
            situation_input.visible = False
        page.update()
    
    # Fonction pour ajouter une nouvelle valeur dans la liste déroulante de situation matrimoniale
    def add_new_situation(e):
        new_situation = situation_input.value
        if new_situation:  # Si une nouvelle valeur est saisie
            situation_dropdown.options.append(ft.dropdown.Option(new_situation))  # Ajouter à la liste déroulante
            situation_dropdown.value = new_situation  # Sélectionner la nouvelle valeur
            situation_input.value = ""  # Réinitialiser le champ de saisie
            situation_input.visible = False  # Masquer le champ après l'ajout
        page.update()


    situation_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Marié(e)"),
            ft.dropdown.Option("Célibataire"),
            ft.dropdown.Option("Autre")  # Option pour ajouter une situation matrimoniale personnalisée
        ],
        on_change=on_situation_change
    )

    situation_matrimoniale_row = ft.Row([
        ft.Text("Situation matrimoniale:"),
        situation_dropdown
    ], expand=True)

    # TextField pour saisir une situation matrimoniale personnalisée
    situation_input = ft.TextField(
        label="Saisir une autre situation matrimoniale",
        visible=False,
        on_submit=add_new_situation  # Ajout dynamique
    )

    # Groupe enfant
    enfant_group = ft.Column([])

    # Fonction pour mettre à jour le nombre d'enfants
    def update_enfants(nb_enfants):
        enfant_group.controls.clear()
        for i in range(nb_enfants):
            enfant_group.controls.append(
                ft.Column([
                    ft.Text(f"Enfant {i + 1}: "),
                    ft.TextField(label="Nom de l'enfant"),
                    ft.TextField(label="Prénoms de l'enfant"),
                    ft.TextField(label="Sexe de l'enfant"),
                    ft.TextField(label="Date de naissance", on_submit=lambda e: validate_date(e.control.value)),
                    ft.Checkbox(label="Enfant à charge")
                ], expand=True)
            )
        enfant_group.update()

    # TextField pour saisir le nombre d'enfants
    def on_enfant_number_change(e):
        try:
            nb_enfants = int(e.control.value)
            update_enfants(nb_enfants)
        except ValueError:
            enfant_group.controls.clear()  # Vider si la saisie n'est pas valide
            enfant_group.update()

    enfant_counter_field = ft.Row([ft.Text("Nombre d'enfant"), ft.TextField(value="0", on_change=on_enfant_number_change)], expand=True)

    # Cadre pour la photo d'identité
    photo_id_container = ft.Container(
        content=ft.Image(src="1dc1f7e37b9e4991b1bb0e3400808f45.jpg", width=150, height=150),
        alignment=alignment.center,
        border_radius=border_radius.all(10),
        width=150,
        height=150,
        bgcolor=colors.GREY_400,
        padding=padding.all(10),
    )

    # Créer la colonne principale avec tous les éléments
    col = ft.Column([
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
        conjoint_group,  # Afficher uniquement si nécessaire
        enfant_counter_field,  # TextField pour saisir le nombre d'enfants
        enfant_group
    ], expand=True)

    # Boutons d'action intégrés dans le formulaire
    buttons_row = ft.Row([
        ft.ElevatedButton(text="Enregistrer", on_click=save_data),
        ft.ElevatedButton(text="Enregistrer et ajouter un nouveau", on_click=save_and_new),
        ft.ElevatedButton(text="Enregistrer et continuer", on_click=save_and_continue),
        ft.ElevatedButton(text="Supprimer", on_click=delete_data),
    ], alignment=ft.MainAxisAlignment.END, expand=True)

    # Ajouter les boutons au conteneur principal
    col.controls.append(buttons_row)

    # Ajouter un Container avec un défilement et cadre de photo
    return ft.Container(
        content=ft.Row([
            col,  # Formulaire
            ft.Container(  # Cadre pour la photo
                content=photo_id_container,
                alignment=alignment.top_right,
            )
        ], expand=True),
        width=1000,  # Largeur fixe du container
        height=1000,
        bgcolor=ft.colors.GREY_800,  # Hauteur fixe avec scrollbar
        padding=ft.padding.all(10),
    )


def save_data(e):
    print("Enregistrer les modifications")


def save_and_new(e):
    print("Enregistrer et ajouter un nouveau")


def save_and_continue(e):
    print("Enregistrer et continuer les modifications")


def delete_data(e):
    print("Supprimer")


# Fonction principale qui crée l'application
def main(page: ft.Page):
    sidebar = Sidebar(None, page)
    page.scroll = "always"
    page.title = "Fiche salarié(e)"

    # Formulaire principal
    employee_form = build_employee_form(page)

    # Agencement principal avec la barre latérale et le contenu principal
    layout = Row(
        controls=[
            sidebar.build(),
            Container(content=employee_form, expand=True),
        ],
        expand=True,
    )

    page.add(layout)
    page.update()

# Lancer l'application Flet
ft.app(target=main)

