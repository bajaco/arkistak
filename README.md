# Arkistak

Arkistak is intended to be a full-stack application generator that parses JSON templates build basic models, views, and behaviors.

Currently only has functionality to generate a virtual environment, source it, and install packages.

### Usage
The following command will create a virtual environment and install Flask. Must be run in the main directory to access the arkistak package:
`python -m arkistak create blog'
When sourced outside of arkistak the prompt for this environment will display as:
`(arkistak-blog)`
