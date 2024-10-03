import flet as ft
#import navbar  # Assurez-vous que infoentreprise.py est dans le même répertoire

def ouvrir_page_entreprise(page: ft.Page):
    page.title = "Entreprises"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50
    page.update()
    page.window_height = 800
    page.window_width = 800
    page.window_resizable = True
    page.window_maximizable = True
    page.window_minimizable = True
    page.window_center()


    # Création de la GridView
    entreprises_grid = ft.GridView(
        expand=1,
        runs_count=5,  # Nombre de colonnes
        max_extent=200,  # Taille maximale des éléments
        child_aspect_ratio=1.0,
        spacing=10,
        run_spacing=10,
    )

    page.add(entreprises_grid)

    # Exemple de liste d'entreprises (nom et logo)
    entreprises = [
        {"nom": "Entreprise A", "logo": "https://picsum.photos/100/100?1", "id": 1},
        {"nom": "Entreprise B", "logo": "https://picsum.photos/100/100?2", "id": 2},
        {"nom": "Entreprise C", "logo": "https://picsum.photos/100/100?3", "id": 3},
        {"nom": "Entreprise D", "logo": "https://picsum.photos/100/100?4", "id": 4},
    ]

    # Fonction de redirection vers infoentreprise.py
    def afficher_navbar(e):
        entreprise_id = e.control.data["id"]
        #navbar.ouvrir_page_navbar(page, entreprise_id)

    # Ajouter les entreprises existantes dans les cadres cliquables
    for entreprise in entreprises:
        cadre = ft.Container(
            content=ft.Column(
                [
                    ft.CircleAvatar(foreground_image_src=entreprise["logo"], height=100, width=100),
                    ft.Text(entreprise["nom"], size=20, weight=ft.FontWeight.BOLD),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=10,
            border_radius=ft.border_radius.all(10),
            bgcolor=ft.colors.BLUE_GREY_900,
            on_click=afficher_navbar,  # Rendre le cadre cliquable
            data=entreprise,  # Transmettre les informations de l'entreprise
        )

        # Ajouter chaque cadre d'entreprise à la GridView
        entreprises_grid.controls.append(cadre)

    # Cadre séparé pour ajouter une nouvelle entreprise
    cadre_ajout = ft.Container(
        content=ft.Column(
            [
                ft.Icon(ft.icons.ADD_BOX, size=50, color=ft.colors.GREEN),
                ft.Text("Ajouter une entreprise", size=20, weight=ft.FontWeight.BOLD),
                ft.ElevatedButton("Ajouter", on_click=lambda e: print("Ajouter une nouvelle entreprise")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=10,
        border_radius=ft.border_radius.all(10),
        bgcolor=ft.colors.LIGHT_GREEN_900,
    )

    # Ajouter le cadre d'ajout à la GridView
    entreprises_grid.controls.append(cadre_ajout)

    page.update()


