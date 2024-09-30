import flet as ft
from datetime import datetime, timedelta

def main(page: ft.Page):
    page.title = "Fiche Client - Informations Entreprise"
    
    # Variables pour l'année et le mois sélectionnés
    selected_year = datetime.now().year
    selected_month = datetime.now().month

    # Champ de texte pour afficher la date sélectionnée
    siren_field = ft.TextField(
        label="Date de création",
        read_only=True,  # Ce champ sera rempli par le calendrier
        width=300,
        suffix=ft.IconButton(
            icon=ft.icons.CALENDAR_MONTH,  # Icône de calendrier dans le champ
            on_click=lambda e: toggle_calendar(e)  # Ouvre le calendrier quand on clique dessus
        )
    )

    # Fonction pour générer les jours du mois
    def generate_calendar(year, month):
        first_day_of_month = datetime(year, month, 1)
        start_day = first_day_of_month.weekday()
        days_in_month = (first_day_of_month + timedelta(days=32)).replace(day=1) - timedelta(days=1)
        days_in_month = days_in_month.day

        calendar_days.controls.clear()

        # Ajouter des espaces vides avant le premier jour
        for _ in range(start_day):
            calendar_days.controls.append(ft.Container(width=40, height=40))

        # Ajouter les jours du mois
        for day in range(1, days_in_month + 1):
            btn = ft.ElevatedButton(
                text=str(day), 
                on_click=lambda e, d=day: select_date(d),
                width=40,  # Largeur des boutons
                height=40,  # Hauteur des boutons
                style=ft.ButtonStyle(
                    shape=ft.buttons.CircleBorder(),
                    padding=ft.Padding(0, 0, 0, 0)  # Spécification des quatre côtés (gauche, haut, droite, bas)
                )
            )

            calendar_days.controls.append(btn)

        page.update()

    # Fonction pour sélectionner une date
    def select_date(day):
        siren_field.value = f"{day}/{selected_month}/{selected_year}"
        # Cacher le calendrier après sélection
        hide_calendar()
        page.update()

    # Fonction pour changer de mois
    def change_month(e, increment):
        nonlocal selected_month, selected_year
        selected_month += increment
        if selected_month > 12:
            selected_month = 1
            selected_year += 1
        elif selected_month < 1:
            selected_month = 12
            selected_year -= 1
        # Mettre à jour le calendrier
        month_label.value = f"{datetime(selected_year, selected_month, 1).strftime('%B %Y')}"
        generate_calendar(selected_year, selected_month)

    # Boutons pour changer de mois
    prev_month_button = ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda e: change_month(e, -1))
    next_month_button = ft.IconButton(icon=ft.icons.ARROW_FORWARD, on_click=lambda e: change_month(e, 1))

    # Label pour afficher le mois et l'année courants
    month_label = ft.Text(value=f"{datetime(selected_year, selected_month, 1).strftime('%B %Y')}", size=25)

    # Ligne de navigation (mois précédent, mois suivant)
    navigation_row = ft.Row(controls=[prev_month_button, month_label, next_month_button], alignment="center")

    # Grille pour afficher les jours du mois
    calendar_days = ft.GridView(expand=True, runs_count=7, max_extent=40, spacing=2)

    # Conteneur pour le calendrier (sera caché par défaut) avec bordures
    calendar_container = ft.Container(
        content=ft.Column(controls=[navigation_row, calendar_days], horizontal_alignment="center"),
        visible=True,  # Défini sur "visible" pour qu'il apparaisse dans l'overlay
        border=ft.border.all(1, ft.colors.BLACK),  # Bordure noire de 1px
        padding=3,  # Espacement interne
        width=290,  # Largeur fixe du calendrier
        height=280,  # Hauteur fixe du calendrier
        border_radius=10,
        bgcolor=ft.colors.WHITE54,  # Couleur de fond du calendrier
        # Ajout d'une position absolue pour placer le calendrier sous l'icône
        left=80,  # Ajustez la valeur pour correspondre à la position de l'icône
        top=150  # Ajustez la valeur pour placer sous l'icône du calendrier
    )

    # Générer le calendrier pour le mois actuel
    generate_calendar(selected_year, selected_month)

    # Conteneur d'arrière-plan pour simuler un flou (opacité réduite)
    blur_background = ft.Container(
        bgcolor=ft.colors.BLACK54,  # Couleur noire semi-transparente
        expand=True,  # Prend toute la place
        visible=False  # Caché par défaut
    )

    # Fonction pour afficher/masquer le calendrier avec l'arrière-plan flou
    def toggle_calendar(e):
        if blur_background.visible:
            hide_calendar()
        else:
            show_calendar()
        page.update()

    def show_calendar():
        blur_background.visible = True
        page.overlay.append(calendar_container)

    def hide_calendar():
        blur_background.visible = False
        page.overlay.clear()

    # Logo de l'entreprise
    logo = ft.Image(src="path_to_logo.jpg", width=150, height=150, fit=ft.ImageFit.COVER)
    
    # Informations générales sur l'entreprise
    nom_entreprise_field = ft.TextField(label="Nom de l'entreprise", hint_text="Nom de l'entreprise", width=400)
    adresse_field = ft.TextField(label="Adresse", hint_text="Adresse complète", width=400)
    email_field = ft.TextField(label="Email", hint_text="Email de l'entreprise", width=400)
    phone_field = ft.TextField(label="Téléphone", hint_text="Numéro de téléphone", width=300)
    
    # Informations supplémentaires
    site_web_field = ft.TextField(label="Site Web", hint_text="Site web de l'entreprise", width=400)
    secteur_activite_field = ft.TextField(label="Secteur d'activité", hint_text="Ex: Technologie, Commerce", width=400)
    
    # Bouton pour ajouter l'entreprise
    btn_add = ft.ElevatedButton(text="Ajouter l'entreprise", on_click=lambda e: add_entreprise())

    def add_entreprise():
        # Fonction pour ajouter l'entreprise (à compléter selon votre logique)
        print(f"Ajout de l'entreprise: {nom_entreprise_field.value}, Date de création: {siren_field.value}")

    # Disposition des champs
    page.add(
        ft.Column(controls=[
            ft.Row([logo]),
            ft.Row([nom_entreprise_field]),
            ft.Row([siren_field]),  # Remplacement du SIREN par le champ de date avec le bouton calendrier à l'intérieur
            ft.Row([adresse_field]),
            ft.Row([email_field, phone_field]),
            ft.Row([site_web_field, secteur_activite_field]),
            ft.Row([btn_add])
        ], spacing=10)  # Espacement entre les éléments
    )

    # Ajouter le conteneur de flou à l'overlay
    page.overlay.append(blur_background)

# Exécuter l'application
ft.app(target=main)
