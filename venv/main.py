import flet as ft

def main(page: ft.Page):

    page.title = "MY CALC"
    page.window_width = 350
    page.window_height = 340
    page.window_resizable = False
    page.window_maximizable = False
    page.bgcolor = "#5f5f5f"

    txt_typ = "0"
    txt_res = "0"


# Add number
    def ad_num(e):
        comma = lbl_monitor.value.find(".")
        if comma != -1:
            lbl_monitor.value = str(lbl_monitor.value.rsplit("0")[0])

        if (float(lbl_monitor.value) == 0):
            lbl_monitor.value = str(e.control.data)
            print(str(lbl_monitor.value))
            page.update()
        else:
            lbl_monitor.value = str(lbl_monitor.value) + str(e.control.data)
            print(str(lbl_monitor.value))
            page.update()

#add comma
    def comma(e):
        comma = lbl_monitor.value.find(".")
        if comma == -1:
            lbl_monitor.value = str(lbl_monitor.value) + str(e.control.data) + "0"
            print(str(lbl_monitor.value))
            page.update()
        else:
            print("comma")

# clr
    def b_clear(e):
        lbl_monitor.value = "0"
        page.update()

# add operation
    def protcent(e):
        lbl_monitor.value = str(float(lbl_monitor.value)/100)
        page.update()

# add operation
    def click(e):
        print(e.control.text)

    # style = ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE | ft.TextDecoration.OVERLINE,
    #                      font_family="/fonts/hesab.ttf")

    lbl_monitor = ft.TextField(value=str(txt_res), bgcolor="#f8f8f8", color="080808")
    # lbl_monitor.value="34656"
    btn_protcent = ft.ElevatedButton(text="%",data="",on_click=protcent)
    btn_stepen = ft.ElevatedButton(text="x2",data="",on_click=click)
    btn_clr = ft.ElevatedButton(text="Clr",data="",on_click=b_clear)
    btn_bsp = ft.ElevatedButton(text="<-",data="",on_click=click)
    row0 = ft.Row(controls=[btn_protcent,btn_stepen,btn_clr,btn_bsp],
                  alignment=ft.MainAxisAlignment.SPACE_AROUND)
    btn_7 = ft.ElevatedButton(text="7",data="7",on_click=ad_num)
    btn_8 = ft.ElevatedButton(text="8",data="8",on_click=ad_num)
    btn_9 = ft.ElevatedButton(text="9",data="9",on_click=ad_num)
    btn_zarb = ft.ElevatedButton(text="*",data="",on_click=click)
    row1 = ft.Row(controls=[btn_7,btn_8,btn_9,btn_zarb],
                  alignment=ft.MainAxisAlignment.SPACE_AROUND)
    btn_4 = ft.ElevatedButton(text="4",data="4",on_click=ad_num)
    btn_5 = ft.ElevatedButton(text="5",data="5",on_click=ad_num)
    btn_6 = ft.ElevatedButton(text="6",data="6",on_click=ad_num)
    btn_menha = ft.ElevatedButton(text="-",data="",on_click=click)
    row2 = ft.Row(controls=[btn_4,btn_5,btn_6,btn_menha],
                  alignment=ft.MainAxisAlignment.SPACE_AROUND)
    btn_1 = ft.ElevatedButton(text="1",data="1",on_click=ad_num)
    btn_2 = ft.ElevatedButton(text="2",data="2",on_click=ad_num)
    btn_3 = ft.ElevatedButton(text="3",data="3",on_click=ad_num)
    btn_jam = ft.ElevatedButton(text="+",data="+",on_click=click)
    row3 = ft.Row(controls=[btn_1,btn_2,btn_3,btn_jam],
                  alignment=ft.MainAxisAlignment.SPACE_AROUND)
    btn_manfi = ft.ElevatedButton(text="+/-",data="",on_click=click)
    btn_0 = ft.ElevatedButton(text="0",data="0",on_click=ad_num)
    btn_momayez = ft.ElevatedButton(text=".",data=".",on_click=comma)
    btn_mosavi = ft.ElevatedButton(text="=",data="",on_click=click)
    row4 = ft.Row(controls=[btn_manfi,btn_0,btn_momayez,btn_mosavi],
                  alignment=ft.MainAxisAlignment.SPACE_AROUND)

    page.add(lbl_monitor,row0,row1,row2,row3,row4)


    page.update()
ft.app(target=main)
