Negocio123
=====

Webpage that guides future business owners through the process to start their business.

How to Run Locally
=====

Clone the repo and `cd` into the directory

```bash
git clone git@github.com:CoquiCoders/negocio123.git
cd negocio123
```

Create a virtualenv. [(Or download it if you don't have it)](http://virtualenv.readthedocs.org/en/latest/)

```bash
virtualenv venv
source venv/bin/activate
```

Install the project's dependencies using `pip`

```bash
pip install -r requirements.txt
```

Now let's get your database up and running. Run the following command to get some seed data up there:

```bash
python db.py
```

Finally in order to run the server run this command:

```bash
python negocio123.py runserver
```

You should be able to see everything on your [localhost:5000](http://localhost:5000)


Tests
======

To run the tests run

```bash
python tests.py
```