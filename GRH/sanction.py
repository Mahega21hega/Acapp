import flet as ft
from datetime import datetime

def main(page: ft.Page):
    # Liste des éléments avec leurs dates de création
    items = [
        {"name": "Élément 1", "date": datetime(2024, 9, 25)},
        {"name": "Élément 2", "date": datetime(2024, 9, 24)},
        {"name": "Élément 3", "date": datetime(2024, 9, 23)},
        {"name": "Élément 4", "date": datetime(2024, 9, 22)},
    ]

    # Fonction pour créer un tableau déroulant avec DataTable
    def create_dropdown_table(rows):
        return ft.DataTable(
            columns=[
                ft.DataColumn(label=ft.Text("Colonne 1 (Éditable)")),
                ft.DataColumn(label=ft.Text("Colonne 2")),
                ft.DataColumn(label=ft.Text("Colonne 3")),
                ft.DataColumn(label=ft.Text("Colonne 4")),
                ft.DataColumn(label=ft.Text("Colonne 5")),
            ],
            rows=rows,
            border=ft.Border(
                left=ft.BorderSide(1, ft.colors.BLACK),
                right=ft.BorderSide(1, ft.colors.BLACK),
                bottom=ft.BorderSide(1, ft.colors.BLACK),
            ),
            divider_thickness=1,  # Épaisseur du diviseur entre les colonnes
            show_checkbox_column=False  # Désactiver les cases à cocher par défaut
        )

    # Fonction pour gérer le clic sur une ligne
    def on_row_click(e, container, table_container, bouton_ajout):
        table_container.visible = not table_container.visible
        bouton_ajout.visible = table_container.visible
        table_container.update()  # Mise à jour du conteneur pour refléter la visibilité
        bouton_ajout.update()  # Mise à jour du bouton "Ajouter une ligne"
        container.update()  # Mise à jour du conteneur principal

    # Fonction pour ajouter une nouvelle ligne au tableau
    def add_row(table_container, rows):
        new_row = ft.DataRow(cells=[
            ft.DataCell(ft.TextField(value="Nouvelle Valeur 1", width=100)),  # Cellule éditable
            ft.DataCell(ft.Text("Nouvelle Valeur 2")),
            ft.DataCell(ft.Text("Nouvelle Valeur 3")),
            ft.DataCell(ft.Text("Nouvelle Valeur 4")),
            ft.DataCell(ft.Text("Nouvelle Valeur 5")),
        ])
        rows.append(new_row)
        table_container.content = create_dropdown_table(rows)
        table_container.update()

    # Créer la colonne principale
    liste_elements = ft.Column()

    # Ajouter chaque élément avec gestion de l'affichage du tableau déroulant
    for item in items:
        rows = [
            ft.DataRow(cells=[
                ft.DataCell(ft.TextField(value="Valeur 1", width=100)),  # Cellule éditable
                ft.DataCell(ft.Text("Valeur 2")),
                ft.DataCell(ft.Text("Valeur 3")),
                ft.DataCell(ft.Text("Valeur 4")),
                ft.DataCell(ft.Text("Valeur 5")),
            ])
        ]

        # Conteneur pour le tableau déroulant
        table_container = ft.Container(
            content=create_dropdown_table(rows),
            visible=False  # Masqué par défaut
        )

        # Ajouter la possibilité d'ajouter une ligne au tableau
        bouton_ajout = ft.ElevatedButton(
            text="Ajouter une ligne",
            on_click=lambda e, c=table_container, r=rows: add_row(c, r),
            visible=False  # Masqué par défaut
        )

        # Conteneur de chaque ligne avec l'événement de clic
        ligne = ft.Container(
            content=ft.Row(
                [
                    ft.Text(item["name"], size=18),  # Nom de l'élément
                    ft.Text(item["date"].strftime("%d/%m/%Y"), size=14, color=ft.colors.GREY),  # Date de création
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN  # Espace entre le nom et la date
            ),
            padding=10,
            border_radius=10,
            bgcolor=ft.colors.LIGHT_BLUE_100,
            margin=5,
            on_click=lambda e, c=table_container, b=bouton_ajout: on_row_click(e, ligne, c, b)  # Gestion du clic
        )

        # Ajouter la ligne, le tableau et le bouton à la colonne
        liste_elements.controls.append(ligne)
        liste_elements.controls.append(table_container)
        liste_elements.controls.append(bouton_ajout)

    # Ajouter la colonne à la page
    page.add(liste_elements)

# Démarrer l'application Flet
ft.app(target=main)
