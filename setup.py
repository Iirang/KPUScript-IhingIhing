from distutils.core import setup, Extension

module1 = Extension('spammodule',
                    sources = ['spammodule.c'])

setup(
    name='Ihing-Ihing',
    version='1.0',
    py_modules=['main', 'Horse', 'Owner', 'Map', 'raceResult', 'raceHorseInfo', 'horseOwnerInfo', 'TelegramBot'],
    ext_modules = [module1]
   ) 