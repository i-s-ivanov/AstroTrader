# AstroTrader
SoftUni final project defence - Django

## Description

AstroTrader is an app for selling or buying second hand astro equipment

## Getting Started

### Urls:

#### Accounts:

* Authentication (non-authenticated)
    * /accounts/login/
    * /accounts/register/
* Authentication (authenticated)
    * /accounts/update/
    * /accounts/delete/<int:pk>/
    * /accounts/profile/
    * /accounts/password/ - change user's password
    * /accounts/logout/
    
#### Telescopes:

* Authentication (non-authenticated)
    * /telescopes/details/<int:pk>/comment/ - everyone can comment and ask questions on post
* Authentication (authenticated)
    * /telescopes/create/
    * /telescopes/update/<int:pk>/
    * /telescopes/delete/<int:pk>/
    * /telescopes/details/<int:pk>/

#### Common:

* Authentication (non-authenticated)
    * /search/ - search by make or model
         

### Executing program

* How to run the program
```
pip install requirments.txt
```
