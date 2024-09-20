import flet as ft

def main(page):
    # Fonction appelée lorsque la date est sélectionnée
    def on_date_select(e):
        date_field.value = e.control.value  # Met à jour le TextField avec la date sélectionnée
        page.update()  # Rafraîchit la page pour afficher la date

    # TextField avec une icône de calendrier qui ouvre un DatePicker
    date_field = ft.TextField(
        label="Sélectionne une date",
        suffix=ft.Icon(ft.icons.CALENDAR_MONTH),  # Icône du calendrier
        read_only=True  # Empêche la saisie manuelle dans le champ
    )

    # Définir le DatePicker
    date_picker = ft.DatePicker(
        on_change=on_date_select  # Appelé lorsque la date est sélectionnée
    )

    # Conteneur pour ouvrir le DatePicker lorsque l'utilisateur clique sur le champ texte
    def open_calendar(e):
        date_picker.show()

    # Rendre le TextField cliquable pour ouvrir le calendrier
    date_field.on_click = open_calendar

    # Ajoute les contrôles à la page
    page.add(date_field, date_picker)

ft.app(target=main)
