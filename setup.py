from setuptools import setup, find_packages

setup(
	name='mac2trash',
	version='1.0.0',
	packages=find_packages(),
	entry_points={
		'console_scripts': [
			'mac2trash = mac2trash.__main__:main'
		]
	},
	author='Troy Grizzle',
	author_email='snark@macintrash.org',
	description='Remove macOS metadata and junk from files and folders.',
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	url='https://macintrash.org',
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
	],
	python_requires='>=3.6',
)
