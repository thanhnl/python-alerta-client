
import sys
import click

from .cmd_key import cli as revoke


@click.command('revoke', short_help='revoke API key')
@click.option('--api-key', '-K', required=True)
@click.pass_context
def cli(ctx, api_key):
    ctx.invoke(revoke, delete=api_key)