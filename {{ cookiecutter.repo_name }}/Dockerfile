{% if cookiecutter.framework == "flask" %}

{% if cookiecutter.project_type == "apiserver" %}
FROM {% if cookiecutter.use_alipine_base == "y" %}python:2.7.15-alpine3.8 {% else %}python:2.7.15 {% endif %}
{% elif cookiecutter.project_type == "behaviour" %}
FROM macherlabs.azurecr.io/edge:latest_cpu
{% else %}
FROM ubuntu
{% endif %}

{% elif cookiecutter.framework == "nodejs" %}
FROM node:8
{% else %}
FROM ubuntu
{% endif %}

LABEL maintainer="{{ cookiecutter.full_name }} <{{ cookiecutter.email }}>"

##########################################
# DO NOT EDIT THIS ----->
##########################################
ENV APP_PORT {{ cookiecutter.port }}
ENV PORT ${APP_PORT}

# Expose ports
EXPOSE ${APP_PORT}

# Add source code
COPY . .
WORKDIR /app

# Make scripts executable
RUN chmod +x /start.sh
RUN chmod +x /entrypoint.sh
RUN chmod +x /app/install.sh
RUN chmod +x /app/prestart.sh
RUN chmod +x /app/serve.sh
RUN /app/install.sh

# Add Tini init system
{% if cookiecutter.use_alipine_base == "y" %}
RUN apk add --no-cache tini
ENTRYPOINT ["/sbin/tini", "-g", "--", "/entrypoint.sh"]
{% elif cookiecutter.use_alipine_base == "n" %}
ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "-g", "--", "/entrypoint.sh"]
{% else %}
ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "-g", "--", "/entrypoint.sh"]
{% endif %}

##########################################
# ------> DO NOT EDIT THIS
##########################################

# Pass your environment variables
{% if cookiecutter.framework == "flask" %}
ENV APP_HOST_NAME {{ cookiecutter.host_name }}
ENV APP_MODULE {{ cookiecutter.repo_name.lower().replace('-', '_') }}
ENV APP_THREADS 2
# Make /app/* available to be imported by Python globally to better support several use cases like Alembic migrations.
ENV PYTHONPATH=/app
{% elif cookiecutter.framework == "nodejs" %}
ENV APP_HOST_NAME {{ cookiecutter.host_name }}
{% else %}
ENV APP_HOST_NAME {{ cookiecutter.host_name }}
{% endif %}

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Supervisor, which in turn will start Nginx and uWSGI
CMD ["/start.sh"]
