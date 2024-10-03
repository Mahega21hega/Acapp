import flet as ft

def main(page: ft.Page):
    page.bgcolor=ft.colors.GREY_900
    page.title = "Fiche Client - Informations Entreprise"
    
    # Logo de l'entreprise
    logo = ft.Image(src="97968957-14b7-40d9-98c2-042c77a49414.jpg", width=150, height=150, fit=ft.ImageFit.COVER)
    
    # Informations générales sur l'entreprise
    nom_entreprise_field = ft.TextField(label="Nom de l'entreprise", hint_text="Nom de l'entreprise", width=400)
    siren_field = ft.TextField(label="SIREN", hint_text="Numéro SIREN", width=300)  # Numéro d'immatriculation de l'entreprise
    adresse_field = ft.TextField(label="Adresse", hint_text="Adresse complète", width=400)
    email_field = ft.TextField(label="Email", hint_text="Email de l'entreprise", width=400)
    phone_field = ft.TextField(label="Téléphone", hint_text="Numéro de téléphone", width=300)
    
    # Informations supplémentaires
    site_web_field = ft.TextField(label="Site Web", hint_text="Site web de l'entreprise", width=400)
    secteur_activite_field = ft.TextField(label="Secteur d'activité", hint_text="Ex: Technologie, Commerce", width=400)
    
    # Bouton pour ajouter l'entreprise
    btn_add = ft.ElevatedButton(text="Ajouter l'entreprise", on_click=lambda e: add_entreprise())

    def add_entreprise():
        # Fonction pour ajouter l'entreprise (à compléter selon votre logique)
        print(f"Ajout de l'entreprise: {nom_entreprise_field.value}, SIREN: {siren_field.value}")

    # Disposition des champs
    page.add(
        ft.Row([logo]),
        ft.Row([nom_entreprise_field]),
        ft.Row([siren_field, adresse_field]),
        ft.Row([email_field, phone_field]),
        ft.Row([site_web_field, secteur_activite_field]),
        ft.Row([btn_add])
    )

# Exécuter l'application
ft.app(target=main)
