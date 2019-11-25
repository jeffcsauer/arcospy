import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name = "arcospy",
	version = "0.0.1",
	author = "Python translator: Jeffery Sauer. Original R Package Authors: Washington Post Data Investigations Team",
	author_email = "jcsauer@terpmail.umd.edu",
	description = "Python version of the R arcos package",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = "https://github.com/jeffcsauer/arcospy",
	packages = setuptools.find_packages(),
	classifiers = [
		"Programming Language :: Python :: 3", 
		"License :: OSI Approvied :: MIT License", 
		"Operating System :: OS Independent",
	],
	python_requires = '>=3.6',
)