import flet as ft
import requests

input_field = ft.TextField(hint_text='Add task ...')

def main(page: ft.Page):
    def get(e):
        api_request = requests.get('http://127.0.0.1:8000/app/').json()
        
        for tasks in range(len(api_request)):
            page.add(ft.Text(api_request[tasks]['task']))
            
        page.update()

    def post(e):
        requests.post('http://127.0.0.1:8000/app/', data={'task': str(input_field.value)})
    
    page.add(
        ft.Column(
            controls=[
                input_field,
                ft.FloatingActionButton(icon=ft.icons.ADD, on_click=post),
                ft.FloatingActionButton(icon=ft.icons.TRACK_CHANGES, on_click=get)

            ]
        )
    )


if __name__ == '__main__':
    ft.app(target=main)