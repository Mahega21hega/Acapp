import flet as ft

def main(page: ft.Page):
    page.title = "Trimestres de l'année"
    
    # Correct initialization of Ref without arguments
    show_trimestres = ft.Ref()  # This will later hold a bool value
    trimestres_list = ft.Ref()  # This will later hold a Column
    container_ref = ft.Ref()  # Reference to the container
    
    # Function to toggle the visibility of the trimesters
    def toggle_trimestres(e):
        if show_trimestres.current is None:
            show_trimestres.current = False
        show_trimestres.current = not show_trimestres.current
        trimestres_list.current.visible = show_trimestres.current
        
        # Adjust the container height based on the visibility of the trimesters
        if show_trimestres.current:
            container_ref.current.height = 350  # Larger height to show the list
        else:
            container_ref.current.height = 80  # Default smaller height
        page.update()
    
    # Function to close the modal window
    def close_modal(e):
        page.overlay.clear()  # Clear the modal view and the background blur
        page.update()

    # Function to open the modal window for a selected trimester
    def open_trimestre_view(e, trimestre):
        # Background blur container
        blur_overlay = ft.Container(
            bgcolor=ft.colors.with_opacity(0.6, ft.colors.BLACK),  # Semi-transparent background
            expand=True,
            on_click=close_modal  # Close the modal if the background is clicked
        )

        # Content of the modal window
        modal_content = ft.Container(
            content=ft.Column(
                [
                    ft.Text(f"IRSA - {trimestre}", size=30, weight=ft.FontWeight.BOLD),
                    ft.Divider(),
                    ft.Row([ft.Text("État nominatif"), ft.ElevatedButton("Télécharger",expand=True)], spacing=200),
                    ft.Divider(),
                    ft.Row(
                    [
                        ft.Column([ft.Text("ON"), ft.ElevatedButton("Upload", expand=True)]),
                        ft.Column([ft.Text("AR"), ft.ElevatedButton("Upload", expand=True)]),
                        ft.Column([ft.Text("Récépissé"), ft.ElevatedButton("Upload", expand=True)]),
                    ],
                    spacing=20,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ],
                spacing=20
            ),
            padding=ft.padding.all(20),
            border=ft.border.all(2, ft.colors.BLACK),  # Black border
            border_radius=10,  # Rounded corners
            bgcolor=ft.colors.BLACK,  # White background
            width=500,  # Width of the modal window
            height=300,  # Height of the modal window
            alignment=ft.alignment.center  # Centered on the screen
        )

        # Add the blur background and the modal to the page
        page.overlay.append(blur_overlay)
        page.overlay.append(modal_content)
        page.update()

    # Function to create a clickable row for each trimester
    def create_clickable_row(trimestre):
        return ft.GestureDetector(
            content=ft.Container(
                content=ft.Row(
                    [ft.Text(trimestre, size=18)],  # Name of the trimester
                    alignment="start",
                    vertical_alignment="center",
                ),  # Differentiate each row with background color or style
                padding=ft.padding.symmetric(vertical=10, horizontal=20),
                border_radius=ft.border_radius.all(5),  # Rounded corners for each row
            ),
            on_tap=lambda e: open_trimestre_view(e, trimestre),  # Handle the click to open the trimester view
        )

    # Main container with padding
    container = ft.Container(
        content=ft.Column(
            [
                # GestureDetector wrapping the Row to handle click events
                ft.GestureDetector(
                    content=ft.Row(
                        [
                            ft.Text("ANNÉE", size=20),
                            ft.Text("2024", size=20),
                        ],
                        alignment="spaceBetween"
                    ),
                    on_tap=toggle_trimestres  # Click event to show or hide the trimesters
                ),
                ft.Divider(height=10),  # Divider line
                ft.Column(
                    [
                        create_clickable_row("1er Trimestre"),
                        create_clickable_row("2ème Trimestre"),
                        create_clickable_row("3ème Trimestre"),
                        create_clickable_row("4ème Trimestre"),
                    ],
                    spacing=5,
                    ref=trimestres_list,  # Reference to the list of trimesters
                    visible=False  # Initially hide the trimesters
                )
            ],
            spacing=5,  # Space between items
        ),
        padding=20,  # Inner padding of the container
        border_radius=10,  # Rounded corners
        border=ft.border.all(1, "black"),  # Black border
        height=80,  # Default smaller height
        ref=container_ref,  # Reference to the container
        expand_loose=True  # Adjusted container width
    )
    
    page.add(container)

ft.app(target=main)
