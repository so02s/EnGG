# src\web\study_view\ui_elements\study_cards.py
import flet as ft
from domain import Rating

# TODO вынести в отдельный класс стилей
BG_COLOR = ft.Colors.GREEN_600

class CardStyle(ft.Container):
    def __init__(self, title: str):
        super().__init__()
        self.border_radius = 10
        self.bgcolor = BG_COLOR
        self.height = 200
        self.width = 200
        self.align = ft.Alignment.CENTER
        self.animate_offset=ft.Animation(
            400,
            ft.AnimationCurve.DECELERATE
        )
        self.content = ft.Text(
            title,
            size=20,
            weight=ft.FontWeight.BOLD,
            align=ft.Alignment.CENTER
        )

class GestureCard(ft.GestureDetector):
    def __init__(self, content, on_swipe = None):
        super().__init__()
        self.on_swipe = on_swipe
        self.content = content
        self.mouse_cursor = ft.MouseCursor.MOVE
        self.drag_interval = 10
        self.threshold = 0.1
        self._start_offset = ft.Offset()
        self.on_pan_start = self.handle_pan_start
        self.on_pan_update = self.handle_pan_update
        self.on_pan_end = self.handle_pan_end

    def handle_pan_start(self, e: ft.DragStartEvent):
        self._start_offset = self.content.offset or ft.Offset()
        # self.content.animate_offset = None
        self.content.update()

    def handle_pan_update(self, e: ft.DragUpdateEvent):
        print(self.content.offset)
        print('e',e.local_delta)
        self.content.offset = ft.Offset(
            self._start_offset.x + e.local_delta.x,
            self._start_offset.y + e.local_delta.y
        )
        print(self.content.offset)
        self.content.update()
    
    def handle_pan_end(self, e: ft.DragEndEvent):
        offset = self.content.offset
        if offset is None:
            return
        # print(self.content.offset)
        dx, dy = offset.x, offset.y

        if abs(dx) > self.threshold:
            rating = Rating.GOOD if dx > 0 else Rating.BAD
        elif abs(dy) > self.threshold:
            rating = Rating.NEUTRAL if dy > 0 else None
        else:
            rating = None

        if rating is not None:
            self.on_swipe(rating)
        else:
            self.content.offset = ft.Offset()
            self.content.update()