# Udacity Logs Analysis Project
This is a project for the Udacity Full Stack Nanodegree.

It is a reporting tool for a newspaper that runs SQL 
queries and prints out the 3 most popular articles in 
the database, the authors in order of popularity and 
days with a high proportion of HTTP error responses.

It is written in Python 3 and runs from the command line.

## Usage
The project runs using VirtualBox and Vagrant. It builds 
off of the [FSND-Virtual-Machine](https://github.com/udacity/fullstack-nanodegree-vm).

Clone the code inside of the `vagrant` directory of the
`fullstack-nanodegree-vm` directory, then you can start up
the virtual machine. 
```
git clone https://github.com/jasonreed7/udacity-logs-analysis.git
vagrant up
vagrant ssh
```

Data can be loaded into the news database from Udacity's 
`newsdata.sql` file.
```
psql -d news -f newsdata.sql
```

To run the program:
```
python3 report.py
```