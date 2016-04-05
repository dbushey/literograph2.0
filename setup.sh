

# General updates
sudo apt-get update
sudo locale-gen en_US.UTF-8

# Install PostgreSQL and setup database
sudo apt-get install -y postgresql 
sudo apt-get install -y postgresql-contrib
sudo -u postgres psql -U postgres -d postgres -c "alter user postgres with password 'password';"
sudo -u postgres createdb axiologue_db
sudo -u postgres psql -c "CREATE EXTENSION adminpack;"

# Install necessary libraries
sudo apt-get install -y python3-dev
sudo apt-get install -y libpq-dev

# Install pip and necessary packages
sudo apt-get install -y python3-pip
sudo pip3 install django
sudo pip3 install psycopg2

# Add bash aliases
echo "alias runs='python3 manage.py runserver [::]:8001'" >> ~/.bash_aliases && source ~/.bash_aliases
echo "alias mm='python3 manage.py makemigrations'" >> ~/.bash_aliases && source ~/.bash_aliases
echo "alias migrate='python3 manage.py migrate'" >> ~/.bash_aliases && source ~/.bash_aliases
echo "alias shell='python3 manage.py shell'" >> ~/.bash_aliases && source ~/.bash_aliases