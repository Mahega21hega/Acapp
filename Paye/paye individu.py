import flet as ft

# Fonction principale
def main(page: ft.Page):
    page.bgcolor = ft.colors.GREY_900
    page.vertical_alignment = ft.MainAxisAlignment.START

    id_counter = 1
    text_fields = []  # Liste pour stocker les TextField

    def ajouter_rubrique(e):
        nonlocal id_counter
        ajouter_nouvelle_ligne(id_counter, f"Nom {id_counter}", "XXXXXX", "JJ/MM/AAAA", "Non", "Inactif", "montant")
        id_counter += 1
        data_table.update()

    def demander_confirmation(row_index):
        def handle_delete_confirmation(e):
            try:
                data_table.rows.pop(row_index)
                reindexer_lignes()
                data_table.update()
                confirmation_dialog.open = False
                page.update()
            except IndexError:
                print(f"Index {row_index} hors limites")

        def cancel(e):
            confirmation_dialog.open = False
            page.update()

        confirmation_dialog = ft.AlertDialog(
            title=ft.Text("Confirmer la suppression"),
            content=ft.Text("Êtes-vous sûr de vouloir supprimer cette ligne ?"),
            actions=[
                ft.TextButton("Annuler", on_click=cancel),
                ft.TextButton("Confirmer", on_click=handle_delete_confirmation),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.overlay.append(confirmation_dialog)
        confirmation_dialog.open = True
        page.update()

    def ajouter_nouvelle_ligne(id, nom, cnaps, embauche, alloc_familiale, statut, retenu):
        delete_icon = ft.IconButton(
            icon=ft.icons.DELETE,
            on_click=lambda e, index=len(data_table.rows): demander_confirmation(index)
        )
        new_row = ft.DataRow(cells=[
            ft.DataCell(ft.Text(str(id))),
            ft.DataCell(ft.Text(nom)),
            ft.DataCell(ft.Text(cnaps)),
            ft.DataCell(ft.Text(embauche)),
            ft.DataCell(ft.Text(alloc_familiale)),
            ft.DataCell(ft.Text(statut)),
            ft.DataCell(ft.Text(retenu)),
            ft.DataCell(delete_icon),
        ])
        data_table.rows.append(new_row)

    def reindexer_lignes():
        for i, row in enumerate(data_table.rows):
            delete_button = row.cells[-1].content
            delete_button.on_click = lambda e, row_index=i: demander_confirmation(row_index)

    # Fonction pour vider les champs de texte
    def supprimer_tout(e):
        for text_field in text_fields:
            text_field.value = ""  # Efface le contenu du TextField
        page.update()

    # Créer le formulaire et ajouter chaque TextField à la liste text_fields
    forum = ft.ResponsiveRow(
        controls=[
            ft.Column([ft.Text("Salaire brut:"), ft.TextField()], col={"xs": 12, "sm": 6, "md": 6, "lg": 4}),
            ft.Column([ft.Text("Salaire plafonne:"), ft.TextField()], col={"xs": 12, "sm": 6, "md": 6, "lg": 4}),
            ft.Column([ft.Text("Cnaps salarial:"), ft.TextField()], col={"xs": 12, "sm": 6, "md": 6, "lg": 4}),
            ft.Column([ft.Text("Osie salarial:"), ft.TextField()], col={"xs": 12, "sm": 6, "md": 6, "lg": 4}),
            ft.Column([ft.Text("Total hs exo:"), ft.TextField()], col={"xs": 12, "sm": 6, "md": 6, "lg": 4}),
            ft.Column([ft.Text("Salaire brut imposable:"), ft.TextField()], col={"xs": 12, "sm": 6, "md": 6, "lg": 4}),
            ft.Column([ft.Text("Salaire net imposable:"), ft.TextField()], col={"xs": 12, "sm": 6, "md": 6, "lg": 4}),
            ft.Column([ft.Text("Irsa brut:"), ft.TextField()], col={"xs": 12, "sm": 6, "md": 6, "lg": 4}),
            ft.Column([ft.Text("Réduction enfant:"), ft.TextField()], col={"xs": 12, "sm": 6, "md": 6, "lg": 4}),
            ft.Column([ft.Text("Irsa net:"), ft.TextField()], col={"xs": 12, "sm": 6, "md": 6, "lg": 4}),
            ft.Column([ft.Text("Salaire net:"), ft.TextField()], col={"xs": 12, "sm": 6, "md": 6, "lg": 4}),
            ft.Column([ft.Text("Cnaps patronal:"), ft.TextField()], col={"xs": 12, "sm": 6, "md": 6, "lg": 4}),
            ft.Column([ft.Text("Osie patronal:"), ft.TextField()], col={"xs": 12, "sm": 6, "md": 6, "lg": 4}),
            ft.Column([ft.Text("Fmfp:"), ft.TextField()], col={"xs": 12, "sm": 6, "md": 6, "lg": 4}),
            ft.Column([ft.Text("Cotisation salarial:"), ft.TextField()], col={"xs": 12, "sm": 6, "md": 6, "lg": 4}),
            ft.Column([ft.Text("Cotisation patronal:"), ft.TextField()], col={"xs": 12, "sm": 6, "md": 6, "lg": 4}),
            ft.Column([ft.Text("Masse salarial:"), ft.TextField()], col={"xs": 12, "sm": 6, "md": 6, "lg": 4}),
        ]
    )
    
    # Ajouter chaque TextField du forum dans la liste text_fields
    for control in forum.controls:
        text_field = control.controls[1]  # Récupère le TextField dans chaque colonne
        text_fields.append(text_field)

    # Créer un tableau avec des colonnes
    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Liste de rubrique")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Base")),
            ft.DataColumn(ft.Text("Montant forfait")),
            ft.DataColumn(ft.Text("Gain")),
            ft.DataColumn(ft.Text("Retenu")),
            ft.DataColumn(ft.Text("Action")),
        ],
        rows=[],
        expand=True,
    )

    page.add(
        ft.Column(
            controls=[
                data_table,
                ft.Row([ft.ElevatedButton("Ajouter une rubrique", on_click=ajouter_rubrique)]),
                forum,
                ft.Row(
                    [ft.ElevatedButton("Supprimer tout", on_click=supprimer_tout, color="red")],
                    alignment=ft.MainAxisAlignment.END
                )
            ],
            scroll=ft.ScrollMode.ALWAYS,
            expand=True,
        )
    )

# Lancer l'application
ft.app(target=main)
