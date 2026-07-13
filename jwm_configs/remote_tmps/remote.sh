set -e

require_env() {
for var in "$@"; do
    if [ -z "${!var}" ]; then
        echo "Error: $var is not set" >&2
        exit 1
    fi
done
}
# change the following based on your running preference
export RUN_DIR_PRE="/home/jinma/project_remote_jwm"
export RUN_PROJ="fileserver_jingwei"

# uncomment the following to define them based on your running preference
# export HF_TOKEN="fill in your huggingface token"


JWM_SERVER_NAME=greatrawr
if [ -z ${RUN_BACKGROUND_JWM} ]; then
    docker compose ${DOCKER_ARGS} up --force-recreate -d
else
    docker compose ${DOCKER_ARGS} up --force-recreate -d 2>&1
fi
