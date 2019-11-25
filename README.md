# Purpose
This is a small simulator for setting up an apache server infront of a flask app as a sub url of the main server address.  In this case it will place the flask app behind the url `http://localhost/helloapp`.  This has been put together to demonstrate the ways flask must be configured in order to be able to work when not at the root of the url tree so that it can play nice in systems with more involved service layers underneath.

As this is simulating a real environment that normally would have a mod_auth_cas requirment on `/` the apache service passes through a `REMOTE_USER` variable to all applications behind it set simply to `testuser`.

## Customization
The port for apache can be altered simply by updating the `docker-compose.yml` file; for example changing the `80:80` entry to `8080:80` will change the url to `http://localhost:8080/helloapp`.

Additionally doing a string replacement on `helloapp` in the file `./apache/sites/default-vhost.conf` will allow you to rename the url the flask application lives at to anything you might want.
