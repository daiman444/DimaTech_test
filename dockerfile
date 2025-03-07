ARG BASE_IMG=python:3.13-alpine

FROM ${BASE_IMG} AS app

RUN apk update
COPY ./ /app/
COPY --from=ghcr.io/astral-sh/uv:0.5.18 /uv /uvx /bin/
WORKDIR /app
RUN uv sync
ENV PATH="/src/.venv/bin:$PATH"
CMD [ "uvicorn", "--factory", "src.main:create_app", "--host", "0.0.0.0", "--port", "8000" ]
