import flet as ft

# Fonction principale
def main(page: ft.Page):

    # Initialiser le compteur d'ID
    id_counter = 1

    # Fonction pour ajouter une nouvelle ligne
    def ajouter_rubrique(e):
        nonlocal id_counter
        ajouter_nouvelle_ligne(id_counter, f"Nom {id_counter}", "XXXXXX", "JJ/MM/AAAA", "Non", "Inactif")
        id_counter += 1
        data_table.update()

    # Fonction pour afficher un dialogue de confirmation avant suppression
    def demander_confirmation(row_index):
        # Fonction appelée lorsque l'utilisateur confirme la suppression
        def handle_delete_confirmation(e):
            data_table.rows.pop(row_index)  # Supprimer la ligne
            reindexer_lignes()  # Mettre à jour les indices de suppression après la suppression
            data_table.update()
            page.dialog.open = False  # Fermer le dialogue de confirmation
            page.update()

        # Fonction pour annuler la suppression
        def cancel(e):
            page.dialog.open = False
            page.update()

        # Créer et afficher le dialogue de confirmation
        confirmation_dialog = ft.AlertDialog(
            title=ft.Text("Confirmer la suppression"),
            content=ft.Text("Êtes-vous sûr de vouloir supprimer cette ligne ?"),
            actions=[
                ft.TextButton("Annuler", on_click=cancel),
                ft.TextButton("Confirmer", on_click=handle_delete_confirmation),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.dialog = confirmation_dialog
        confirmation_dialog.open = True
        page.update()

    # Fonction pour ajouter une ligne avec les données fournies
    def ajouter_nouvelle_ligne(id, nom, cnaps, embauche, alloc_familiale, statut, retenu):
        delete_icon = ft.IconButton(
            icon=ft.icons.DELETE,
            on_click=lambda e: demander_confirmation(len(data_table.rows))  # Associer la fonction supprimer à l'index
        )
        new_row = ft.DataRow(cells=[
            ft.DataCell(ft.Text(str(id))),  # ID auto-incrémenté
            ft.DataCell(ft.Text(nom)),
            ft.DataCell(ft.Text(cnaps)),
            ft.DataCell(ft.Text(embauche)),
            ft.DataCell(ft.Text(alloc_familiale)),
            ft.DataCell(ft.Text(statut)),
            ft.DataCell(ft.Text(retenu)),
            ft.DataCell(delete_icon),  # Ajouter l'icône de suppression
        ])
        data_table.rows.append(new_row)

    # Fonction pour réindexer les lignes après suppression
    def reindexer_lignes():
        for i, row in enumerate(data_table.rows):
            delete_button = row.cells[-1].content
            delete_button.on_click = lambda e, row_index=i: demander_confirmation(row_index)

    # Créer un tableau avec 6 colonnes plus une colonne de suppression
    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Liste de rubrique")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Base")),
            ft.DataColumn(ft.Text("Montant forfait")),
            ft.DataColumn(ft.Text("Gain")),
            ft.DataColumn(ft.Text("Retenu")),
            ft.DataColumn(ft.Text("Action")),  # Colonne pour les actions
        ],
        rows=[
            # Lignes initiales
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("1")),
                ft.DataCell(ft.Text("John Doe")),
                ft.DataCell(ft.Text("123456789")),
                ft.DataCell(ft.Text("01/01/2020")),
                ft.DataCell(ft.Text("Oui")),
                ft.DataCell(ft.Text("Actif")),
                ft.DataCell(ft.Text("montant")),
                ft.DataCell(ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e: demander_confirmation(0))),  # Supprimer ligne
            ]),
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("2")),
                ft.DataCell(ft.Text("Jane Smith")),
                ft.DataCell(ft.Text("987654321")),
                ft.DataCell(ft.Text("15/06/2019")),
                ft.DataCell(ft.Text("Non")),
                ft.DataCell(ft.Text("Inactif")),
                ft.DataCell(ft.Text("montant")),
                ft.DataCell(ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e: demander_confirmation(1))),  # Supprimer ligne
            ]),
        ],
    )

    # Ajouter le tableau et le bouton d'ajout à la page
    page.add(
        data_table,
        ft.ElevatedButton("Ajouter une rubrique", on_click=ajouter_rubrique)
    )

# Lancer l'application
ft.app(target=main)
