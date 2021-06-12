
import subprocess
import pwd

c = get_config()
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 8000
c.NotebookApp.open_browser = False
c.FileContentsManager.delete_to_trash = False

def pre_spawn_hook(spawner):
    username = spawner.user.name
    try:
        pwd.getpwnam(username)
    except KeyError:
        subprocess.check_call(['useradd', '-ms', '/bin/bash', username])

c.Spawner.pre_spawn_hook = pre_spawn_hook
c.Spawner.default_url='/lab'

c.JupyterHub.authenticator_class = 'nativeauthenticator.NativeAuthenticator'
c.Authenticator.minimum_password_length = 4
c.Authenticator.admin_users = {'admin'}
c.Authenticator.allowed_users = {'admin'}
c.Authenticator.open_signup = True
c.LocalAuthenticator.create_system_users = True
c.Authenticator.allowed_failed_logins = 3
c.Authenticator.seconds_before_next_try = 30
c.Authenticator.ask_email_on_signup = True
c.DummyAuthenticator.password = "admin"