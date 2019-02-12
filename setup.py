from setuptools import setup

setup(
        name='narcelik-ui',
        version='1.0.0',
        packages=['narcelik'],
        license='GPLv3',
        author='Umut Karcı',
        description='Narçelik kahve makinası dokunmatık arayüzü',
        install_requires=['PySide2'],
        include_package_data=True,
        entry_points={
            'gui_scripts': [
                'narcelik = narcelik.narcelik_ui:main',
            ],
        }
)
