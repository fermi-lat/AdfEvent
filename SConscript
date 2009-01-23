# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/AdfEvent/SConscript,v 1.2 2008/11/07 16:01:53 ecephas Exp $
# Authors: N.Omodei <nicola.omodei@pi.infn.it>
# Version: AdfEvent-00-05-01
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()
libEnv = baseEnv.Clone()

libEnv.Tool('AdfEventLib',depsOnly=1)
AdfEvent = libEnv.StaticLibrary('AdfEvent',listFiles(['src/*.cxx']))

progEnv.Tool('AdfEventLib')
test_AdfEvent = progEnv.Program('test_AdfEvent', ['src/test/testMain.cxx'])

progEnv.Tool('registerObjects', package = 'AdfEvent',
             libraries = [AdfEvent],
             testApps = [test_AdfEvent],
             includes = listFiles(['AdfEvent/*.h']))




