# mym_order

clone project
```
git clone https://github.com/ijas-mp/mym_order.git
```
create a venv

```
python3 -m venv env
```
install requirements
```
pip install -r requirements.txt
```
migrate db
```
python manage.py migrate
```
create super user
```
python manage.py createsuperuser
```
runserver
```
python manage.py runsrver
```

## api documentation can be seen on http://127.0.0.1:8000/api/docs/

### addres can be added using `/api/address`

### item can be added using `/api/item`

### order can be added using `/api/order`