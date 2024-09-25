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
            TextButton(text="Déclaration", on_click=self.on_nav_button_click, bgcolor=colors.GREEN_500)
        ]
        self.top_option_buttons = [
            TextButton(text="Option audit", on_click=self.on_nav_button_click, bgcolor=colors.GREEN_500)
        ]
        self.top_fiche_buttons = [
            TextButton(text="Fiche client", on_click=self.on_nav_button_click, bgcolor=colors.GREEN_500)
        ]

        # Boutons principaux
        self.GRH_button = TextButton(
            text="G.R.H",
            on_click=self.toggle_GRH_list,
            bgcolor=colors.BLUE_700,  # Couleur principale pour G.R.H
            color=colors.WHITE,
        )
        self.GRH_list = Column(visible=False)
        self.paye_button = TextButton(
            text="Paye",
            on_click=self.toggle_paye_list,
            bgcolor=colors.BLUE_700,  # Couleur principale pour Paye
            color=colors.WHITE,
        )
        self.paye_list = Column(visible=False)

    def build(self):
        self.view = Container(
            content=Column([  
                Column(self.top_fiche_buttons),  # Ajout des TextButtons à la place de NavigationRail
                # diviseur
                self._create_divider(),
                Row([self.GRH_button]),  # Bouton G.R.H
                self.GRH_list,
                # diviseur
                self._create_divider(),
                Row([self.paye_button]),  # Bouton Paye
                self.paye_list,
                # diviseur
                self._create_divider(),
                Column(self.top_declar_buttons),  # Ajout des TextButtons à la place de NavigationRail
                # diviseur
                self._create_divider(),
                Column(self.top_option_buttons),  # Ajout des TextButtons à la place de NavigationRail
                # diviseur
                self._create_divider(),
            ], tight=True),
            padding=padding.all(15),
            margin=margin.all(0),
            width=250,
            height=1000,
            bgcolor=colors.GREY_700,
        )
        return self.view

    def _create_divider(self):
        return Container(
            bgcolor=colors.BLACK54,
            border_radius=border_radius.all(30),
            height=1,
            alignment=alignment.center_right,
            width=220
        )
    
    def toggle_paye_list(self, e):
        self.paye_open = not self.paye_open
        self.paye_list.visible = self.paye_open
        if self.paye_open:
            self.paye_list.controls = [
                TextButton(text="Traitemant de paye", bgcolor=colors.ORANGE_300, color=colors.BLACK),
                TextButton(text="Contrat", bgcolor=colors.ORANGE_300, color=colors.BLACK),
                TextButton(text="C.N.A.P.S", bgcolor=colors.ORANGE_300, color=colors.BLACK),
                TextButton(text="O.S.I.E", bgcolor=colors.ORANGE_300, color=colors.BLACK),
                TextButton(text="Autre", bgcolor=colors.ORANGE_300, color=colors.BLACK),
            ]
        else:
            self.paye_list.controls = []
        self.update()

    def toggle_GRH_list(self, e):
        self.GRH_open = not self.GRH_open
        self.GRH_list.visible = self.GRH_open
        if self.GRH_open:
            self.GRH_list.controls = [
                TextButton(text="Fiche salarié", bgcolor=colors.YELLOW_300, color=colors.BLACK),
                TextButton(text="Contrat", bgcolor=colors.YELLOW_300, color=colors.BLACK),
                TextButton(text="C.N.A.P.S", bgcolor=colors.YELLOW_300, color=colors.BLACK),
                TextButton(text="O.S.I.E", bgcolor=colors.YELLOW_300, color=colors.BLACK),
                TextButton(text="Autre", bgcolor=colors.YELLOW_300, color=colors.BLACK),
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

def main(page: ft.Page):
    # Exemple de lancement de la page avec un id d'entreprise
    ouvrir_page_navbar(page, entreprise_id="1234")

# Lancer l'application Flet avec ft.app()
ft.app(target=main)
