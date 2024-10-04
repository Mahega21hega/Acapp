import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.GREY_900
    page.title = "C.N.A.P.S"

    # Fonction pour ajouter une nouvelle année
    def add_year(e):
        if new_year_field.value:
            year_item = ft.ListTile(
                title=ft.Text(new_year_field.value),
                leading=ft.Icon(ft.icons.CALENDAR_MONTH),
            )
            year_list.controls.append(year_item)
            new_year_field.value = ""  # Réinitialiser le champ après ajout
            page.update()

    # Années d'allocation familiale
    year_list = ft.Column(spacing=5)

    # Champ pour ajouter une nouvelle année
    new_year_field = ft.TextField(label="Nouvelle Année", width=150)
    add_year_button = ft.ElevatedButton(text="Ajouter Année", on_click=add_year)

    # Conteneur pour la liste des années
    year_section = ft.Column(
        controls=[
            ft.Text("Années:", weight="bold"),
            year_list,
            ft.Row([new_year_field, add_year_button], spacing=10),
        ],
        visible=False,  # Masquer par défaut
        spacing=10,
    )

    # Fonction pour afficher/masquer la section des années
    def toggle_year_section(e):
        year_section.visible = not year_section.visible
        page.update()

    # Fonction pour ajouter une nouvelle ligne
    def add_row(e):
        if new_info_label_field.value:
            new_row = ft.Row(
                controls=[
                    ft.Text(new_info_label_field.value + ":", width=120),
                    ft.TextField("", expand=True)  # Champ vide
                ]
            )
            info.controls.append(new_row)
            new_info_label_field.value = ""  # Réinitialiser le champ après ajout
            page.update()

    # Liste des informations
    info = ft.Column(
        controls=[
            ft.Row([ft.Text("Identifiant:", width=120), ft.TextField("", expand=True)]),
            ft.Row([ft.Text("Carte C.N.A.P.S:", width=120), ft.TextField("", expand=True)]),
            ft.Row([ft.Text("Embauche:", width=120), ft.TextField("", expand=True)]),
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.TextButton("Allocation Familiale", on_click=toggle_year_section),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10,
                ),
                padding=10,
                border_radius=10,
                bgcolor=ft.colors.GREY_900,
            ),
            year_section,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    # Champ pour ajouter une nouvelle ligne (label seulement)
    new_info_label_field = ft.TextField(label="Nom de la ligne", width=300)

    # Bouton pour soumettre la nouvelle information
    add_button = ft.ElevatedButton(text="Ajouter", on_click=add_row)

    # Agencement du formulaire pour ajouter une nouvelle ligne
    add_new_info_row = ft.Row(
        controls=[new_info_label_field, add_button],
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
    )

    # Agencement principal
    layout = ft.Column(
        controls=[
            info,  # Liste des infos statiques
            add_new_info_row,  # Formulaire pour ajouter une nouvelle ligne
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.START,
    )

    # Ajout du layout dans la page
    page.add(layout)

# Lancement de l'application Flet
ft.app(target=main)
