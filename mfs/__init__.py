import os
from django.conf import settings
from .utils import utils
# from .core  import *

FSDIR = None;
FSURL = None;

if not hasattr(settings, 'FSDIR'):
    FSDIR = os.path.join(settings.BASE_DIR, "fsdir");
    if not os.path.isdir(FSDIR):
        os.mkdir(FSDIR);
        utils.printsucc("{} is created.".format(FSDIR));
else:
    FSDIR = settings.FSDIR;

if not hasattr(settings, 'FSURL'):
    FSURL = "/file/";
else:
    FSURL = settings.FSURL;

