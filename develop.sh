#!/usr/bin/env bash
celery -A simple_celery.tasks worker --loglevel=info
