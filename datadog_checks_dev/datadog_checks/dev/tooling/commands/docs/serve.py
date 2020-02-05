# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import subprocess
import webbrowser
from contextlib import suppress

import click

from ....utils import chdir
from ...constants import get_root
from ..console import CONTEXT_SETTINGS, abort


@click.command(context_settings=CONTEXT_SETTINGS, short_help='Serve and view documentation in a web browser')
@click.option('--no-open', '-n', is_flag=True, help='Do not open the documentation in a web browser')
def serve(no_open):
    """Serve and view documentation in a web browser."""
    with chdir(get_root()):
        process = subprocess.Popen(['tox', '-qqq', '-e', 'docs', 'serve'])

    if not no_open:
        webbrowser.open_new_tab('http://localhost:8000')

    try:
        process.wait()
    except KeyboardInterrupt:
        with suppress(OSError):
            process.terminate()
            process.wait()

    abort(code=process.returncode)
