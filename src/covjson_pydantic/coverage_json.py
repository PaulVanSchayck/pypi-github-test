from typing import Literal
from typing import Optional

from .my_base_model import MyBaseModel


class CoverageJson(MyBaseModel):
    id: Optional[str]
    type: Literal["Coverage"] = "Coverage"
