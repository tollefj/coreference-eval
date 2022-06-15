import setuptools  # type: ignore

setuptools.setup(
    name="coreference-eval",
    version="0.0.1",
    description="Common metrics and evaluation tools for coreference chains (jsonline format)",
    packages=setuptools.find_packages(),
    python_requires='>=3.9',
)