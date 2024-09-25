import flet as ft
from flet import (
    UserControl,
    Column,
    Container,
    Row,
    TextButton,
    alignment,
    border_radius,
    colors,
    padding,
    margin,
)    
    
class Sidebar(UserControl):

    def __init__(self, app_layout, page):
        super().__init__()
        self.app_layout = app_layout
        self.page = page
        self.GRH_open = False
        self.paye_open = False

        # Remplacer NavigationRailDestination par TextButton pour chaque destination
        self.top_declar_buttons = [
            TextButton(text="Déclaration", on_click=self.on_nav_button_click)
        ]
        self.top_option_buttons = [
            TextButton(text="Option audit", on_click=self.on_nav_button_click)
        ]
        self.top_fiche_buttons = [
            TextButton(text="Fiche client", on_click=self.on_nav_button_click)
        ]

        self.GRH_button = TextButton(
            text="G.R.H",
            on_click=self.toggle_GRH_list
        )
        self.GRH_list = Column(visible=False)
        self.paye_button = TextButton(
            text="Paye",
            on_click=self.toggle_paye_list
        )
        self.paye_list = Column(visible=False)

    def build(self):
        self.view = Container(
            content=Column([
                Column(self.top_fiche_buttons),  # Ajout des TextButtons à la place de NavigationRail
                # diviseur
                Container(
                    bgcolor=colors.BLACK54,
                    border_radius=border_radius.all(30),
                    height=1,
                    alignment=alignment.center_right,
                    width=220
                ),
                Row([self.GRH_button]),  # Bouton G.R.H
                self.GRH_list,
                # diviseur
                Container(
                    bgcolor=colors.BLACK54,
                    border_radius=border_radius.all(30),
                    height=1,
                    alignment=alignment.center_right,
                    width=220
                ),
                Row([self.paye_button]),
                self.paye_list,  # Liste à afficher ou cacher
                # diviseur
                Container(
                    bgcolor=colors.BLACK54,
                    border_radius=border_radius.all(30),
                    height=1,
                    alignment=alignment.center_right,
                    width=220
                ),
                Column(self.top_declar_buttons),  # Ajout des TextButtons à la place de NavigationRail
                # diviseur
                Container(
                    bgcolor=colors.BLACK54,
                    border_radius=border_radius.all(30),
                    height=1,
                    alignment=alignment.center_right,
                    width=220
                ),
                Column(self.top_option_buttons),  # Ajout des TextButtons à la place de NavigationRail
                # diviseur
                Container(
                    bgcolor=colors.BLACK54,
                    border_radius=border_radius.all(30),
                    height=1,
                    alignment=alignment.center_right,
                    width=220
                ),
            ], tight=True),
            padding=padding.all(15),
            margin=margin.all(0),
            width=250,
            height=1000,
            bgcolor=colors.GREY_700,
        )
        return self.view
    
    def toggle_paye_list(self, e):
        self.paye_open = not self.paye_open
        self.paye_list.visible = self.paye_open
        if self.paye_open:
            self.paye_list.controls = [
                TextButton(text="Traitemant de paye"),
                TextButton(text="Contrat"),
                TextButton(text="C.N.A.P.S"),
                TextButton(text="O.S.I.E"),
                TextButton(text="Autre"),
            ]
        else:
            self.paye_list.controls = []
        self.update()

    def toggle_GRH_list(self, e):
        self.GRH_open = not self.GRH_open
        self.GRH_list.visible = self.GRH_open
        if self.GRH_open:
            self.GRH_list.controls = [
                TextButton(text="Fiche salarié"),
                TextButton(text="Contrat"),
                TextButton(text="C.N.A.P.S"),
                TextButton(text="O.S.I.E"),
                TextButton(text="Autre"),
            ]
        else:
            self.GRH_list.controls = []
        self.update()

    def on_nav_button_click(self, e):
        # Gestion de la navigation à partir des TextButtons
        clicked_button = e.control
        print(f"{clicked_button.text} button clicked")
        # Vous pouvez également implémenter la logique de navigation ici
        self.update()

def ouvrir_page_navbar(page: ft.Page, entreprise_id):
    page.title = f"Informations de l'entreprise {entreprise_id}"
    app_layout = None  # Ajuster selon votre layout principal
    sidebar = Sidebar(app_layout, page)
    page.clean()
    page.add(sidebar)

# Lancer l'application Flet

