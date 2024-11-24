from data_get import Instance
import flet as ft

def main(page: ft.Page):
    page.title = "Formula Data"
    start = Instance()

    def show_latest():
        page.views.clear()
        items = []
        stuff = []
        latest = start.get_latest()
        start.get_res(latest)

        txt = ft.Text("Latest Session: " + str(latest))

        for i in range(0, 3):
            cont = ft.Container(
                content=ft.Text(f"P{i+1}: {start.drivers[i]}"),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLACK,
                width=300,
                height=150,
                border_radius=50,
            )
            items.append(cont)
        btn = ft.TextButton(text="View More...", on_click=lambda e: page.go("/latest_session"))
        items.append(btn)

        row = ft.Row(
            spacing=15,
            controls=items
        )
        stuff.append(txt)
        stuff.append(row)
        col = ft.Column(
            controls=stuff,
        )
        return col

    def select_session():
        season = Instance()
        season.get_meetings()
        season23 = []
        season24 = []
        for meeting in season.meetings:
            btn = ft.TextButton(
                content=ft.Text(
                    meeting,
                    color=ft.colors.WHITE,
                ),
                on_click=lambda e, m=meeting: print(f"Selected meeting: {m.id}"),
            )
            if meeting.year == 2023:
                season23.append(btn)
            elif meeting.year == 2024:
                season24.append(btn)

        tabs = ft.Tabs(
            selected_index=1,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="2023",
                    content=ft.Column(controls=season23, spacing=15, scroll=True)
                ),
                ft.Tab(
                    text="2024",
                    content=ft.Column(controls=season24, spacing=15, scroll=True),
                ),
            ],
            expand=1,
        )
        return tabs

    def latest_data():
        items = []
        tbl = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Position"), numeric=True),
                ft.DataColumn(ft.Text("Name")),
                ft.DataColumn(ft.Text("Team")),
                ft.DataColumn(ft.Text("Fastest Lap")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("John")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("43")),
                        ft.DataCell(ft.Text("goober")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("John")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("43")),
                        ft.DataCell(ft.Text("goober")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("John")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("43")),
                        ft.DataCell(ft.Text("goober")),
                    ],
                ),
            ],
        )
        btn = ft.TextButton(text="Menu", on_click=lambda e: page.go("/"))
        items.append(tbl)
        items.append(btn)
        col = ft.Column(
            controls=items
        )
        return col

    def on_route_change(e):
        page.views.clear()
        if e.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [
                        show_latest(),
                        select_session(),
                    ]
                )
            )
        if e.route == "/latest_session":
            page.views.append(
                ft.View(
                    "/latest_session",
                    [
                        latest_data(),
                    ]
                )
            )
        page.update()

    # Set initial route
    page.on_route_change = on_route_change
    page.go("/")
    page.update()

ft.app(main)
