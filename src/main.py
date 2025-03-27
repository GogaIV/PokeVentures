import flet as ft


def main(page: ft.Page):
    page.title = 'PokéVentures'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    clicked = ft.Text("Test")

    def home_button(e):
            page.add(
                  ft.Row([
                        clicked
                        ], alignment = ft.MainAxisAlignment.CENTER))
            page.update()


    btn = ft.ElevatedButton("Click me!", on_click=home_button)

    page.add(
          ft.SafeArea(
                ft.Text('PokéVentures', text_align=center))
    )

    page.add(
                ft.Row([btn],ft.MainAxisAlignment.CENTER))
    page.update()


ft.app(main)
