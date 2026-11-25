import flet as ft


def main(page: ft.Page):

    # Hello World
    hello_world = ft.Text("Hello World", size=50)

    # カウンター表示用のオブジェクト
    counter = ft.Text("0", size=50, data=0)

    # +ボタンがクリックされた時に呼び出される関数
    def increment_click(e: ft.Event[ft.FloatingActionButton]):
        counter.data += 1
        counter.value = str(counter.data)

    # -ボタンがクリックされた時に呼び出される関数
    def decrement_click(e: ft.Event[ft.FloatingActionButton]):
        counter.data -= 1
        counter.value = str(counter.data)

    # +ボタンを描画エリアに追加
    # page.floating_action_button = ft.FloatingActionButton(icon=ft.Icons.ADD, key="increment", on_click=increment_click)
    plus_button = ft.FloatingActionButton(icon=ft.Icons.ADD, key="increment", on_click=increment_click)
    minus_button = ft.FloatingActionButton(icon=ft.Icons.REMOVE, key="decrement", on_click=decrement_click)

    # コンテンツを描画エリアに追加
    page.add(
        # 実行環境に表示エリアを合わせるためのオブジェクト
        ft.SafeArea(
            expand=True,
            # パーツをまとめるオブジェクト
            content=ft.Container(
                # content=counter,
                content=ft.Column(
                    controls=[
                        hello_world,
                        ft.Row(controls=[minus_button, counter, plus_button], alignment=ft.MainAxisAlignment.CENTER),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                alignment=ft.Alignment.CENTER,
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)