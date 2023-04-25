"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    
    value : int

    text: str = "Hello World"
    color: str = "red"

    def flip_color(self):
        if self.color == "red":
            self.color = "blue"
        else:
            self.color = "red"


    

def index() -> pc.Component:
    return pc.center(                   # 중앙 정렬
        pc.vstack(                      # 수직 정렬
            pc.hstack(                  # 수평 정렬
                pc.circular_progress(
                    pc.circular_progress_label("50", color="green"),
                    value=50,
                ),
                pc.circular_progress(
                    pc.circular_progress_label(
                        "∞", color="rgb(107,99,246)"
                    ),
                    is_indeterminate=True,
                ),
            ),
            # 텍스트 추가 및 색상 변경
            pc.text("김기태 Hello World! 123", color="blue", font_size="1.5em"),
            pc.text("김기태 Hello World! 123", color="black", font_size="1.5em"),

            # 버튼 추가
            pc.avatar(
                name="Ki Tae Kim",
            ),

            # 박스 추가
            pc.box("박스 부분 : 파일명 ", pc.code(filename, font_size="1em")),

            # 버튼 추가 
            pc.button(
                "Fancy Button",
                border_radius="1em",
                box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
                box_sizing="border-box",
                color="white",
                _hover={
                    "opacity": 0.85,
                },
            ),            
            pc.badge(
                State.text,
                color_scheme=State.color,
                on_click=State.flip_color,
                font_size="1.5em",
                _hover={
                    "cursor": "pointer",
                },
            ),
            pc.slider(
                on_change_end=State.set_value,
                color_scheme=pc.cond(
                    State.value > 50, "green", "pink"
                ),
            ),
            spacing="1.2em",
        ),
    )

def about():
    return pc.text("About Page")

# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index, route="/")
app.add_page(about, route="/about")
app.compile()
