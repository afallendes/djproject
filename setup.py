import os, platform
import subprocess
from argparse import ArgumentParser


# change working directory
os.chdir("setup")

parser = ArgumentParser()
parser.add_argument("-p", "--production", action="store_true")
parser.add_argument("command")

args, unknownargs = parser.parse_known_args()

# DEBUG:
# print(args, unknownargs)

BASE_COMPOSE_FILE = "base.docker-compose.yml"
DEV_COMPOSE_FILE = "development.docker-compose.yml"
PRO_COMPOSE_FILE = "production.docker-compose.yml"

COMPOSE_FILE = [
    "docker", "compose",
    "-f", BASE_COMPOSE_FILE,
    "-f", PRO_COMPOSE_FILE if args.production else DEV_COMPOSE_FILE
]

DOCKER_COMMAND = COMPOSE_FILE + [args.command] + unknownargs

subprocess.run(DOCKER_COMMAND)
