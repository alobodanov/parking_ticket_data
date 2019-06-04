#!/bin/bash
export FLASK_APP=parkingTicketData
export FLASK_DEBUG=true
pip install -e .
FLASK_APP=parkingTicketData/app.py flask run
