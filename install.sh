#!/bin/bash
[ -e prj.db ] && rm prj.db
sqlite3 prj.db <prj-tables.sql
sqlite3 prj.db <test-data.sql
