import flet as ft

def main(page: ft.Page):

    # Liste d'éléments à rechercher
    elements = [f"Élément {i}" for i in range(1, 101)]# Une liste de 100 éléments

    # Fonction pour gérer la recherche
    def on_search(e):
        search_term = search_box.value.lower()
        if search_term:
            filtered_elements = [el for el in elements if search_term in el.lower()]
            search_result.controls = [ft.Text(el) for el in filtered_elements] if filtered_elements else [ft.Text("Aucun résultat trouvé.")]
        else:
            search_result.controls = [ft.Text(el) for el in elements]
        search_result.update()

    # Barre de recherche
    search_box = ft.TextField(
        label="Recherche", 
        hint_text="Entrez un mot-clé", 
        autofocus=True, 
        width=500, 
        on_change=on_search  # Recherche dynamique
    )

    # Bouton de recherche avec une icône
    search_button = ft.IconButton(
        icon=ft.icons.SEARCH, 
        on_click=on_search
    )
    
    traitement_button = ft.Container(
        content=ft.TextButton(
            text="Traitement collectif",   
        ),
        bgcolor=ft.colors.BLUE_GREY_900,
        border_radius=10,
        height=50
    )

    # Affichage du résultat de la recherche
    search_result = ft.Column(
        controls=[ft.Text(el) for el in elements],  # Affichage initial de tous les éléments
        scroll=ft.ScrollMode.AUTO,  # Ajoute un scroll si la liste est longue
        expand=True  # S'adapte à la taille disponible
    )

    # Ajouter les éléments à la page
    page.add(
        ft.Row(
            [search_box, search_button,traitement_button], 
            alignment=ft.MainAxisAlignment.START
        ),
        search_result
    )

ft.app(target=main)
