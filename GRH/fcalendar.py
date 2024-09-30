import flet as ft
from datetime import datetime, timedelta

def create_calendar(page: ft.Page, date_field: ft.TextField):
    selected_year = datetime.now().year
    selected_month = datetime.now().month
    if date_field is None:
        raise ValueError("Le champ de date n'a pas été initialisé correctement")

    # Fonction pour générer les jours du mois
    def generate_calendar(year, month):
        first_day_of_month = datetime(year, month, 1)
        start_day = first_day_of_month.weekday()  # Jour de début du mois (0 = Lundi)
        days_in_month = (first_day_of_month + timedelta(days=32)).replace(day=1) - timedelta(days=1)
        days_in_month = days_in_month.day

        calendar_days.controls.clear()

        # Ajouter des espaces vides avant le premier jour du mois
        for _ in range(start_day):
            calendar_days.controls.append(ft.Container(width=40, height=40))

        # Ajouter les jours du mois
        for day in range(1, days_in_month + 1):
            btn = ft.ElevatedButton(
                text=str(day),
                on_click=lambda e, d=day: select_date(d),  # Appeler select_date avec le jour
                width=40,
                height=40,
                style=ft.ButtonStyle(
                    shape=ft.buttons.CircleBorder(),
                    padding=ft.Padding(0, 0, 0, 0)
                )
            )
            calendar_days.controls.append(btn)

        page.update()

    # Fonction pour sélectionner une date
    def select_date(day):
        # Mettre à jour le champ texte avec la date sélectionnée
        date_field.value = f"{day}/{selected_month}/{selected_year}"
        hide_calendar()  # Masquer le calendrier après la sélection
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

    # Conteneur pour le calendrier
    calendar_container = ft.Container(
        content=ft.Column(controls=[navigation_row, calendar_days], horizontal_alignment="center"),
        visible=True,
        border=ft.border.all(1, ft.colors.BLACK),
        padding=3,
        width=290,
        height=280,
        border_radius=10,
        bgcolor=ft.colors.WHITE54,
        left=80,
        top=150
    )

    # Générer le calendrier pour le mois actuel
    generate_calendar(selected_year, selected_month)

    # Conteneur d'arrière-plan pour flouter
    blur_background = ft.Container(
        bgcolor=ft.colors.BLACK54,
        expand=True,
        visible=False
    )

    # Fonction pour afficher/masquer le calendrier
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
        if calendar_container in page.overlay:
            page.overlay.remove(calendar_container)

    # Retourne les composants du calendrier et le flou d'arrière-plan
    return toggle_calendar,blur_background, calendar_container
