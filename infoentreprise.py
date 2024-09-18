import flet as ft

def ouvrir_page_info_entreprise(page: ft.Page, entreprise_id):
    page.title = f"Informations de l'entreprise {entreprise_id}"
    page.clean()  # Nettoyer la page pour charger une nouvelle vue
    
    def on_change(e):
        selected_index = e.control.selected_index
        print("Selected destination:", selected_index)
        if selected_index == 1:  # Afficher la nav bar si "Second" est sélectionné
            if nav_bar not in page.controls:
                page.controls.insert(1, nav_bar)  # Ajouter la nav bar au début de la page
        else:
            if nav_bar in page.controls:
                page.controls.remove(nav_bar)  # Retirer la nav bar si une autre option est sélectionnée
        page.update()
    
    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.PERSON, label="Fiche"),
            ft.NavigationBarDestination(icon=ft.icons.FILE_COPY_SHARP, label="Contrat"),
            ft.NavigationBarDestination(icon=ft.icons.BOOKMARK, label="C.N.A.P.S"),
            ft.NavigationBarDestination(icon=ft.icons.BOOKMARK, label="O.S.I.E"),
            ft.NavigationBarDestination(icon=ft.icons.OTHER_HOUSES_ROUNDED, label="Autre")
        ]
    )

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="Fiche Client"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.BOOKMARK_BORDER, selected_icon=ft.icons.BOOKMARK, label="G.R.H"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED, selected_icon=ft.icons.SETTINGS, label="Paye"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED, selected_icon=ft.icons.SETTINGS, label="Déclaration"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED, selected_icon=ft.icons.SETTINGS, label="Option audit"
            ),
        ],
        on_change=on_change,
    )

    page.add(
        ft.Row(
            [
                rail,
                ft.Column([ ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    )
    
    page.update()

