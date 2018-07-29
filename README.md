i think this will set you up on ubuntu bionic:

```
# install systemwide dependencies
apt install python3 python3-virtualenv python-pip unzip
# clone repo
git clone git@github.com:seetherrr/coin-crap.git
cd coin-crap
# create python virtual environment
mkdir venv
python3 -m virtualenv -p python3 venv
# activate virtual environment (once per shell!)
. venv/bin/activate # just use "deactivate" to deactivate in your shell
# install local dependencies (make sure you have activated first)
pip install -r requirements.txt # i think
# download data (this link might expire?)
mkdir data
cd data
# if this link doesn't work visit https://www.kaggle.com/mczielinski/bitcoin-historical-data/version/14 and figure it out yourself
curl -o bitcoin-historical-data.zip 'https://storage.googleapis.com/kaggle-datasets/1346/44817/bitcoin-historical-data.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1533086724&Signature=Cnoo6%2BotEuSFyxw9U5bgh%2F7nIqFHAroWCocp%2BJkIlET1ofTq8UljXGt5zNWs0NowZEMXyNEUhs0s2Ttgy4JdvAZ435ktrq6SbwZZjKErvtXv5i3LIVXjEHCnwzqryv18B05B1q4H7K3Pemhr4jX9TWrIpqwupybHSLUw2Lj7mZQXrqhbap0m638VxFqez4yl8GUMUJ%2Bg28uq6icoII7ujn7D5meegTDjC%2F1TyWnp9Fj%2B%2FvQI3wJ6jwAtEEbeEWq6Z7Wq2vPEqO1dwaVV0Z5ZcLMK%2BFkqThd1R5DOlm2Jj0YJbDrr9Tlfb56138GPIg7wZpkKYNlrNKHp%2BJJPYS50Sg%3D%3D'
unzip bitcoin-historical-data.zip
# optionally remove the zip file
rm bitcoin-historical-data.zip
# optionally create smaller versions of a csv for quicker testing:
head -n 10 bitstampUSD_1-min_data_2012-01-01_to_2018-06-27.csv short-test.csv
# you're off to the races!
```
