# Configuration file for jupyterhub.

c = get_config()  #noqa


c.JupyterHub.load_groups = {

		'formgrade-test': ['grader'],
		'nbgrader-test': []
		





	}



c.JupyterHub.load_roles = [






		{
			'name': 'nbgrader_token_role',
			'scopes': ['read:users:groups', 'list:services',
			'groups', 'admin:users'],
			'services': ['nbgrader_token_service']
		}
	]


c.JupyterHub.services = [










		{
			'name': 'nbgrader_token_service',
			'api_token': '8e81894080964fb59c5c03cc70ae7d14'
		}
	]



# c.Spawner.default_url = ''


c.Spawner.environment = {'JUPYTERHUB_API_TOKEN_CUSTOM': '8e81894080964fb59c5c03cc70ae7d14'}


c.Authenticator.admin_users = {'vuswh'}



c.Authenticator.allowed_users = {'grader'}





