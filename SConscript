# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/AdfEvent/SConscript,v 1.9 2010/06/12 17:19:08 jrb Exp $
# Authors: N.Omodei <nicola.omodei@pi.infn.it>
# Version: AdfEvent-00-05-03
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()
libEnv = baseEnv.Clone()

libEnv.Tool('addLinkDeps', package = 'AdfEvent', toBuild='static')
AdfEvent = libEnv.StaticLibrary('AdfEvent',listFiles(['src/*.cxx']))

progEnv.Tool('AdfEventLib')
test_AdfEvent = progEnv.Program('test_AdfEvent', ['src/test/testMain.cxx'])

progEnv.Tool('registerTargets', package = 'AdfEvent',
             staticLibraryCxts = [[AdfEvent, libEnv]],
             testAppCxts = [[test_AdfEvent, progEnv]],
             includes = listFiles(['AdfEvent/*.h']))




