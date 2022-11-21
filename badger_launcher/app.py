import json
import badger2040
from badger_ui.base import App
from badger_ui.list import ListWidget

from .menu_item import MenuItem, MenuItemWidget

class MyApp(App):
  def __init__(self):
    super().__init__()

    with open('/launcher.json', 'r') as f:
      launchers = json.load(f)
    self.items = [
      MenuItem(**launcher)
      for launcher in launchers
    ]
    self.child = ListWidget(
        item_height=21,
        item_count=len(self.items),
        item_builder=self.item_builder,
        page_item_count=6,
        selected_index=0,
    )

  def item_builder(self, index: int, selected: bool):
    return MenuItemWidget(
        item=self.items[index],
        selected=selected,
    )
