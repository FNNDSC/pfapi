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
from    .api                            import API

logger = logging.getLogger(__name__)


@cbv(API.router)
class hello_router:
    """
    A router for the 'hello' endpoint
    """
    @router.get("/hello")
    def hello_item(self):
        return {'message': 'Hello, world!'}


