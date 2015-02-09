# Midonet release

This project target the generation of midonet-release rpms for Enterprise Linuxes.

## Usage

If you do not have rpmbuild on your machine, just run:
```
docker build -t celebdor/rpmbuild docker/el7
```

Where 'celebdor' can be your linux username (`whoami`)

Then to generate the rpm package:

```
docker run -v /home/celebdor/code/midonet-release/pkg:/root/rpmbuild/SOURCES \
-v /home/celebdor/code/midonet-release/out:/root/rpmbuild/RPMS/noarch \
celebdor/rpmbuild -ba /root/rpmbuild/SOURCES/midonet-release.spec
```

Where 'celebdor' can be your linux username (`whoami`)

After running that, the midonet-release rpm package is going to be in
a directory called 'out'
