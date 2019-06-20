# cookiecutter-vedalabs-server-boilerplate
========
Boilerplate for creating CI/CD enabled Server applications for VedaLabs.  This primarily consists of bootstrapping your project with dockerfile & charts for kubernetes helm for deployment.

This cookiecutter is being used from [CookieCutter](https://github.com/audreyr/cookiecutter")

# Introduction
This project takes care of the setup and configuration so you can focus on making your service awesome. Scaffolding a project takes seconds and it gives you the essentials of devops and container orchestration, like drone, helm, kubernetes integration to get started. This project aims to get out of your way, and to allow you easily and quickly create web services while providing a solid foundation for your service to mature in the future.

## Features

- Support for RESTful & JSON-RPC services via [Python Eve](http://docs.python-eve.org/en/latest/) & [Python Flask](http://flask.pocoo.org/)
- Support for Web frameworks like [Python Flask](http://flask.pocoo.org/) & [nodejs](https://nodejs.org/en/)
- CI/CD via ["Drone.io", "gitlabci"
- [Helm](https://www.helm.sh/) for deployment in [Kubernetes](https://kubernetes.io/)

## Quick Start
Install [cookiecutter](https://github.com/audreyr/cookiecutter):
```bash
pip install cookiecutter
```

Scaffold your project (from bitbucket):
```
cookiecutter gh:macherlabs/cookiecutter-vedalabs-server-boilerplate
```

![server scaffolding](https://cloud.githubusercontent.com/assets/3332051/10678207/df1f2de0-78de-11e5-84b7-62484ddfea56.gif)

## Contributing
Want a new feature or find a bug? Submit a Pull Request!
