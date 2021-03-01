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

from .cli import PFapiCLICore
from .cli import PFapiCLISwift

logger = logging.getLogger(__name__)

class API:
    """
    The core class of this project. This really provides only
    the base machinery for a fastapi system.
    """

    def __init__(   self,
                    CLIcore :   PFapiCLICore,
                    CLIswift:   PFapiCLISwift):

        self.args   = Namespace(**vars(CLIcore.args), **vars(CLIswift.args))
        self.app    = FastAPI()
        self.router = InferringRouter()
        self.app.include_router(router)

@cbv(router)
class hello_router:
    """
    A router for the 'hello' endpoint
    """
    @router.get("/hello")
    def hello_item(self):
        return {'message': 'Hello, world!'}

class GuessingException(Exception):
    """
    For when we can't detect something about the system we need to know.
    """
    pass

