import badger2040
from badger_ui.base import App
from badger_ui.list import ListWidget

from .menu_item import MenuItem, MenuItemWidget


class ArkhamHorrorLCG(MenuItem):
  name = 'Arkham Horror LCG'

  def __call__(self):
    import ahlcg2040
    ahlcg2040.start()


class Netrunner(MenuItem):
  name = 'Android: Netrunner'

  def __call__(self):
    import netrunner2040
    netrunner2040.start()


class LordOfTheRignsLCG(MenuItem):
  name = 'Lord of the Rings LCG'

  def __call__(self):
    import lotrlcg2040
    lotrlcg2040.start()


class Mahjong(MenuItem):
  name = 'Mahjong'

  def __call__(self):
    import mahjong2040.client
    mahjong2040.client.start()


class Blaseball(MenuItem):
  name = 'Blaseball'

  def __call__(self):
    import blaseball2040
    blaseball2040.start()


class MyApp(App):
  def __init__(self):
    super().__init__()

    self.items = [
        ArkhamHorrorLCG(),
        Netrunner(),
        LordOfTheRignsLCG(),
        Mahjong(),
        Blaseball(),
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
