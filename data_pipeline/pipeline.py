"""Pipeline core."""

from typing import Any, Callable, List

class Pipeline:
    def __init__(self, source=None, transforms=None, sink=None):
        self.source = source
        self.transforms = transforms or []
        self.sink = sink
    
    def run(self):
        data = self.source.read()
        for transform in self.transforms:
            data = transform(data)
        self.sink.write(data)
