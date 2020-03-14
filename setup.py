from setuptools import setup, find_packages

setup(
    name='reconlit',
    version='1.0',
    python_requires='>=2.7',
    install_requires=['dnspython', 'requests', 'argparse; python_version==\'2.7\''],
    packages=find_packages()+['.'],
    include_package_data=True,
    url='https://github.com/YashGoti/recon-lit',
    license='GPL-3.0',
    description='A Sub domain Enumeration Tool',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: GNU General Public License v2',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security',
    ],
    keywords='A Sub domain Enumeration Tool',
    entry_points={
        'console_scripts': [
            'reconlit = reconlit:interactive',
        ],
    },
)
