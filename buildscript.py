import os
from subprocess import call
from distutils.dir_util import copy_tree

import redash_stmo

# Copy JS extensions into components
redashSTMOPath = os.path.split(redash_stmo.__file__)[0]
jsExtensionPath = os.path.realpath(os.path.join(redashSTMOPath, 'js'))
copy_tree(jsExtensionPath, './client/app/components/')

call("npm run build", shell=True)
