import flet as ft

def main(page: ft.Page):
    # Fonction appelée lorsqu'un fichier est sélectionné
    def on_file_picker_result(e: ft.FilePickerResultEvent):
        if e.files:
            selected_file.value = f"Fichier sélectionné : {e.files[0].name}"
            # Afficher l'image sélectionnée
            image_display.src = e.files[0].path
        else:
            selected_file.value = "Aucun fichier sélectionné"
            image_display.src = None  # Efface l'image si aucun fichier n'est sélectionné
        page.update()

    # Créer un file picker pour choisir une image (logo)
    file_picker = ft.FilePicker(on_result=on_file_picker_result)

    # Ajouter le file picker à la page
    page.overlay.append(file_picker)

    # Champ pour afficher le nom du fichier sélectionné
    selected_file = ft.Text(value="Aucun fichier sélectionné")

    # Image display (cadre arrondi)
    image_display = ft.Image(
        src=None,  # Initialement vide
        width=150, 
        height=150, 
        border_radius=75,  # Rendre le cadre arrondi (75 pour un cercle complet)
        fit=ft.ImageFit.COVER  # Ajuster l'image pour qu'elle remplisse le cadre
    )

    # Bouton pour parcourir les fichiers
    browse_button = ft.ElevatedButton(
        "Parcourir",
        on_click=lambda _: file_picker.pick_files(
            allow_multiple=False,  # Permet seulement de choisir un fichier
            file_type=ft.FilePickerFileType.IMAGE  # Limite la sélection aux images
        )
    )

    # Formulaire pour ajouter un logo
    form = ft.Column([
        ft.Text("Formulaire d'ajout de logo pour l'entreprise"),
        ft.TextField(label="Nom de l'entreprise", width=400),
        browse_button,
        selected_file,  # Affiche le fichier sélectionné
        image_display,  # Affiche l'image sélectionnée dans un cadre arrondi
        ft.ElevatedButton("Soumettre", on_click=lambda _: print("Logo ajouté pour l'entreprise"))
    ], spacing=20)

    # Ajouter les éléments à la page
    page.add(form)

# Démarrer l'application Flet en mode desktop
ft.app(target=main, view=ft.AppView.FLET_APP)
