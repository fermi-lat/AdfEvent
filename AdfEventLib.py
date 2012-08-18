# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/AdfEvent/AdfEventLib.py,v 1.2 2008/11/07 16:03:00 ecephas Exp $
def generate(env, **kw):
    if not kw.get('depsOnly', 0):
        env.Tool('addLibrary', library = ['AdfEvent'])
        if env['PLATFORM'] == "win32" and env.get('CONTAINERNAME','') == 'GlastRelease':
            env.Tool('findPkgPath', package = 'AdfEvent') 

    env.Tool('facilitiesLib')
    env.Tool('addLibrary', library = env['gaudiLibs'])
    #  no need for incsOnly section since no other pkgs are referenced
def exists(env):
    return 1;

