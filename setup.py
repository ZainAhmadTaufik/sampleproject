import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()


setuptools.setup(
	nama = "ai_pkg",
	version = "0.0.2", 
	author = "Zain Ahmad Taufik",
	author_email = "zain1800018169@webmail.uad.aca.id",
	description = "A small example package",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = "https://github.com/ZainAhmadTaufik/sampleproject",
	packages = setuptools.find_packages(),
	classifiers=[
		"Programing Language :: Python :: 3",
		"License :: OSI Aproved :: License",
		"operationg System :: OS Independent",
		],
	)