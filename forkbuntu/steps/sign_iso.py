from ..step import Step
from munch import munchify
from os import path

class SignIso(Step):
    messages = munchify({
        'past': 'signed iso',
        'present': 'signing iso',
        'cache': 'using signed iso cache'
    })
    requires = [
        'configure_filesystem'
    ]

    def __init__(self, name, app):
        super().__init__(name, app)
        c = app.conf
        self.checksum_paths = [path.join(c.paths.iso)]

    def run(self):
        s = self.app.services
        s.configure.sign_iso()
