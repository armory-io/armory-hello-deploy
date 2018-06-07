# armory-hello-deploy

This is for demo purposes, let's show some automation!


## Developing
`arm run`


## Building a package
We're using `gradlew` to build the package


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
brew install dpkg
dpkg -c build/distributions/*.deb
```

-Inspect the control file
```bash
dpkg -f build/distributions/*.deb
```


