"""Options for CORDIC algorithm configuration."""

import json
from collections.abc import Callable
from dataclasses import KW_ONLY, asdict, dataclass, field, fields
from typing import Any, Generic, TypeVar

T = TypeVar("T")


@dataclass
class Option(Generic[T]):
    """Class for individual options."""

    name: str
    _: KW_ONLY
    value: T
    doc: str = ""
    validate: Callable[[T], bool] | None = field(
        default=None, repr=False, metadata={"json": False}
    )

    def __post_init__(self) -> None:
        """Validate the option value if a validator is provided."""
        if self.validate is None:
            return
        if not self.validate(self.value):
            msg = f"Invalid value for option '{self.name}': {self.value!r}"
            raise ValueError(msg)

    def make_jsonable(self) -> dict[str, Any]:
        """Convert Option to JSON."""
        self_as_dict = asdict(self)
        for field_object in fields(self):
            if not field_object.metadata.get("json", True):
                # These options, such as `validate`, are not JSON serializable and not
                # too meaningful to export.
                self_as_dict.pop(field_object.name)
        return self_as_dict


available_options: dict[str, Option[Any]] = {
    "save_precomputed": Option(
        name="save_precomputed",
        value=True,
        validate=lambda x: isinstance(x, bool),
        doc="Whether to save precomputed values to disk for future runs.",
    ),
    "max_iters": Option(
        name="max_iters",
        value=50,
        validate=lambda x: isinstance(x, int) and x > 0,
        doc="Maximum number of iterations for the CORDIC algorithm.",
    ),
}


# @dataclass
class OptionsStore:
    """Class for alll the options."""

    options_store: dict[str, Option[Any]] = available_options

    def __repr__(self) -> str:
        """`repr` of OptionsStore."""
        store_pretty_json = json.dumps(
            self.options_store, indent=2, default=Option.make_jsonable
        )
        return f"{self.__class__.__name__}({store_pretty_json})"

    def __getitem__(self, key: str) -> Any:
        """Get the value of an option by name."""
        return self.options_store[key].value

    def __setitem__(self, key: str, value: Any) -> None:
        """Set the value of an option by name, validating it first."""
        # Validate option name
        if key not in self.options_store:
            msg = f"Invalid option name: {key}"
            raise KeyError(msg)

        option = self.options_store[key]

        # Validate option value
        if option.validate is not None and not option.validate(value):
            msg = f"Invalid value for option '{key}': {value}"
            raise ValueError(msg)

        # All good - Set the option value
        self.options_store[key].value = value


options = OptionsStore()
__all__ = ["options"]
