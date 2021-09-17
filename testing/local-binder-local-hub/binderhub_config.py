######################################################################
## A development config to test BinderHub locally.
#
# If you are running BidnerHub manually (not via JupyterHub) run
# `python -m binderhub -f binderhub_config.py`

# Optionally override the external access URL for JupyterHub
JUPYTERHUB_EXTERNAL_URL = None

# Host IP is needed in a few places
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
hostip = s.getsockname()[0]
s.close()

from binderhub.build_local import LocalRepo2dockerBuild
import os


c.BinderHub.debug = True
c.BinderHub.use_registry = False
c.BinderHub.builder_required = False

c.BinderHub.build_class = LocalRepo2dockerBuild
c.BinderHub.push_secret = None

c.BinderHub.about_message = "This is a local dev deployment without Kubernetes"
c.BinderHub.banner_message = 'See <a href="https://github.com/jupyterhub/binderhub">BinderHub on GitHub</a>'

c.BinderHub.hub_url_local = 'http://localhost:8000'

# Are we running as a managed JupyterHub service?
if os.getenv('JUPYTERHUB_SERVICE_PREFIX'):
    c.BinderHub.base_url = os.getenv('JUPYTERHUB_SERVICE_PREFIX')
    # JUPYTERHUB_BASE_URL may not include the host
    # c.BinderHub.hub_url = os.getenv('JUPYTERHUB_BASE_URL')
    c.BinderHub.hub_url = JUPYTERHUB_EXTERNAL_URL or f'http://{hostip}:8000'
else:
    c.BinderHub.hub_url = JUPYTERHUB_EXTERNAL_URL or f'http://{hostip}:8000'
