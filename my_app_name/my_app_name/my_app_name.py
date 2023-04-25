import pynecone as pc

class State(pc.State):
  count: int = 0

  # 이벤트 핸들러를 정의합니다.
  def increment(self):
    self.count += 1

  # 이벤트 핸들러를 정의합니다.
  def decrement(self):
    self.count -= 1

# 앱의 프론트엔드를 정의합니다.
def index():
  return pc.hstack(
    pc.button("Decrement", color_scheme="red", boarder_radius="1em", on_click=State.decrement,),
    pc.heading(State.count, size="2em"),
    pc.button("Increment", color_scheme="green", boarder_radius="1em", on_click=State.increment,),
    pc.text("Hello World!", color="blue", font_size="1.5em"),
  )
def about():
  return pc.text("About Page")

# 앱을 실행합니다. 
app = pc.App(state=State) # 앱 생성
app.add_page(index, route="/") # 페이지 추가
app.add_page(about, route="/about") # 페이지 추가
app.compile() # 컴파일