"""events"""
import dataclasses as dc
import enum


class Event:
    pass

@dc.dataclass
class OutOfStock(Event):
    sku: str
