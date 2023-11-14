"""
Return config on servers to start for bokeh
See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import sys

serverfile = os.path.join(os.path.dirname(__file__), "server.py")


def launch_server():
    return {"command": [sys.executable, serverfile, "{port}"], "timeout": 20, "launcher_entry": {"enabled": False}}


try:
    from ._version import __version__
except ImportError:
    # Fallback when using the package in dev mode without installing
    # in editable mode with pip. It is highly recommended to install
    # the package from a stable release or in editable mode: https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs
    import warnings

    warnings.warn("Importing 'jupyterlab_nvdashboard' outside a proper installation.")
    __version__ = "dev"


def _jupyter_labextension_paths():
    return [{
        "src": "labextension",
        "dest": "jupyterlab-nvdashboard"
    }]
