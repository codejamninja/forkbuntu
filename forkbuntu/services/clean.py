from cfoundation import Service
import shutil

class Clean(Service):
    def tmp(self):
        c = self.app.conf
        shutil.rmtree(c.paths.tmp)

    def nuke(self):
        shutil.rmtree(path.join(c.paths.cwd, '.tmp'))
