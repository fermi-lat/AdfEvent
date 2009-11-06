# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/AdfEvent/SConscript,v 1.6 2009/08/07 21:52:17 jrb Exp $
# Authors: N.Omodei <nicola.omodei@pi.infn.it>
# Version: AdfEvent-00-05-02
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()
libEnv = baseEnv.Clone()

libEnv.Tool('AdfEventLib',depsOnly=1)
AdfEvent = libEnv.StaticLibrary('AdfEvent',listFiles(['src/*.cxx']))

progEnv.Tool('AdfEventLib')
test_AdfEvent = progEnv.Program('test_AdfEvent', ['src/test/testMain.cxx'])

progEnv.Tool('registerTargets', package = 'AdfEvent',
             staticLibraryCxts = [[AdfEvent, libEnv]],
             testAppCxts = [[test_AdfEvent, progEnv]],
             includes = listFiles(['AdfEvent/*.h']))




