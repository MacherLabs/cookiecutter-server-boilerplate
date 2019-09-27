#!/usr/bin/env python

import os
import distutils
from distutils import dir_util
from cookiecutter.main import cookiecutter

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
APP_DIRECTORY = 'app'

if __name__ == '__main__':
    if '{{ cookiecutter.framework }}' == 'flask' and '{{ cookiecutter.project_type }}' in ['apiserver', 'behaviour']:
        cookiecutter(
            'https://github.com/macherlabs/cookiecutter-{{ cookiecutter.framework }}-{{ cookiecutter.project_type }}.git', 
            no_input=True,
            extra_context={{ cookiecutter | jsonify }})
        distutils.dir_util.copy_tree('{{ cookiecutter.repo_name }}', APP_DIRECTORY)
        distutils.dir_util.remove_tree('{{ cookiecutter.repo_name }}')

    if '{{ cookiecutter.framework }}' == 'express' and '{{ cookiecutter.project_type }}' in ['apiserver']:
        cookiecutter(
            'https://github.com/macherlabs/cookiecutter-{{ cookiecutter.framework }}-{{ cookiecutter.project_type }}.git', 
            no_input=True,
            extra_context={{ cookiecutter | jsonify }})
        distutils.dir_util.copy_tree('{{ cookiecutter.repo_name }}', APP_DIRECTORY)
        distutils.dir_util.remove_tree('{{ cookiecutter.repo_name }}')

    if '{{ cookiecutter.framework }}' == 'flask' and '{{ cookiecutter.project_type }}' in ['behaviour']:
        print("Fetching Makefile from gitlab:remote-build-and-test")
        os.system("git clone https://gitlab.com/_macherlabs/behaviours/dev-ops/remote-build-and-test.git")
        distutils.file_util.move_file('remote-build-and-test/Makefile', ".")
        distutils.file_util.move_file('remote-build-and-test/Makehelper.sh', ".")
        distutils.dir_util.remove_tree('remote-build-and-test')