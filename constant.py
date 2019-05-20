import git

GITBASE = git.Repo('.', search_parent_directories=True).working_tree_dir
BASEDIR = "{}".format(GITBASE)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

REPORT_KEYS_FPATH = '{}/reports/report_keys.txt'.format(BASEDIR)
REPORT_KEYS_FNAME = 'report_keystats.txt'
