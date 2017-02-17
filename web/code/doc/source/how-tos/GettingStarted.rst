Getting Started
===============

Step 1
------

Clone the repository.

Step 2
------

Build the images. This will install all the packages required using `pip` (these are listed in the [requirements.txt](./web/requirements.txt) file in case you're interested). This will probably take a little bit of time.

  $ docker-compose build


Step 3
------

Now, you're ready to bring everything up. I prefer to do this when developing:

  $ docker-compose up -d ; docker-compose logs -f

It brings the images up and disconnects. It then gives a live stream of the logs in a separate process so that if you break out of it (ctrl-C), it doesn't kill the machines as well. If you've not downloaded the PostgreSQL image before, it will take a little time to download it before starting everything up.

Step 4
------

In another terminal window, run the following:

  $ docker-compose run --rm web /bin/bash
  root@xxxxxxxxxxxx:/code# ./manage.py migrate
  root@xxxxxxxxxxxx:/code# ./manage.py createsuperuser
  root@xxxxxxxxxxxx:/code# ./manage.py shell_plus

This will set up the database and then create a super user (I've left this as an interactive activity so that you can set your own credentials), and then drop you into an interactive shell.

Step 5
------

If all has gone well, you should now be able to visit your site at:  `http://localhost:8015/` and the admin interface at `http://localhost:8015/admin`

Step 6
------

You might notice that no products show up on the public side. You need to create a "Store" under Vendor:Printful and connect to it with your API keys.
