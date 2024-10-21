import flet as ft

def open_irsa_view(page: ft.Page, month, year):
    # Fonction pour fermer la fenêtre IRSA
    def close_irsa(e):
        page.overlay.clear()  # Retirer la vue IRSA et le voile de fond
        page.update()

    # Conteneur pour le voile flou en arrière-plan
    blur_overlay = ft.Container(
        bgcolor=ft.colors.with_opacity(0.6, ft.colors.BLACK),  # Voile semi-transparent
        expand=True,
        on_click=close_irsa,  # Ferme la fenêtre si on clique en dehors du modal
    )

    # Contenu de la fenêtre IRSA
    irsa_modal = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(f"IRSA - {month}", size=30, weight=ft.FontWeight.BOLD),
                        ft.Text(f"{year}", size=20),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Divider(),
                ft.Row([ft.Text("État nominatif"), ft.ElevatedButton("Télécharger",expand=True)], spacing=200),
                ft.Row([ft.Text("Bordereau de revenu"), ft.ElevatedButton("Télécharger",expand=True)], spacing=165),
                ft.Row([ft.Text("Fiche de ventilation"), ft.ElevatedButton("Télécharger",expand=True)], spacing=170),
                ft.Divider(),
                ft.Row(
                    [
                        ft.Column([ft.Text("ON"), ft.ElevatedButton("Upload", expand=True)]),
                        ft.Column([ft.Text("AR"), ft.ElevatedButton("Upload", expand=True)]),
                        ft.Column([ft.Text("Récépissé"), ft.ElevatedButton("Upload", expand=True)]),
                    ],
                    spacing=20,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),  # Bouton pour fermer
            ],
            spacing=20
        ),
        padding=ft.padding.all(20),
        border=ft.border.all(2, ft.colors.BLACK),  # Bordure noire
        border_radius=10,  # Coins arrondis
        bgcolor=ft.colors.BLACK,  # Fond noir
        width=500,  # Largeur de la fenêtre modale
        height=400,  # Hauteur de la fenêtre modale
        alignment=ft.alignment.center  # Centré dans l'écran
    )

    # Ajouter le flou de fond et le modal IRSA à la page
    page.overlay.append(blur_overlay)
    page.overlay.append(irsa_modal)
    page.update()

def show_months_list(page: ft.Page):
    show_trimestres = False
    trimestres_list = ft.Ref()
    container_ref = ft.Ref()

    def toggle_trimestres(e):
        nonlocal show_trimestres
        show_trimestres = not show_trimestres
        trimestres_list.current.visible = show_trimestres
        container_ref.current.height = 350 if show_trimestres else 80
        page.update()

    def open_month_irsa(e, month):
        open_irsa_view(page, month, "2024")

    def create_clickable_row(month):
        return ft.GestureDetector(
            content=ft.Row(
                [ft.Text(month, size=18)],
                alignment="start",
                vertical_alignment="center",
            ),
            on_tap=lambda e: open_month_irsa(e, month),
        )

    container = ft.Container(
        content=ft.Column(
            [
                ft.GestureDetector(
                    content=ft.Row(
                        [
                            ft.Text("ANNÉE", size=20),
                            ft.Text("2024", size=20),
                        ],
                        alignment="spaceBetween"
                    ),
                    on_tap=toggle_trimestres
                ),
                ft.Divider(height=10),
                ft.Column(
                    [
                        create_clickable_row("Janvier"),
                        create_clickable_row("Février"),
                        create_clickable_row("Mars"),
                        create_clickable_row("Avril"),
                    ],
                    ref=trimestres_list,
                    visible=False
                )
            ],
            spacing=5
        ),
        padding=20,
        border_radius=10,
        border=ft.border.all(1, "black"),
        height=80,
        ref=container_ref,
    )

    page.controls.clear()
    page.add(container)
    page.update()

def main(page: ft.Page):
    page.title = "Trimestres de l'année"
    show_months_list(page)

ft.app(target=main)
