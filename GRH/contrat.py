import flet as ft
from fcalendar import create_calendar

def main(page: ft.Page):
    page.bgcolor=ft.colors.GREY_900
    page.title = "Contrat"

    # Variable pour suivre l'état du mode édition
    is_editing = False
    
    def on_date_selected(date, target_field):
        target_field.value = date
        page.update()
        

    # Fonction pour afficher une boîte de dialogue
    def show_dialog(title, content):
        dlg = ft.AlertDialog(
            title=ft.Text(title),
            content=ft.Text(content),
            actions=[
                ft.Row([ft.TextButton("Oui"), ft.TextButton("Non")]),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.dialog = dlg
        dlg.open = True
        page.update()

    # Liste déroulante pour le champ Type
    type_label = ft.Text("Type:", width=120)
    type_dropdown = ft.Dropdown(
        expand=True,
        options=[
            ft.dropdown.Option("CDI"),
            ft.dropdown.Option("CDD"),
            ft.dropdown.Option("Consultant"),
        ],
        disabled=True  # Désactivé par défaut, activé en mode édition
    )

    debut_date_label = ft.Text("Date de début:", width=120)
    debut_date_field = ft.TextField(height=50,suffix=ft.IconButton(icon=ft.icons.CALENDAR_MONTH, on_click=lambda e: toggle_calendar_debutdate(e)),expand=True, disabled=True)
    fin_date_label = ft.Text("Date de fin:", width=120)
    fin_date_field = ft.TextField(height=50,suffix=ft.IconButton(icon=ft.icons.CALENDAR_MONTH, on_click=lambda e: toggle_calendar_findate(e)),expand=True, disabled=True)
    fonction_label = ft.Text("Fonction:", width=120)
    fonction_field = ft.TextField(expand=True, disabled=True)
    departe_label = ft.Text("Département:", width=120)
    departe_field = ft.TextField(expand=True, disabled=True)
    catego_label = ft.Text("Catégorie:", width=120)
    catego_field = ft.TextField(expand=True, disabled=True)
    lieutrav_label = ft.Text("Lieu de travail:", width=120)
    lieutrav_field = ft.TextField(expand=True, disabled=True)
    salaire_label = ft.Text("Salaire de base:", width=120)
    salaire_field = ft.TextField(expand=True, disabled=True)
    
    # Les champs cachés par défaut
    debut_label = ft.Text("Début:", width=50, visible=False)
    debut_field = ft.TextField(height=50,suffix=ft.IconButton(icon=ft.icons.CALENDAR_MONTH, on_click=lambda e: toggle_calendar_debut(e)),expand=True, visible=False,disabled=True)
    fin_label = ft.Text("Fin:", width=30, visible=False)
    fin_field = ft.TextField(height=50,suffix=ft.IconButton(icon=ft.icons.CALENDAR_MONTH, on_click=lambda e: toggle_calendar_fin(e)),expand=True, visible=False,disabled=True)
    decision_label = ft.Text("Décision:", width=60, visible=False)
    decision_dropdown = ft.Dropdown(
        expand=True,
        options=[
            ft.dropdown.Option("Confirmation"),
            ft.dropdown.Option("Renouvellement"),
            ft.dropdown.Option("Fin contrat"),
        ],
        visible=False,disabled=True  # Désactivé par défaut, activé en mode édition
    )

    # Les checkbox pour la période d'essai
    periessai_checkbox = ft.Checkbox(label="", disabled=True)
    
    toggle_calendar_debutdate, blur_background_debutdate, calendar_container_debutdate = create_calendar(page, debut_date_field)
    toggle_calendar_findate, blur_background_findate, calendar_container_findate = create_calendar(page, fin_date_field)
    toggle_calendar_debut, blur_background_debut, calendar_container_debut = create_calendar(page, debut_field)
    toggle_calendar_fin, blur_background_fin, calendar_container_fin = create_calendar(page, fin_field)
    
    page.overlay.append(blur_background_debutdate)
    page.overlay.append(blur_background_findate)
    page.overlay.append(blur_background_debut)
    page.overlay.append(blur_background_fin)


    # Fonction pour basculer entre l'édition et l'affichage
    def toggle_edit_mode(e):
        nonlocal is_editing
        is_editing = not is_editing  # Basculer entre mode édition et affichage

        # Activer/Désactiver la liste déroulante et les champs
        type_dropdown.disabled = not is_editing
        debut_date_field.disabled = not is_editing
        fin_date_field.disabled = not is_editing
        salaire_field.disabled = not is_editing
        periessai_checkbox.disabled = not is_editing
        lieutrav_field.disabled = not is_editing
        catego_field.disabled = not is_editing
        departe_field.disabled = not is_editing
        fonction_field.disabled = not is_editing
        debut_field.disabled = not is_editing
        fin_field.disabled = not is_editing
        decision_dropdown.disabled = not is_editing

        # Changer le texte du bouton
        edit_button.text = "Enregistrer" if is_editing else "Éditer"

        # Rafraîchir la page
        page.update()

    # Fonction pour afficher ou cacher les champs basés sur la case à cocher
    def toggle_trial_period_fields(e):
        is_checked = periessai_checkbox.value
        debut_label.visible = is_checked
        debut_field.visible = is_checked
        fin_label.visible = is_checked
        fin_field.visible = is_checked
        decision_label.visible = is_checked
        decision_dropdown.visible = is_checked
        page.update()

    # Lier la fonction à la case à cocher
    periessai_checkbox.on_change = toggle_trial_period_fields

    # Créer le bouton Éditer/Enregistrer
    edit_button = ft.ElevatedButton(text="Éditer", on_click=toggle_edit_mode)

    # Créer le bouton Historique
    history_button = ft.ElevatedButton(text="Historique")

    # Créer la colonne principale
    col = ft.Column([
        ft.Row([type_label, type_dropdown], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Row([debut_date_label, debut_date_field], alignment=ft.MainAxisAlignment.SPACE_AROUND),
        ft.Row([fin_date_label, fin_date_field], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Row([ft.Text("Période d'essai:"), periessai_checkbox]),
        ft.Row([debut_label, debut_field, fin_label, fin_field, decision_label, decision_dropdown]),
        ft.Row([fonction_label, fonction_field], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Row([departe_label, departe_field], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Row([catego_label, catego_field], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Row([lieutrav_label, lieutrav_field], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Row([salaire_label, salaire_field], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Row([edit_button], alignment=ft.MainAxisAlignment.END),  # Placer le bouton en bas à droite
    ])

    # Créer une rangée pour positionner le bouton Historique en haut à droite
    header = ft.Row(
        [
            ft.Container(),  # Espace vide à gauche pour centrer le bouton
            history_button
        ],
        alignment=ft.MainAxisAlignment.END  # Aligner le bouton à droite
    )

    # Ajouter le header et le contenu principal à la page
    page.add(header, col)

ft.app(target=main)
