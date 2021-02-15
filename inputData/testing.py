from . import make10hexs_per_line
from . import makeBin
from . import makeTest
from . import makeDir

import os
from diehard.settings import BASE_DIR


def test(ID, filename):
	makeDir.main(ID, filename)
	path = os.path.join(BASE_DIR, 'uploads\\' + str(ID))
	make10hexs_per_line.main(os.path.join(path, filename), os.path.join(BASE_DIR,'inputData\\hex.ascii'))
	makeBin.main('hex.ascii', 'bin')
	makeTest.main('bin', 't.txt')
	makeTest.moveFile(ID)