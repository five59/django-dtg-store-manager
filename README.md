# Print Aura API Sync

A Django/Python-based app that syncs the Print Aura API locally to provide tools and visibility into your products to make it easier to manage.

I created this tool to allow me to make it easier to see all of my options for designing dropship printing products through Print Aura.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites

*  [Docker Engine and Docker Composer](https://docs.docker.com)


### Installing

1. Clone the repository.

1. Add your API credentials to ```web/code/project/settings.py```. You will need to provide API_KEY and API_HASH. You can find these in your PrintAura account.

1. Build "web" first. This will install all the packages required using `pip` (these are listed in the [requirements.txt](./web/requirements.txt) file in case you're interested). This will probably take a little bit of time.
```
$ docker-compose build web
```

1. Bring up "db." This is a postgres box with a couple of volumes defined to persist data across runs. The ```-d``` argument disconnects the process from your terminal session, so you won't see any logging. Just wait a few moments before proceeding.
```
$ docker-compose up db -d
```
(If you know of a way to force Docker to wait for dependencies to come online before starting other services, let me know. This is always a problem for me.)

1. Now, you're ready to bring everything up:
```
$ docker-compose up -d ; docker-compose logs -f
```

1. In another terminal window, run the following:
```
$ docker-compose run --rm web /bin/bash
root@xxxxxxxxxxxx:/code# ./manage.py migrate
root@xxxxxxxxxxxx:/code# ./manage.py createsuperuser
root@xxxxxxxxxxxx:/code# ./manage.py shell_plus
```
This will set up the database and then create a super user (I've left this as an interactive activity so that you can set your own credentials), and then drop you into an interactive shell.

1. Now, you're ready to do an API sync from within the interactive shell:
```
>>> from printaura import helper
>>> helper.sync_api()
```
Look at the ```web/code/printaura/helper.py``` file for additional calls that you can make to sync with different parts of the API.

1. If all has gone well, you should now be able to visit your site at:  ```http://localhost:8015/``` and the admin interface at ```http://localhost:8015/admin```

1. You might notice that no products show up on the public side. This is by design. I wanted the ability to organize products into my own categories (since sometimes the Print Aura products are categorized in odd ways). In the admin interface, simply create **Local Product Groups** and then assign **Products** to them. These will now show up in the public UI.


## Depreciated Products
Something you'll find is that there are "depreciated" products mixed in. You can move them to their own group with the following snippet in the interactive shell:
```
>>> lpg = LocalProductGroup(name="Depreciated", slug='depreciated')
>>> lpg.save()
>>> for p in Product.objects.filter(name__contains='depreciated'):
...     p.localproductgroup = lpg
...     p.save()
```

## Built With

* [Django](https://docs.djangoproject.com/en/1.10/) - the 1.10.x series at the time of this writing.
* [Python 3.5](https://docs.python.org/3/) - the 3.5.x series at  the time of this writing.
* [Postgres](https://www.postgresql.org/docs/)


## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/printaura-api-wrapper/tags).


## Authors

* **Andrew Marconi, 559 Labs** - *Initial work*, [559 Labs](https://github.com/559Labs)


## License

This open source software is licensed under the **Apache License 2.0** (see [LICENSE.md](LICENSE.md) for details).

  > A permissive license whose main conditions require preservation of copyright and license notices. Contributors provide an express grant of patent rights. Licensed works, modifications, and larger works may be distributed under different terms and without source code.


## Acknowledgments

* [Print Aura](http://www.printaura.com/) - Print Aura is white-label solution for companies to have t-shirts printed on demand under YOUR BRAND. Print Aura makes t-shirt drop shipping easy. You control your customer information, we just print and ship and it all appears that it came from you.
