c = get_config()

c.JupyterHub.port = 80
# c.Authenticator.create_system_users = True
# c.Authenticator.admin_users = {'cs'}

# c.JupyterHub.log_file = '/var/log/jupyterhub.log'
c.Spawner.notebook_dir = '~/tutorial/'
c.Spawner.default_url = '/notebooks/index.ipynb'
