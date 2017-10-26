import os

def resolve_runfile(path):
  if os.getenv('RUNFILES_MANIFEST_ONLY') != "1":
    return os.path.join(os.environ['TEST_SRCDIR'], path)

  manifest = os.getenv('RUNFILES_MANIFEST_FILE')
  with open(manifest) as f:
    for line in f.readlines():
      if line.split()[0] == path:
        return line.split()[1]
  raise "Cannot find %s in manifest %s" % (path, manifest)
