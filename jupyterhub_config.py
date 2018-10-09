c = get_config()

c.JupyterHub.port = 80

c.Authenticator.admin_users = {'cs'}

c.JupyterHub.log_file = '/var/log/jupyterhub.log'
c.Spawner.notebook_dir = '~/tutorial'
c.Spawner.args = ['--NotebookApp.default_url=notebooks/release/1/index.ipynb']

