# armory-hello-deploy

This is for demo purposes, let's show some automation!


## Developing
`arm run`


## Building a package
Ideally, we want to use something like `fpm`. However, there is no support for adding your own files through the
python builder currently.

Example of a python package:
```bash
fpm -t deb \
    --name ${APP_NAME} \
    --version ${VERSION} \
    --no-auto-depends \
    --depends python3-flask \
    --depends 'python3:any (>= 3.3.2-2~)' \
    --depends 'python3' \
    -s python --python-pip /usr/bin/pip3 --python-bin /usr/bin/python3 \
    --package build/${APP_NAME}_${VERSION}_all.deb \
    --after-install etc/postinst \
    --deb-init etc/armory-hello-deploy.conf \
    --deb-default etc/default/armory-hello-deploy \
    --deb-default /etc/default/server-env \
    ./setup.py"
```


### General overview:
- package up your files
    - you can add `preinst` or `postinst` scripts. Note, it's not possible to run
    `apt-get` commands from within preinst/postinst. If you needed to add other packages
    consider adding `depends-on` or `pre-depends`. If your packages span multiple apps, consider a
    pre-baked option. If it doesn't really fall into this category, add it to an upstart script with a
    conditional run once or make it self destroying.
- (ubuntu) include an upstart script to start the app, see example.
- Spinnaker will deploy the specified version from jenkins.
- It's best to have the baking phase to only just do installs. Then on the next time the
image gets booted up, it'll start.


### Tips
- Inspect files included into a deb
```bash
brew intall dpkg
dpkg -c build/*.deb
```

-Inspect the control file
```bash
dpkg -f build/*.deb
```
