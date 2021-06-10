from setuptools import setup
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='html_parse',
    version='0.0.1',
    packages=['html_parse'],
    author="lvyunze",
    author_email="17817462542@163.com",
    description="html数据解析封装",
    keywords="提取html表格数据",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lvyunze/html_parse",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['pandas==1.1.2'],
)