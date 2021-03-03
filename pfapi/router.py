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

import  os
import  threading
import  platform
import  socket
import  psutil
import  multiprocessing
import  datetime

logger = logging.getLogger(__name__)

router = InferringRouter()


@cbv(router)
class hello_router:
    """
    A router for the 'hello' endpoint
    """
    @router.get("/hello/{info}")
    def hello_item(self, info) -> dict:
        d_ret   :   dict    = {}
        b_status:   bool    = False

        if info == 'timestamp':
            str_timeStamp   = datetime.datetime.today().strftime('%Y%m%d%H%M%S.%f')
            d_ret['timestamp']              = {}
            d_ret['timestamp']['now']       = str_timeStamp
            b_status                        = True
        if info == 'sysinfo':
            d_ret['sysinfo']                = {}
            d_ret['sysinfo']['system']      = platform.system()
            d_ret['sysinfo']['machine']     = platform.machine()
            d_ret['sysinfo']['platform']    = platform.platform()
            d_ret['sysinfo']['uname']       = platform.uname()
            d_ret['sysinfo']['version']     = platform.version()
            d_ret['sysinfo']['memory']      = psutil.virtual_memory()
            d_ret['sysinfo']['cpucount']    = multiprocessing.cpu_count()
            d_ret['sysinfo']['loadavg']     = os.getloadavg()
            d_ret['sysinfo']['cpu_percent'] = psutil.cpu_percent()
            d_ret['sysinfo']['hostname']    = socket.gethostname()
            b_status                        = True
        if not b_status:
            d_ret['invalid']                = {}
            d_ret['invalid']['message']     = "Invalid GET. Select timestamp or sysinfo"

        return {
            'status':   b_status,
            'hello':    d_ret
        }


