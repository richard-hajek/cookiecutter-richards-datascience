#!/usr/bin/env python
from __future__ import annotations

import os
import shutil
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath: str) -> None:
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


def move_file(filepath: str, target: str) -> None:
    os.rename(os.path.join(PROJECT_DIRECTORY, filepath), os.path.join(PROJECT_DIRECTORY, target))


def move_dir(src: str, target: str) -> None:
    shutil.move(os.path.join(PROJECT_DIRECTORY, src), os.path.join(PROJECT_DIRECTORY, target))

def git_init():
    subprocess.run(["git", "init"], cwd=PROJECT_DIRECTORY, check=True)

    if "{{cookiecutter.include_richards_toolbox}}" == "y":
        submodule_path = os.path.join("src", "lib", "richards-toolbox")
        subprocess.run([
            "git", "submodule", "add",
            "git@github.com:richard-hajek/richards-toolbox.git",
            submodule_path
        ], cwd=PROJECT_DIRECTORY, check=True)


if __name__ == "__main__":
    if "{{cookiecutter.include_github_actions}}" != "y":
        remove_dir(".github")
    else:
        if "{{cookiecutter.mkdocs}}" != "y" and "{{cookiecutter.publish_to_pypi}}" == "n":
            remove_file(".github/workflows/on-release-main.yml")
    
    if "{{cookiecutter.use_data_dir}}" != "true":
        remove_dir("_data")
