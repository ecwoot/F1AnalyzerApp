from data_get import Instance
import flet as ft

# Shared state
current_instance = Instance()
current_meeting = None
current_session = None

def main(page: ft.Page):
    page.title = "Formula Data"

    def show_latest():
        items = []
        stuff = []
        current_instance.get_latest()
        latest = current_instance.latest
        current_instance.get_res(latest)
        global current_session 
        current_session = latest

        txt = ft.Text("Latest Session: " + str(latest))
        stuff.append(txt)

        for i in range(3):
            cont = ft.Container(
                content=ft.Text(f"P{i+1}: {current_instance.drivers[i]}", color=ft.colors.BLACK),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=current_instance.drivers[i].color,
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
        stuff.append(row)

        col = ft.Column(controls=stuff)
        return col

    def select_meeting():
        season = Instance()
        season.get_meetings()
        season23 = []
        season24 = []
        for meeting in season.meetings:
            btn = ft.TextButton(
                content=ft.Text(meeting, color=ft.colors.WHITE),
                on_click=lambda e, m=meeting: navigate_to_meeting(m, season),
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
    
    def select_session(meeting, season):
        season.get_sessions(meeting.id)
        btns = []
        for session in season.sessions:
            btn = ft.TextButton(
                content=ft.Text(session, color=ft.colors.WHITE),
                on_click=lambda e, s=session: navigate_to_session(s, season),
            )
            btns.append(btn)
        col = ft.Column(controls=btns)
        return col

    def find_laps(instance, driver):
        for lap in instance.laps:
            if lap.number == driver.number:
                return str(lap)

    def show_data(instance):
        items = []
        rows = []
        instance.get_laps(current_session)
        for driver in instance.drivers:
            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(driver.pos)),
                        ft.DataCell(ft.Text(driver.name)),
                        ft.DataCell(ft.Text(driver.team)),
                        ft.DataCell(ft.Text(find_laps(instance, driver))),
                    ],
                ),
            )
        tbl = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Position")),
                ft.DataColumn(ft.Text("Name")),
                ft.DataColumn(ft.Text("Team")),
                ft.DataColumn(ft.Text("Fastest Lap")),
            ],
            rows=rows,
        )
        btn = ft.ElevatedButton(text="Menu", on_click=lambda e: page.go("/"))
        items.append(tbl)
        items.append(btn)
        list_view = ft.ListView(
            expand=1,
            auto_scroll=True,
            padding=10,
            controls=items,
        )
        return list_view

    def navigate_to_meeting(meeting, instance):
        global current_instance, current_meeting
        current_instance = instance
        current_meeting = meeting
        page.go("/meeting")

    def navigate_to_session(session, instance):
        global current_instance, current_session
        current_instance = instance
        current_session = session
        page.go("/session")

    def on_route_change(e):
        page.views.clear()
        if e.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    controls=[
                        show_latest(),
                        select_meeting(),
                    ]
                )
            )
        elif e.route == "/latest_session":
            page.views.append(
                ft.View(
                    "/latest_session",
                    controls=[
                        show_data(current_instance),
                    ]
                )
            )
        elif e.route == "/meeting":
            page.views.append(
                ft.View(
                    "/meeting",
                    controls=[
                        select_session(current_meeting, current_instance),
                    ]
                )
            )
        elif e.route == "/session":
            current_instance.get_res(current_session)
            page.views.append(
                ft.View(
                    "/session",
                    controls=[
                        show_data(current_instance),
                    ],
                    scroll=True
                )
            )
        page.update()

    # Set initial route
    page.on_route_change = on_route_change
    page.go("/")
    page.update()

ft.app(main)
