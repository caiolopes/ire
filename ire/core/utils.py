from typing import Any
from importlib import import_module


def get_class(path: str) -> Any:
    # grab the classname off of the backend string
    package, klass = path.rsplit(".", 1)

    # dynamically import the module, in this case app.backends.adapter_a
    module = import_module(package)

    # pull the class off the module and return
    return getattr(module, klass)
