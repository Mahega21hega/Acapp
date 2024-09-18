import flet as ft

# Fonction pour désactiver/activer l'édition de la fiche
def toggle_edit_mode(e, text_fields, checkboxes):
    editable = e.control.data
    e.control.data = not editable
    
    for field in text_fields:
        field.disabled = not editable
    for checkbox in checkboxes:
        checkbox.disabled = not editable
    e.control.text = "Enregistrer" if editable else  "Éditer"
    
    e.page.update()

def main(page: ft.Page):
    page.title = "Fiche de contrat"
    
    # Informations de l'employé (désactivées par défaut)
    Type_field = ft.TextField(label="Type", value="John Doe", disabled=True)
    Date_de_début_field = ft.TextField(label="Date de début", value="Développeur", disabled=True)
    Date_de_fin_field = ft.TextField(label="Date de fin", value="Informatique", disabled=True)
    Salaire_field = ft.TextField(label="Salaire", value="salaire", disabled=True)
    Lieu_de_travail_field = ft.TextField(label="Lieu de travail", value="Lieu", disabled=True)
    
    # Ligne pour période d'essai avec trois cases à cocher (désactivées par défaut)
    periode_essaie_label = ft.Text("Période d'essai :")
    checkbox_1_mois = ft.Checkbox(label="Confirmation", disabled=True)
    checkbox_2_mois = ft.Checkbox(label="Renouvellement", disabled=True)
    checkbox_3_mois = ft.Checkbox(label="Fin contrat", disabled=True)
    
    # Groupe de cases à cocher
    checkbox_row = ft.Row(
        controls=[checkbox_1_mois, checkbox_2_mois, checkbox_3_mois],
        spacing=10
    )
    
    # Disposition principale de la fiche
    fiche_layout = ft.Column(
        controls=[
            Type_field,
            Date_de_début_field,
            Date_de_fin_field,
            Salaire_field,
            Lieu_de_travail_field,
            periode_essaie_label,
            checkbox_row
        ],
        spacing=20,
    )

    # Bouton flottant "Historique" en haut à droite
    historique_button = ft.FloatingActionButton(
        icon=ft.icons.HISTORY,
        tooltip="Voir historique",
        on_click=lambda e: print("Historique cliqué")
    )

    # Bouton flottant "Éditer" en bas à droite (désactivé par défaut)
    editer_button = ft.FloatingActionButton(
        icon=ft.icons.EDIT,
        text="Éditer",
        tooltip="Modifier la fiche",
        data=False,  # False signifie que la fiche est en mode lecture
        on_click=lambda e: toggle_edit_mode(e, [Type_field,Date_de_début_field,Date_de_fin_field,Salaire_field,Lieu_de_travail_field], [checkbox_1_mois, checkbox_2_mois, checkbox_3_mois])
    )

    # Layout avec les deux boutons flottants
    page.add(
        ft.Stack(
            [
                fiche_layout,
                ft.Container(
                    content=editer_button,
                    alignment=ft.alignment.bottom_right,
                ),
                ft.Container(
                    content=historique_button,
                    alignment=ft.alignment.top_right,
                ),
            ],
        )
    )

# Lancement de l'application Flet
ft.app(target=main)
