from invoke import task

PROJECT_DIR = '{{cookiecutter.project_dir}}'
IMAGE_NAME = f"tuteco/{PROJECT_DIR}"


@task
def build_local(context):
    """
        build an image from a Dockerfile with tag 'latest-dev'
    """
    context.run(f"docker build -t {IMAGE_NAME}:latest-dev . -f Dockerfile")


@task(help={
    "images": "remove images used by service"
})
def docker_clean(context, images=False):
    """
        remove containers, networks, volumes and images(optional)
    """
    context.run("docker compose down -v")

    if images:
        # delete project image
        context.run(f"docker rmi {IMAGE_NAME}:latest-dev -f")
        # delete AWS image if not in use
        context.run(f"docker rmi amazon/amazon-ecs-local-container-endpoints")
        # remove dangling images
        context.run(f"docker image prune -f")
