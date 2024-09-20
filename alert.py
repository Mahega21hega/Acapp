import flet as ft
from datetime import datetime

# Fonction de validation de date
def validate_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False 

def main(page: ft.Page):
    page.title = "Modification d'employé"

    # Créer les éléments de l'interface
    Matricule_field = ft.TextField(label="Matricule")
    civilite_id_field = ft.TextField(label="Civilité")
    Nom_field = ft.TextField(label="Nom")
    Prénoms_field = ft.TextField(label="Prénoms")
    date_de_naiss_field = ft.TextField(label="Date de naissance", on_submit=lambda e: validate_date(e.control.value))
    lieu_de_naiss_field = ft.TextField(label="Lieu de naissance")
    N_CIN_field = ft.TextField(label="N°CIN")
    date_CIN_field = ft.TextField(label="Date CIN", on_submit=lambda e: validate_date(e.control.value))
    Lieu_CIN_field = ft.TextField(label="Lieu CIN")
    duplicata_date_field = ft.TextField(label="Date Duplicata", on_submit=lambda e: validate_date(e.control.value))
    duplicata_lieu_field = ft.TextField(label="Lieu Duplicata")
    adresse_field = ft.TextField(label="Adresse")
    E_mail_field = ft.TextField(label="E-mail")
    N_telephone_field = ft.TextField(label="N°téléphone")
    nationalite_field = ft.TextField(label="Nationalité")
    situation_matrimoniale_field = ft.TextField(label="Situation matrimoniale")

    # Groupe conjoint
    conjoint_group = ft.Column([
        ft.Text("Conjoint:"),
        ft.TextField(label="Nom Conjoint"),
        ft.TextField(label="Prénoms Conjoint"),
        ft.TextField(label="Date de naissance Conjoint", on_submit=lambda e: validate_date(e.control.value)),
    ], visible=False)  # Vous pouvez afficher ce groupe en fonction de la situation matrimoniale

    # Groupe enfant
    enfant_group = ft.Column([])

    # Bouton pour ajouter un enfant
    def add_enfant(e):
        enfant_group.controls.append(
            ft.Row([
                ft.TextField(label="Nom de l'enfant"),
                ft.TextField(label="Prénoms de l'enfant"),
                ft.TextField(label="Sexe de l'enfant"),
                ft.TextField(label="Date de naissance", on_submit=lambda e: validate_date(e.control.value)),
                ft.Checkbox(label="Enfant à charge")
            ])
        )
        enfant_group.update()

    add_enfant_button = ft.ElevatedButton("Ajouter un enfant", on_click=add_enfant)

    # Créer la colonne principale avec tous les éléments
    col = ft.Column([
        ft.Row([Matricule_field]),
        ft.Row([civilite_id_field]),
        ft.Row([Nom_field, Prénoms_field]),
        ft.Row([date_de_naiss_field, lieu_de_naiss_field]),
        ft.Row([N_CIN_field, date_CIN_field, Lieu_CIN_field]),
        ft.Row([duplicata_date_field, duplicata_lieu_field]),
        ft.Row([adresse_field]),
        ft.Row([E_mail_field]),
        ft.Row([N_telephone_field]),
        ft.Row([nationalite_field]),
        ft.Row([situation_matrimoniale_field]),
        conjoint_group,  # Afficher uniquement si nécessaire
        add_enfant_button,
        enfant_group
    ])

    # Ajouter la colonne à la page
    page.add(col)

ft.app(target=main)
