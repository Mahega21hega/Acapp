import flet as ft
from flet import (
    UserControl,
    Column,
    Container,
    Row,
    TextButton,
    Text,
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
            self.create_colored_button("Déclaration", colors.RED_ACCENT_700, self.on_nav_button_click)
        ]
        self.top_option_buttons = [
            self.create_colored_button("Option audit", colors.RED_ACCENT_700, self.on_nav_button_click)
        ]
        self.top_fiche_buttons = [
            self.create_colored_button("Fiche client", colors.RED_ACCENT_700, self.on_nav_button_click)
        ]

        self.GRH_button = self.create_colored_button("G.R.H", colors.RED_ACCENT_700, self.toggle_GRH_list)
        self.GRH_list = Column(visible=False)

        self.paye_button = self.create_colored_button("Paye", colors.RED_ACCENT_700, self.toggle_paye_list)
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
            bgcolor=colors.WHITE,
        )
        return self.view

    def toggle_paye_list(self, e):
        # Fermer la liste GRH si elle est ouverte
        if self.GRH_open:
            self.GRH_open = False
            self.GRH_list.visible = False

        self.paye_open = not self.paye_open
        self.paye_list.visible = self.paye_open
        if self.paye_open:
            self.paye_list.controls = [
                TextButton(content=Text("Traitement paye", color=colors.BLACK)),
                TextButton(content=Text("Contrat", color=colors.BLACK)),
                TextButton(content=Text("C.N.A.P.S", color=colors.BLACK)),
                TextButton(content=Text("O.S.I.E", color=colors.BLACK)),
                TextButton(content=Text("Autre", color=colors.BLACK)),
            ]
        else:
            self.paye_list.controls = []
        self.update()

    def toggle_GRH_list(self, e):
        # Fermer la liste Paye si elle est ouverte
        if self.paye_open:
            self.paye_open = False
            self.paye_list.visible = False

        self.GRH_open = not self.GRH_open
        self.GRH_list.visible = self.GRH_open
        if self.GRH_open:
            self.GRH_list.controls = [
                TextButton(content=Text("Fiche salarié", color=colors.BLACK)),
                TextButton(content=Text("Contrat", color=colors.BLACK)),
                TextButton(content=Text("C.N.A.P.S", color=colors.BLACK)),
                TextButton(content=Text("O.S.I.E", color=colors.BLACK)),
                TextButton(content=Text("Autre", color=colors.BLACK)),
            ]
        else:
            self.GRH_list.controls = []
        self.update()

    def create_colored_button(self, text, bg_color, on_click=None):
        return Container(
            content=TextButton(
                content=Text(text, color=colors.WHITE),  # Utiliser Text pour la couleur du texte
                on_click=on_click,
            ),
            bgcolor=bg_color,
            padding=padding.symmetric(horizontal=15, vertical=5),
            border_radius=border_radius.all(5),
            width=220
        )

    def on_nav_button_click(self, e):
        # Gestion de la navigation à partir des TextButtons
        clicked_button = e.control
        print(f"{clicked_button.content.value} button clicked")
        
        # Fermer toutes les listes déroulantes
        self.GRH_open = False
        self.GRH_list.visible = False
        self.paye_open = False
        self.paye_list.visible = False

        self.update()  # Mettre à jour l'interface

def ouvrir_page_navbar(page: ft.Page):#, entreprise_id):
    page.title = f"Informations de l'entreprise"# {entreprise_id}"
    app_layout = None  # Ajuster selon votre layout principal
    sidebar = Sidebar(app_layout, page)
    page.clean()
    page.add(sidebar)

# Lancer l'application Flet
ft.app(ouvrir_page_navbar)
