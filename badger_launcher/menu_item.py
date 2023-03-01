import sys

import badger2040w
from badger_ui.base import App, Widget
from badger_ui.util import Offset, Size

class MenuItem:
  name: str
  module: str
  callable: str
  args: []
  kwargs: {}

  def __init__(self, name, module, callable=None, args=None, kwargs=None):
    self.name = name
    self.module = module
    self.callable = callable
    self.args = [] if args is None else args
    self.kwargs = {} if kwargs is None else kwargs

  def __call__(self):
    module = __import__(self.module)
    if self.callable:
      for _callable in self.callable.split('.'):
        module = getattr(module, _callable)
      module(*self.args, **self.kwargs)


class MenuItemWidget(Widget):
  def __init__(self, item: MenuItem, selected: bool):
    self.item = item
    self.selected = selected

  def on_button(self, app: App, pressed: dict[int, bool]) -> bool:
    if pressed[badger2040w.BUTTON_B]:
      self.item()
      return True

    return super().on_button(app, pressed)

  def render(self, app: 'App', size: Size, offset: Offset):
    app.display.set_pen(0)
    if self.selected:
      app.display.rectangle(
          offset.x,
          offset.y,
          size.width,
          size.height,
      )
      app.display.set_pen(15)
    app.display.set_font('sans')
    app.display.set_thickness(2)
    app.display.text(
        self.item.name,
        offset.x + 2,
        offset.y + (size.height // 2),
        scale=0.8,
    )
