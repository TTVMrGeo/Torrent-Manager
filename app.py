from main import torrent_management
import flet as ft, json

settings = json.load(open("settings.json", "r"))
tman = torrent_management(settings['save_path'], settings['cache_path'])

def main(page: ft.Page):
    page.title = "Torrent Manager"

    def change_settings(e):
        def update_settings():
            settings["save_path"] = save_path.value
            settings["cache_path"] = cache_path.value
            json.dump(settings, open("settings.json", "w"), indent=4)
            page.pop_dialog()
            page.update()

        save_path = ft.TextField(
            label="Save path",
            value=settings["save_path"]
        )

        cache_path = ft.TextField(
            label="Cache path", 
            value=settings["cache_path"]
        )

        settings_dialog = ft.AlertDialog(
            modal=True, 
            title=ft.Text(value="Settings"),
            content=ft.Column(
                controls=[save_path, cache_path]
            ),
            actions=[
                ft.FilledButton(content="Cancel", on_click=lambda e: page.pop_dialog()),
                ft.FilledButton(content="Save", on_click=update_settings),
            ],
            actions_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )
        page.show_dialog(settings_dialog)

    page.add(ft.Row(
        ft.IconButton(ft.Icons.SETTINGS, on_click=change_settings),
        ft.Text("Saves")
    ))
    saved_list = ft.Column(
        controls=[]
    )

    def update_saved_list():
        saved_list.controls.clear()
        for item in tman.load(tman.saved_path).keys():
            saved_list.controls.append(
                ft.Row(
                    controls=[
                        ft.IconButton(ft.Icons.DELETE, on_click=lambda e: remove(item)),
                        ft.IconButton(ft.Icons.PLAY_ARROW, on_click=lambda e: play(item)),
                        ft.Text(value=item, color=ft.Colors.WHITE)
                    ]
                )
            )
        page.update()

    def play(item):
        tman.play(item)

    def add(item):
        tman.save(item)
        update_saved_list()  # Refresh the UI

    def remove(item):
        tman.remove(item)
        update_saved_list()  # Refresh the UI

    link = ft.TextField(value="", border_color=ft.Colors.WHITE, color=ft.Colors.WHITE)
    bottom = ft.Row(
        controls=[
            ft.Text(value="Magnet Link:"),
            link,
            ft.IconButton(ft.Icons.ADD, on_click=lambda e: add(link.value))
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    page.theme_mode = ft.ThemeMode.DARK
    page.bottom_appbar = ft.BottomAppBar(bgcolor=ft.Colors.BLACK_12, content=bottom, height=100, width=1000)
    update_saved_list()
    page.add(saved_list)
ft.run(main)