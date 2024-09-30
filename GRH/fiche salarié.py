import flet as ft
from fcalendar import create_calendar

def build_employee_form(page):

    def on_date_selected(date, target_field):
        target_field.value = date
        page.update()

    # Initialiser les champs de date avant de les utiliser dans create_calendar
    date_naissance_field = ft.TextField(
        height=50,
        read_only=True,
        suffix=ft.IconButton(icon=ft.icons.CALENDAR_MONTH, on_click=lambda e: toggle_calendar_naissance(e)),
    )

    date_cin_field = ft.TextField(
        height=50,
        read_only=True,
        suffix=ft.IconButton(icon=ft.icons.CALENDAR_MONTH, on_click=lambda e: toggle_calendar_cin(e)),
    )

    date_duplicata_field = ft.TextField(
        height=50,
        read_only=True,
        suffix=ft.IconButton(icon=ft.icons.CALENDAR_MONTH, on_click=lambda e: toggle_calendar_duplicata(e)),
    )
    
    date_naiss_conjoint_field = ft.TextField(
        height=50,
        read_only=True,
        suffix=ft.IconButton(icon=ft.icons.CALENDAR_MONTH, on_click=lambda e: toggle_calendar_naiss_conjoint(e)),
    )
    
    # Créer les calendriers après l'initialisation des champs de date
    toggle_calendar_naissance, blur_background_naissance, calendar_container_naissance = create_calendar(page, date_naissance_field)
    toggle_calendar_cin, blur_background_cin, calendar_container_cin = create_calendar(page, date_cin_field)
    toggle_calendar_duplicata, blur_background_duplicata, calendar_container_duplicata = create_calendar(page, date_duplicata_field)
    toggle_calendar_naiss_conjoint, blur_background_naiss_conjoint, calendar_container_naiss_conjoint = create_calendar(page, date_naiss_conjoint_field)

    # Ajouter les flous d'arrière-plan des calendriers à l'overlay
    page.overlay.append(blur_background_naissance)
    page.overlay.append(blur_background_cin)
    page.overlay.append(blur_background_duplicata)
    page.overlay.append(blur_background_naiss_conjoint)
    
    conjoint_group = ft.Column([
        ft.Text("Conjoint:"),
        ft.Row([ft.Text("Nom:", width=120), ft.TextField("")]),
        ft.Row([ft.Text("Prénom:", width=120), ft.TextField("")]),
        ft.Row([ft.Text("Date de naissance:", width=120), date_naiss_conjoint_field])
    ], visible=False)

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
            def create_on_click_handler(index):
                return lambda e: toggle_calendar_naiss_enfant(index)
                
            date_naiss_enfant_field = ft.TextField(
            height=50,
            read_only=True,
            suffix=ft.IconButton(icon=ft.icons.CALENDAR_MONTH, on_click=create_on_click_handler(i))
        )
            toggle_calendar_naiss_enfant, blur_background_naiss_enfant, calendar_container_naiss_enfant = create_calendar(page, date_naiss_enfant_field)
            page.overlay.append(blur_background_naiss_enfant)
            
            radio_group = ft.RadioGroup(
            content=ft.Row([
                ft.Radio(value="Oui", label="Oui"),
                ft.Radio(value="Non", label="Non")
            ]),
            value=""  # Par défaut "Non"
        )

            enfant_group.controls.append(
                ft.Column([
                    ft.Text(f"Enfant {i + 1}: "),
                    ft.Row([ft.Text("Nom:", width=120), ft.TextField("")]),
                    ft.Row([ft.Text("Prénoms:", width=120), ft.TextField("")]),
                    ft.Row([ft.Text("Sexe:", width=120), ft.TextField("")]),
                    ft.Row([ft.Text("Date de naissance:", width=120), date_naiss_enfant_field]),
                    ft.Row([ft.Text("Enfant à charge:"), radio_group])
                ], expand=True)
            )
        enfant_group.update()
        date_naiss_enfant_field = ft.TextField(
        height=50,
        read_only=True,
        suffix=ft.IconButton(icon=ft.icons.CALENDAR_MONTH, on_click=lambda e, i=i: toggle_calendar_naiss_enfant(e)),
    )

    def on_enfant_number_change(e):
        try:
            nb_enfants = int(e.control.value)
            update_enfants(nb_enfants)
        except ValueError:
            enfant_group.controls.clear()
            enfant_group.update()

    enfant_counter_field = ft.Row([
        ft.Text("Nombre d'enfant:", width=120),
        ft.TextField(value="0", on_change=on_enfant_number_change)
    ], expand=True)

    # Champs du formulaire
    form_fields = [
        ft.Row([ft.Text("Matricule:", width=120), ft.TextField()], expand=True),
        ft.Row([ft.Text("Civilité:", width=120), ft.TextField()], expand=True),
        ft.Row([ft.Text("Nom:", width=120), ft.TextField(), ft.Text("Prénoms:", width=120), ft.TextField()], expand=True),
        ft.Row([ft.Text("Date de naissance:", width=120), date_naissance_field, ft.Text("Lieu de naissance:", width=120), ft.TextField()], expand=True),
        ft.Row([ft.Text("N°CIN:", width=120), ft.TextField(), ft.Text("Date CIN:", width=120), date_cin_field, ft.Text("Lieu CIN:"), ft.TextField()], expand=True),
        ft.Row([ft.Text("Duplicata:"), ft.Text("Date:", width=50), date_duplicata_field, ft.Text("Lieu:", width=120), ft.TextField()], expand=True),
        ft.Row([ft.Text("Adresse:", width=120), ft.TextField()], expand=True),
        ft.Row([ft.Text("E-mail:", width=120), ft.TextField()], expand=True),
        ft.Row([ft.Text("N°téléphone:", width=120), ft.TextField()], expand=True),
        ft.Row([ft.Text("Nationalité:", width=120), nationality_dropdown], expand=True),
        nationality_input,
        ft.Row([ft.Text("Situation matrimoniale:", width=120), situation_dropdown], expand=True),
        situation_input,
        conjoint_group,
        enfant_counter_field,
        enfant_group
    ]

    photo_id_container = ft.Container(
        content=ft.Image(src="1dc1f7e37b9e4991b1bb0e3400808f45.jpg", width=150, height=150),
        alignment=ft.alignment.center,
        border_radius=ft.border_radius.all(10),
        width=150,
        height=150,
        bgcolor=ft.colors.GREY_400,
        padding=ft.padding.all(10),
    )

    form_column = ft.Column(form_fields, expand=True, spacing=20)

    buttons_row = ft.Row([
        ft.ElevatedButton(text="Enregistrer", on_click=save_data, bgcolor=ft.colors.GREEN_400, color=ft.colors.WHITE),
        ft.ElevatedButton(text="Ajouter nouveau", on_click=save_and_new, bgcolor=ft.colors.BLUE_400, color=ft.colors.WHITE),
        ft.ElevatedButton(text="Continuer", on_click=save_and_continue, bgcolor=ft.colors.ORANGE_400, color=ft.colors.WHITE),
        ft.ElevatedButton(text="Supprimer", on_click=delete_data, bgcolor=ft.colors.RED_400, color=ft.colors.WHITE),
    ], alignment=ft.MainAxisAlignment.END, expand=True)

    form_column.controls.append(buttons_row)

    return ft.Container(
        content=ft.Column([
            ft.Container(
                content=photo_id_container,
                alignment=ft.alignment.top_right,
                expand=True,
                margin=ft.margin.all(0),
            ),
            ft.Row([form_column], expand=True),
        ]),
        padding=ft.padding.all(20),
        expand=True,
        bgcolor=ft.colors.GREY_800,
    )

def save_data(e):
    print("Enregistrer les modifications")

def save_and_new(e):
    print("Enregistrer et ajouter un nouveau")

def save_and_continue(e):
    print("Enregistrer et continuer les modifications")

def delete_data(e):
    print("Supprimer")


def main(page: ft.Page):
    page.title = "Fiche salarié(e)"
    page.scroll = "adaptive"
    page.window.maximized = True
    employee_form = build_employee_form(page)
    page.add(employee_form)
    page.update()

ft.app(target=main)
