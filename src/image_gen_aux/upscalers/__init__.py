from typing import TYPE_CHECKING

from ..utils import IMAGE_AUX_SLOW_IMPORT, OptionalDependencyNotAvailable, _LazyModule, is_torch_available


_import_structure = {}

try:
    if not (is_torch_available()):
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    ...
else:
    _import_structure["upscale_with_model"] = [
        "UpscaleWithModel",
    ]

if TYPE_CHECKING or IMAGE_AUX_SLOW_IMPORT:
    try:
        if not is_torch_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        ...
    else:
        from .upscale_with_model import (
            UpscaleWithModel,
        )
else:
    import sys

    sys.modules[__name__] = _LazyModule(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
    )