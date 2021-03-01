#
# __main__.py
#
# "Main" entry point -- essentially this is responsible for
# parsing any CLI and firing up the code "API" object.
#

import  argparse
import  sys
import  pudb
from    importlib.metadata  import  metadata
import  pkg_resources

from    .cli                import  PFapiCLICore,PFapiCLISwift,PFapiCLIinfo
from    .api                import  API

program_info    = metadata(__package__)

def main() -> None:

    parser          = argparse.ArgumentParser(
                        description = program_info['summary']
                    )

    CLIinfo         = PFapiCLIinfo(parser)
    CLICore         = PFapiCLICore(parser)
    CLISwift        = PFapiCLISwift(parser)

    # pudb.set_trace()
    fAPI    = API(CLICore, CLISwift)


if __name__ == '__main__':
    main()
