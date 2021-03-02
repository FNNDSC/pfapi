import  typing
from    collections.abc                 import Iterable
import  abc
import  logging
import  json
from    shutil                          import which
from    subprocess                      import check_output
from    argparse                        import ArgumentParser, Namespace

from    fastapi                         import Depends, FastAPI, Header, HTTPException
from    fastapi_utils.api_model         import APIMessage, APIModel
from    fastapi_utils.cbv               import cbv
from    fastapi_utils.guid_type         import GUID
from    fastapi_utils.inferring_router  import InferringRouter

from    .cli                            import PFapiCLICore
from    .cli                            import PFapiCLISwift

import  pudb

logger = logging.getLogger(__name__)

class API:
    """
    The core class of this project. This really provides only
    the base machinery for a fastapi system.
    """

    app             = FastAPI()
    router          = InferringRouter()
    app.include_router(router)

    def __init__(   self,
                    CLIcore :   PFapiCLICore,
                    CLIswift:   PFapiCLISwift):

        # pudb.set_trace()
        self.args   = Namespace(**vars(CLIcore.args), **vars(CLIswift.args))
