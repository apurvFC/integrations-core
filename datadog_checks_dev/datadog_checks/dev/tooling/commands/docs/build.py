# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import click

from .... import chdir, run_command
from ...constants import get_root
from ..console import CONTEXT_SETTINGS, abort


@click.command(context_settings=CONTEXT_SETTINGS, short_help='Build documentation')
def build():
    """Build documentation."""
    with chdir(get_root()):
        result = run_command('tox -qqq -e docs build')

    abort(code=result.code)
