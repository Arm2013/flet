import flet as ft
import sqlite3

db = sqlite3.connect("phonebook.db", check_same_thread=False)
cur = db.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS phonebook(
    id INTEGER primary key,
    name VARCHAR,
    number VARCHAR
    )
    """
)

#  Class
class phone(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.name = ft.TextField(label="نام را وارد کنید", color="#FFFFFF")
        self.number = ft.TextField(label="شماره را وارد کنید", color="#FFFFFF")
        self.allnumbers = ft.Column()

    def delete(self, e):
        print(e.control.title.value)
        name = e.control.title.value
        cur.execute("DELETE FROM phonebook WHERE name=?", (name,))
        db.commit()
        self.allnumbers.controls.clear()
        self.show_all()
        self.page.update()

    def show_all(self):
        data = cur.execute("SELECT * FROM phonebook")
        for item in data:
            self.allnumbers.controls.append(
                ft.ListTile(
                    title=ft.Text(value=item[1]),
                    subtitle=ft.Text(value=item[2]),
                    on_click=self.delete
                    )
                )
            self.update()

    def show_last(self):
        data = cur.execute("SELECT * FROM phonebook ORDER BY id DESC LIMIT 1")
        item = data.fetchall()
        print(item)
        # self.allnumbers.controls.append(
        #     ft.ListTile(
        #         title=ft.Text(value=item[1]),
        #         subtitle=ft.Text(value=item[2])
        #         )
        #     )
        # self.update()

# Ejraye show all aval shoru barnameh
    def did_mount(self):
        self.show_all()

    def addnumber(self,e):
        query = "INSERT INTO phonebook (name, number) values(?,?)"
        vals = (self.name.value, self.number.value)
        cur.execute(query, vals)
        db.commit()
        # self.show_last()
        self.name.value=""
        self.number.value=""
        self.allnumbers.controls.clear()

        self.page.update()
        self.show_all()
        print("added to db")


    def build(self):
        return ft.Column(
            [
                self.name, self.number,
                ft.ElevatedButton(
                    text="اضافه کردن", bgcolor = "#FFFFFF", color="#fa7373", on_click=self.addnumber
                ),
                self.allnumbers
            ]
        )



#  main
def main(page: ft.page):
    page.title = "دفترچه تلفن"
    page.bgcolor="#8f8f8f"
    page.window_height = 600
    page.window_width = 400
    page.scroll = True

    phone1 = phone()

    page.add(phone1)

    page.update()

ft.app(target=main,view=ft.AppView.WEB_BROWSER, port=8550)