### Use Bash!
Setup script.
```shell
git clone https://github.com/shaspire/serd-rpo5-24r-p1.git &&
cd ./serd-rpo5-24r-p1 &&
python -m venv venv &&
source ./venv/bin/activate &&
pip install -r ./src/req.txt
```

Assuming execution from root of repository.
Collect Static, Migrations and Superuser.
```shell
python src/manage.py collectstatic &&
python src/manage.py makemigrations &&
python src/manage.py migrate &&
python src/manage.py createsuperuser
```
