from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="Jinja2",
    install_requires=["MarkupSafe @ git+https://github.com/ectoglasses/markupsafe.git#egg=MarkupSafe"],
    extras_require={"i18n": ["Babel>=2.7"]},
)
