import flet as ft
from _pydatetime import date

def main(page: ft.Page):

    def open_calendar(e):
        def on_date_selected(e):
            date_field.value = str(e.control.value)
            page.update()

        # Créer un DatePicker
        date_picker = ft.DatePicker(
            on_submit=on_date_selected,
            initial_date=date.today(),
            first_date=date(1900, 1, 1),
            last_date=date(2100, 12, 31)
        )

        # Ouvrir le DatePicker
        date_picker.open()

    # Créer le TextField avec une icône de calendrier
    date_field = ft.TextField(
        label="Choisissez une date",
        suffix_icon=ft.icons.CALENDAR_MONTH,
        on_suffix_icon_click=open_calendar
    )

    # Ajouter le TextField à la page
    page.add(date_field)

# Lancer l'application Flet
ft.app(target=main)
