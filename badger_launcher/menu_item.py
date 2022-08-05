from collections import namedtuple

import badger2040
from badger_ui.base import App, Widget
from badger_ui.util import Offset, Size

class MenuItem:
  name: str

  def __call__(self):
    pass


class MenuItemWidget(Widget):
  def __init__(self, item: MenuItem, selected: bool):
    self.item = item
    self.selected = selected

  def on_button(self, app: App, pressed: dict[int, bool]) -> bool:
    if pressed[badger2040.BUTTON_B]:
      self.item()
      return True

    return super().on_button(app, pressed)

  def render(self, app: 'App', size: Size, offset: Offset):
    app.display.pen(0)
    if self.selected:
      app.display.rectangle(
          offset.x,
          offset.y,
          size.width,
          size.height,
      )
      app.display.pen(15)
    app.display.thickness(2)
    app.display.text(
        self.item.name,
        offset.x + 2,
        offset.y + (size.height // 2),
        0.8,
    )
