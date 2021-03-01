
from __future__         import annotations

from typing             import Optional
from os                 import path, environ, getenv
from yaml               import safe_load
from argparse           import Namespace, ArgumentParser
from importlib.metadata import metadata
import                  pudb
import                  sys
program_info = metadata(__package__)

CONFIG_FILE = path.join(environ['HOME'], '.config', 'fnndsc', 'pfapi.yml')
CONFIG_FILE = getenv('PFAPI_CONFIG_FILE', CONFIG_FILE)

class PFapiCLIinfo:

    str_description = """
    This class is responsible for the defining the info CLI flags
    """

    def __init__(self, parser: ArgumentParser):

        parser.add_argument(
            '--version',
            action  = 'store_true',
            dest    = 'b_version',
            help    = 'if specified, print version number.',
            default = False
        )
        parser.add_argument(
            '--verbosity',
            action  = 'store',
            dest    = 'verbosity',
            default = '0',
            help    = 'program verbosity'
        )
        args        = parser.parse_args()
        self.args   = Namespace(
                        b_version   = args.b_version,
                        verbosity   = args.verbosity
                    )
        if self.args.b_version:
            print(f'%(prog)s {program_info["version"]}')
            sys.exit(0)

class PFapiCLICore:

    str_description = """
    This class is responsible for the defining the core CLI flags
    """

    def __init__(self, parser: ArgumentParser):

        parser.add_argument(
            '--ipSelf',
            action  = 'store',
            dest    = 'ipSelf',
            default = 'localhost',
            help    = 'IP to connect.'
        )
        parser.add_argument(
            '--portSelf',
            action  = 'store',
            dest    = 'portSelf',
            default = '4055',
            help    = 'Port to use.'
        )
        args        = parser.parse_args()
        self.args   = Namespace(
                        ipSelf      = args.ipSelf,
                        portSelf    = args.portSelf
                    )


class PFapiCLISwift:

    str_description = """
    This class is responsible for the defining the swift CLI flags
    """

    def __init__(self, parser: ArgumentParser):

        parser.add_argument(
            '--ipSwift',
            action  = 'store',
            dest    = 'ipSwift',
            default = 'localhost',
            help    = 'IP to connect.'
        )
        parser.add_argument(
            '--portSwift',
            action  = 'store',
            dest    = 'portSwift',
            default = '8080',
            help    = 'Port to use.'
        )

        args        = parser.parse_args()
        self.args   = Namespace(
                        ipSwift     = args.ipSwift,
                        portSwift   = args.portSwift
                    )

def CLIinfo_get() -> PFapiCLICore:
    custom_config = {}
    if path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            custom_config = safe_load(''.join(f.readlines()))
    return PFapiCLIinfo(**custom_config)

def CLICore_get() -> PFapiCLICore:
    custom_config = {}
    if path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            custom_config = safe_load(''.join(f.readlines()))
    return PFapiCLICore(**custom_config)

def CLISwift_get() -> PFapiCLISwift:
    custom_config = {}
    if path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            custom_config = safe_load(''.join(f.readlines()))
    return PFapiCLICore(**custom_config)
