#!/bin/bash
cd /code

echo "Loading auth.user objects..."
./manage.py loaddata ./_fixtures/auth/*

echo "Loading Catalog objects..."
./manage.py loaddata ./_fixtures/catalog/*


echo "Loading Creative objects..."
./manage.py loaddata ./_fixtures/creative/*

echo "Loading WooCommerce objects..."
./manage.py loaddata ./_fixtures/outlet_woo/*

echo "Loading App objects..."
./manage.py loaddata ./_fixtures/app_shopfeeds/*
./manage.py loaddata ./_fixtures/app_care/*

# echo "Loading Manufacturer objects..."
# ./manage.py loaddata ./_fixtures/api_gooten.*

echo "SKIPPED api_gooten."