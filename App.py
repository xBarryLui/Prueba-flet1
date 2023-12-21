import flet as ft
from flet import *

def main(page):
    
    first_name = ft.TextField(label="First name", autofocus=True)
    last_name = ft.TextField(label="Last name")
    greetings = ft.Column()

    def btn_click(e):
        greetings.controls.append(ft.Text(f"HOLIWI, {first_name.value} {last_name.value}!"))
        first_name.value = ""
        last_name.value = ""
        page.update()
        first_name.focus()

    row_f1 = ft.Row(
                    controls= [first_name,last_name,ft.ElevatedButton(text="HOLA PERRO",on_click=btn_click,bgcolor="blue"),greetings],
                   alignment=ft.MainAxisAlignment.END
                )
    greetings.bgcolor = "red"
    page.bgcolor="green"
    page.add(row_f1)
    

ft.app(target=main,view=WEB_BROWSER)