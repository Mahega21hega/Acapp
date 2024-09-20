import flet as ft

def main(page: ft.Page):
    page.title = "Modification d'employé"

    # Créer les éléments de l'interface
    name_label = ft.Text("Nom et Prénom:")
    name_field = ft.TextField(expand=True)
    employee_id_label = ft.Text("Matricule:")
    employee_id_field = ft.TextField(expand=True)
    hire_date_label = ft.Text("Date d'embauche:")
    hire_date_field = ft.TextField(expand=True)
    phone_number_label = ft.Text("Numéro de téléphone:")
    phone_number_field = ft.TextField(expand=True)

    # Créer la colonne principale
    col = ft.Column([
        ft.Text("MIHARI", size=20, weight=ft.FontWeight.BOLD),
        ft.Row([name_label, name_field], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Row([employee_id_label, employee_id_field], alignment=ft.MainAxisAlignment.SPACE_AROUND),
        ft.Row([hire_date_label, hire_date_field], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Row([phone_number_label, phone_number_field], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    ])

    page.add(col)

ft.app(target=main)