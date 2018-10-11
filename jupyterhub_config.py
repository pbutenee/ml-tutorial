c = get_config()

c.JupyterHub.port = 8000

c.Authenticator.admin_users = {'cs'}

c.JupyterHub.log_file = '/var/log/jupyterhub.log'
c.Spawner.notebook_dir = '~/tutorial/'
c.Spawner.default_url='/notebooks/index.ipynb'
