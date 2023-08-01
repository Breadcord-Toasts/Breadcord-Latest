from __future__ import annotations

from typing import TYPE_CHECKING

from textual import events
from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.screen import ModalScreen
from textual.widgets import Static

if TYPE_CHECKING:
    from rich.traceback import Traceback


class ExceptionModal(ModalScreen):
    def __init__(self, traceback: Traceback):
        super().__init__()
        self.traceback = traceback

    def compose(self) -> ComposeResult:
        yield VerticalScroll(
            Static(self.traceback, id='exception'),
            id='exception_container'
        )

    def on_click(self, event: events.Click) -> None:
        if self.get_widget_at(event.screen_x, event.screen_y)[0] is self:
            self.dismiss()
