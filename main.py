from db import main_db
import flet as ft

def main(page: ft.Page):
    page.title = "list_of_purchases"
    page.theme_mode = ft.ThemeMode.DARK

    item_list = ft.Column()

    def load_item():
            item_list.controls.clear()
            for item_id, item_text, is_bought in main_db.get_items():
                item_list.controls.append(create_item_row(item_id=item_id,
                                                        item_text=item_text,
                                                        is_bought=is_bought
                                                        ))

            page.update()

    def create_item_row(item_id, item_text,is_bought):
            item_field = ft.TextField(value=item_text ,read_only=True, expand=True)
            
            checkbox = ft.Checkbox(value=bool(is_bought),
                        on_change=lambda e: toggle_item(item_id, e.control.value))

            def save_button(_):
                main_db.update_items(item_id=item_id, new_item=item_field.value)
                page.update()

            def delete_item(_):
                main_db.delete_items(item_id=item_id)
                
                load_item()
            
            delete_item = ft.IconButton(icon=ft.Icons.DELETE,on_click=delete_item)
            save_button = ft.IconButton(icon=ft.Icons.SAVE,on_click=save_button)
            return ft.Row([checkbox,item_field,save_button,delete_item])

    def add_item(_):
        if item_input.value:
            item = item_input.value
            item_id = main_db.add_item(item)
            item_list.controls.append(create_item_row(item_id=item_id, item_text=item,is_bought=None))
            item_input.value = ""
            page.update()

    def toggle_item(item_id, bought):
        main_db.update_items(item_id,is_bought=int(bought))
        load_item()

    item_input = ft.TextField(label="Enter ur product to buy",expand=True)
    add_button = ft.ElevatedButton("ADD",ft.Icons.ADD,on_click=add_item,height=80,width=100)

    page.add(ft.Row([item_input,add_button]), item_list)   

    load_item()  

if __name__ == "__main__":
    main_db.init_db()
    ft.app(target=main)