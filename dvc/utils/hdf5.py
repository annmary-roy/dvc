
import h5py

class H5ls:
    def __init__(self):
        # Store an empty list for link names
        self.names = []

    def __call__(self, name, obj):
        for key, val in obj.items():
            p = obj.get(name=key,default=None, getclass=False, getlink=True)
            if (isinstance(p, h5py.ExternalLink)):
                self.names.append(p.filename)

def get_external_links(target):
    h5ls = H5ls()
    h5ls.names.append(target)
    with h5py.File(target,'r') as hdf:
        hdf.visititems(h5ls)
        return set(h5ls.names)

