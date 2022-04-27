#!/bin/bash
function start_uvicorn() {
  UVICORN_CMD=""
  UVICORN_CMD+="uvicorn --host ${UVICORN_HOST:=0.0.0.0} --port ${UVICORN_PORT:=8000} --workers ${UVICORN_WORKERS:=1} "
  UVICORN_CMD+="--loop ${UVICORN_EVENT_LOOP_TYPE:=auto} --http ${UVICORN_HTTP_PROTOCOL:=auto} "
  UVICORN_CMD+="--ws ${UVICORN_WEBSOCKET_PROTOCOL:=auto} --lifespan ${UVICORN_LIFESPAN_IMPLEMENTATION:=auto} "
  UVICORN_CMD+="--interface ${UVICORN_INTERFACE:=auto} --log-level ${UVICORN_LOG_LEVEL:=info} "
  UVICORN_CMD+="--timeout-keep-alive ${UVICORN_TIMEOUT_KEEP_ALIVE:=5} "

  if [[ "${UVICORN_RELOAD:=true}" == "true" ]]; then
      UVICORN_CMD+="--reload "
  fi

  if [[ "${UVICORN_ENABLE_ACCESS_LOG:=false}" == "true" ]]; then
      UVICORN_CMD+="--access-log "
  else
      UVICORN_CMD+="--no-access-log "
  fi

  if [[ "${UVICORN_COLORIZED_LOGGING:=true}" == "true" ]]; then
      UVICORN_CMD+="--use-colors "
  else
      UVICORN_CMD+="--no-use-colors "
  fi

  if [[ "${UVICORN_ENABLE_PROXY_HEADERS:=false}" == "true" ]]; then
      UVICORN_CMD+="--proxy-headers "
  else
      UVICORN_CMD+="--no-proxy-headers "
  fi

  if [[ "${UVICORN_FORWARDED_ALLOW_IPS}" != "" ]]; then
      UVICORN_CMD+="--forwarded-allow-ips ${UVICORN_FORWARDED_ALLOW_IPS} "
  fi

  if [[ "${UVICORN_ROOT_PATH}" != "" ]]; then
      UVICORN_CMD+="--root-path ${UVICORN_ROOT_PATH} "
  fi

  if [[ "${UVICORN_LIMIT_CONCURRENCY}" != "" ]]; then
      UVICORN_CMD+="--limit-concurrency ${UVICORN_LIMIT_CONCURRENCY} "
  fi

  if [[ "${UVICORN_BACKLOG}" != "" ]]; then
      UVICORN_CMD+="--backlog ${UVICORN_BACKLOG} "
  fi

  if [[ "${UVICORN_LIMIT_MAX_REQUESTS}" != "" ]]; then
      UVICORN_CMD+="--limit-max-requests ${UVICORN_LIMIT_MAX_REQUESTS} "
  fi

  $UVICORN_CMD "src:app"
}

start_uvicorn