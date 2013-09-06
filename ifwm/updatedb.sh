cd settings
./cfgset.sh gen
cd ..
django-admin syncdb
cd settings
./cfgset.sh run
cd ..
./manage.py runserver
