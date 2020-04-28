from flask.json import JSONEncoder
import numpy as np

class CustomJSONEncoder(JSONEncoder):
    # override
    def __init__(self, **kwargs):
        kwargs['ensure_ascii'] = False
        super(CustomJSONEncoder, self).__init__(**kwargs)
    def default(self, obj):
        try:
            if isinstance(obj, np.integer):
                return int(obj)
            if isinstance(obj, np.float):
                return int(obj)
            return str(obj).encode('utf-8')
        except TypeError:
            pass
        return super(CustomJSONEncoder, self).default(obj)