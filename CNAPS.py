import flet as ft

def main(page: ft.Page):
    page.title = "Fiche employé - Ajout d'années"

    # Informations statiques avec des bordures arrondies et icônes
    def create_info_row(icon, label, value):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(icon, size=24, color=ft.colors.BLUE),
                    ft.Column(
                        [
                            ft.Text(label, weight="bold", color=ft.colors.BLACK87),
                            ft.Text(value, color=ft.colors.BLACK54)
                        ],
                        spacing=2
                    )
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
            padding=10,
            border_radius=10,
            bgcolor=ft.colors.GREY_100,
        )

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
            ft.Text("Années", weight="bold"),
            year_list,
            ft.Row([new_year_field, add_year_button], spacing=10)
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
        if new_info_field.value:
            new_row = create_info_row(ft.icons.ADD, "Nouvelle info", new_info_field.value)
            info.controls.append(new_row)
            new_info_field.value = ""  # Réinitialiser le champ après ajout
            page.update()

    # Liste des informations
    info = ft.Column(
        controls=[
            create_info_row(ft.icons.BADGE, "Identifiant", "123456"),
            create_info_row(ft.icons.CARD_MEMBERSHIP, "Carte CNAPS", "987654321"),
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.icons.FAMILY_RESTROOM, size=24, color=ft.colors.BLUE),
                        ft.TextButton("Allocation Familiale", on_click=toggle_year_section)
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10,
                ),
                padding=10,
                border_radius=10,
                bgcolor=ft.colors.GREY_100,
            ),
            year_section,
            create_info_row(ft.icons.WORK, "Embauche", "01/01/2020"),
            
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )
    
    # Champ pour ajouter une nouvelle ligne
    new_info_field = ft.TextField(label="Nouvelle Information", width=300)
    
    # Bouton pour soumettre la nouvelle information
    add_button = ft.ElevatedButton(text="Ajouter", on_click=add_row)
    
    # Agencement du formulaire pour ajouter une nouvelle ligne
    add_new_info_row = ft.Row(
        controls=[new_info_field, add_button],
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
    )


    # Agencement principal
    layout = ft.Column(
        controls=[
            info,  # Liste des infos statiques
            add_new_info_row,  # Liste des années et bouton pour ajouter une nouvelle année  # Formulaire pour ajouter une nouvelle ligne
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.START,
    )

    # Ajout du layout dans la page
    page.add(layout)

# Lancement de l'application Flet
ft.app(target=main)
