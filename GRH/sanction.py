import flet as ft

def main(page: ft.Page):
    page.title = "Trimestres de l'année"
    
    # Fonction pour créer un tableau déroulant avec DataTable
    def create_dropdown_table(rows):
        return ft.DataTable(
            columns=[
                ft.DataColumn(label=ft.Text("Evenement")),
                ft.DataColumn(label=ft.Text("Type")),
                ft.DataColumn(label=ft.Text("Date")),
                ft.DataColumn(label=ft.Text("Suivi")),
                ft.DataColumn(label=ft.Text("Pièce jointe")),
            ],
            rows=rows,
            expand=True,
            width=2000,
            border=ft.Border(
                left=ft.BorderSide(1, ft.colors.BLACK),
                right=ft.BorderSide(1, ft.colors.BLACK),
                bottom=ft.BorderSide(1, ft.colors.BLACK),
            )
        )
    
    # Correct initialization of Ref without arguments
    show_trimestres = ft.Ref()  # This will later hold a bool value
    trimestres_list = ft.Ref()  # This will later hold a Column
    container_ref = ft.Ref()  # Reference to the container
    
    # Fonction qui bascule la visibilité des trimestres et ajuste la hauteur
    def toggle_trimestres(e):
        if show_trimestres.current is None:
            show_trimestres.current = False
        show_trimestres.current = not show_trimestres.current
        trimestres_list.current.visible = show_trimestres.current
        
        # Ajuster la hauteur en fonction de la visibilité
        if show_trimestres.current:
            container_ref.current.height = 350  # Hauteur plus grande pour montrer la liste
        else:
            container_ref.current.height = 80  # Hauteur plus petite par défaut
        
        page.update()

    # Création des lignes du tableau
    rows = [
        ft.DataRow(cells=[
            ft.DataCell(ft.Text("Événement 1")),
            ft.DataCell(ft.Text("Type A")),
            ft.DataCell(ft.Text("01/01/2024")),
            ft.DataCell(ft.Text("Suivi 1")),
            ft.DataCell(ft.Text("Pièce jointe 1")),
        ]),
        ft.DataRow(cells=[
            ft.DataCell(ft.Text("Événement 2")),
            ft.DataCell(ft.Text("Type B")),
            ft.DataCell(ft.Text("02/02/2024")),
            ft.DataCell(ft.Text("Suivi 2")),
            ft.DataCell(ft.Text("Pièce jointe 2")),
        ])
    ]

    # Conteneur principal avec padding
    container = ft.Container(
        content=ft.Column(
            [
                # GestureDetector wrapping the Row to handle click events
                ft.GestureDetector(
                    content=ft.Row(
                        [
                            ft.Text("ANNÉE", size=20),
                            ft.Text("2024", size=20),
                        ],
                        alignment="spaceBetween"
                    ),
                    on_tap=toggle_trimestres  # Click event to toggle table visibility
                ),
                ft.Divider(height=10),  # Ligne de séparation
                ft.Column(
                    [
                        create_dropdown_table(rows)
                    ],
                    spacing=5,
                    ref=trimestres_list,  # Référence à la liste des trimestres
                    visible=False  # Cacher les trimestres au début
                )
            ],
            spacing=5,  # Espacement entre les items
        ),
        padding=20,  # Espacement intérieur du cadre
        border_radius=10,  # Arrondir les coins
        border=ft.border.all(1, "black"),  # Bordure noire
        height=80,  # Hauteur par défaut réduite
        width=1000,
        ref=container_ref,  # Référence du conteneur
    )
    
    page.add(container)

ft.app(target=main)
