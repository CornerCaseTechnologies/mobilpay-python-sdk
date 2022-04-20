import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mobilpay python sdk",
    version="v1.0.1b1",
    author="MobilPay",
    author_email="contact@web2sms.ro",
    description="A supposed sdk for making payments using mobilpay platform",
    long_description="Read short description",
    long_description_content_type="text/markdown",
    url="",
    project_urls={},
    classifiers=[
        "Development Status :: -1 - ???",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=["pycryptodome", "pyopenssl"],
)