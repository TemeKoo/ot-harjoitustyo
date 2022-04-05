from invoke import task
import os

windows = os.name == "nt"
pty = not windows

@task
def start(ctx):
    ctx.run("python src/main.py", pty=pty)

@task
def test(ctx):
    ctx.run("pytest src", pty=pty)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=pty)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=pty)