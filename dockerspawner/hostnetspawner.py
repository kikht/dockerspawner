from dockerspawner import SystemUserSpawner
from tornado.concurrent import Future

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
        #Some weird stuff to satisfy tornado
        res = Future()
        res.set_result(('127.0.0.1', self.jupyter_port))
        res = yield res
        return res[0], res[1]

