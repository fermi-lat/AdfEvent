# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/AdfEvent/AdfEventLib.py,v 1.1 2008/08/15 21:42:32 ecephas Exp $
def generate(env, **kw):
    if not kw.get('depsOnly', 0):
        env.Tool('addLibrary', library = ['AdfEvent'])
    env.Tool('facilitiesLib')
    env.Tool('addLibrary', library = env['gaudiLibs'])
def exists(env):
    return 1;

