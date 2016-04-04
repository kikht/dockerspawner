from dockerspawner import SystemUserSpawner

class HostNetSpawner(SystemUserSpawner):

    use_internal_ip = True

    @property 
    def jupyter_port(self):
        return 30000 + self.user_id

    def get_env(self):
        env = super(HostNetSpawner, self).get_env()
        env.update(dict(JPY_PORT=self.jupyter_port))
        return env

    def get_ip_and_port(self):
        return '127.0.0.1', self.jupyter_port
