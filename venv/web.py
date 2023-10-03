import flet as ft
import sqlite3

def create_db():
    db = sqlite3.connect("webpage.db", check_same_thread=False)
    cur = db.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS webpage(
        id INTEGER primary key,
        title VARCHAR,
        subtitle VARCHAR,
        text TEXT
        )
        """
    )



def main(page: ft.page):
    page.title = "دفترچه تلفن"
    page.bgcolor="#8f8f8f"
    page.window_width = 800
    page.scroll = True

########## UP MENU APP BAR
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()
        
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("AppBar Example"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )

#################### NAV BAR DOWN
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Admin"),
            ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Client"),
            ft.NavigationDestination(icon=ft.icons.BOOKMARK_BORDER,selected_icon=ft.icons.BOOKMARK,label="Explore",
            ),
        ]
    )


    # page.add(navigation_bar)
    page.update()

ft.app(target=main)