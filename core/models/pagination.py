from dataclasses import dataclass
from typing import Optional


@dataclass
class Pagination:
    search: Optional[str]
    limit: Optional[int]
    offset: Optional[int]

