# demo

It is a study purposes project. I don't expect to provide support or even
maintain for others platforms.

* very simple Python script using argparse
* GNU Makefile
* Python bdist to compile and build py files
* sphinx to generate documentation and man page
* Further Fedora Copr to build RPM

Only tested on **Fedora 24**

Steps
=====

1. clone the repo:

	$ git clone https://github.com/eduardocerqueira/demo.git

2. Make sure you have all packages otherwise install:

	$ sudo dnf install git git-review gcc make rpm-build python-devel python-setuptools python-pip python2-flake8 pylint python-sphinx python2-devel python-setuptools python-kitchen python-pip openssl-devel libffi-devel python-oslo-serialization python-nose python-pep8

3. Generating RPM

	$ make rpm

For all available options run:

	$ make

you should get an output similar this:

	Usage: make <target> where <target> is one of

	clean     clean temp files from local workspace
	doc       generate sphinx documentation and man pages
	test      run unit tests locally
	tarball   generate tarball of project
	rpm       build source codes and generate rpm file
	srpm      generate SRPM file
	all       clean test doc rpm
	flake8    check Python style based on flake8


4. Installing

	$sudo dnf install rpmbuild/RPMS/x86_64/demo-0.0.1-1.fc24.x86_64.rpm

5. check man page

After install you can check man page:

	$ man demo

6. run

	$ demo --help

7. uninstall

	$ sudo dnf remove demo -y


OUTPUTS
=======

some outputs

building
--------

	$ make rpm

	#rpmdev-setuptree into project folder
	make -C docs/ html
	make[1]: Entering directory '/home/ecerquei/git/demo/docs'
	sphinx-build -b html -d build/doctrees   source build/html
	Running Sphinx v1.4.8
	loading pickled environment... done
	building [mo]: targets for 0 po files that are out of date
	building [html]: targets for 0 source files that are out of date
	updating environment: 0 added, 0 changed, 0 removed
	looking for now-outdated files... none found
	no targets are out of date.
	build succeeded.

	Build finished. The HTML pages are in build/html.
	make[1]: Leaving directory '/home/ecerquei/git/demo/docs'
	make -C docs/ man
	make[1]: Entering directory '/home/ecerquei/git/demo/docs'
	sphinx-build -b man -d build/doctrees   source build/man
	Running Sphinx v1.4.8
	loading pickled environment... done
	building [mo]: targets for 0 po files that are out of date
	building [man]: all manpages
	updating environment: 0 added, 0 changed, 0 removed
	looking for now-outdated files... none found
	writing... Demo.1 { development release }
	build succeeded.

	Build finished. The manual pages are in build/man.
	make[1]: Leaving directory '/home/ecerquei/git/demo/docs'
	cp docs/build/man/Demo.1 Demo.1
	sed \
		-e 's/@RPM_VERSION@/0.0.1/g' \
		-e 's/@RPM_RELEASE@/1.fc24/g' \
		< demo.spec.in \
		> /home/ecerquei/git/demo/rpmbuild/SPECS/demo.spec
	git ls-files | tar --transform='s|^|demo/|' \
	--files-from /proc/self/fd/0 \
	-czf /home/ecerquei/git/demo/rpmbuild/SOURCES/demo-0.0.1.tar.gz /home/ecerquei/git/demo/rpmbuild/SPECS/demo.spec
	tar: Removing leading `/' from member names
	rpmbuild --define="_topdir /home/ecerquei/git/demo/rpmbuild" --define "_specdir /home/ecerquei/git/demo/rpmbuild/SPECS" \
	-ts /home/ecerquei/git/demo/rpmbuild/SOURCES/demo-0.0.1.tar.gz
	Wrote: /home/ecerquei/git/demo/rpmbuild/SRPMS/demo-0.0.1-1.fc24.src.rpm
	rpmbuild --define="_topdir /home/ecerquei/git/demo/rpmbuild" --rebuild /home/ecerquei/git/demo/rpmbuild/SRPMS/demo-0.0.1-1.fc24.src.rpm
	Installing /home/ecerquei/git/demo/rpmbuild/SRPMS/demo-0.0.1-1.fc24.src.rpm
	Executing(%prep): /bin/sh -e /var/tmp/rpm-tmp.18dk9Q
	+ umask 022
	+ cd /home/ecerquei/git/demo/rpmbuild/BUILD
	+ cd /home/ecerquei/git/demo/rpmbuild/BUILD
	+ rm -rf demo
	+ /usr/bin/gzip -dc /home/ecerquei/git/demo/rpmbuild/SOURCES/demo-0.0.1.tar.gz
	+ /usr/bin/tar -xof -
	+ STATUS=0
	+ '[' 0 -ne 0 ']'
	+ cd demo
	+ /usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
	+ exit 0
	Executing(%build): /bin/sh -e /var/tmp/rpm-tmp.s9eJHC
	+ umask 022
	+ cd /home/ecerquei/git/demo/rpmbuild/BUILD
	+ cd demo
	+ /usr/bin/python setup.py build
	running build
	running build_py
	creating build
	creating build/lib
	creating build/lib/demo
	copying demo/__init__.py -> build/lib/demo
	copying demo/driver.py -> build/lib/demo
	running egg_info
	creating demo.egg-info
	writing requirements to demo.egg-info/requires.txt
	writing demo.egg-info/PKG-INFO
	writing top-level names to demo.egg-info/top_level.txt
	writing dependency_links to demo.egg-info/dependency_links.txt
	writing entry points to demo.egg-info/entry_points.txt
	writing manifest file 'demo.egg-info/SOURCES.txt'
	reading manifest file 'demo.egg-info/SOURCES.txt'
	reading manifest template 'MANIFEST.in'
	warning: no files found matching 'docs/build/man/Demo.1'
	warning: no previously-included files matching '*' found under directory 'tests'
	warning: no previously-included files matching '__pycache__' found under directory '*'
	warning: no previously-included files matching '*.orig' found under directory '*'
	warning: no previously-included files matching '*' found under directory 'docs'
	warning: no previously-included files matching '.pyc' found anywhere in distribution
	warning: no previously-included files matching '.pyo' found anywhere in distribution
	writing manifest file 'demo.egg-info/SOURCES.txt'
	+ exit 0
	Executing(%install): /bin/sh -e /var/tmp/rpm-tmp.mLEPWp
	+ umask 022
	+ cd /home/ecerquei/git/demo/rpmbuild/BUILD
	+ '[' /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64 '!=' / ']'
	+ rm -rf /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64
	++ dirname /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64
	+ mkdir -p /home/ecerquei/git/demo/rpmbuild/BUILDROOT
	+ mkdir /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64
	+ cd demo
	+ /usr/bin/python setup.py install -O1 --skip-build --root /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64
	running install
	running install_lib
	creating /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64/usr
	creating /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64/usr/lib
	creating /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64/usr/lib/python2.7
	creating /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64/usr/lib/python2.7/site-packages
	creating /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64/usr/lib/python2.7/site-packages/demo
	copying build/lib/demo/__init__.py -> /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64/usr/lib/python2.7/site-packages/demo
	copying build/lib/demo/driver.py -> /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64/usr/lib/python2.7/site-packages/demo
	byte-compiling /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64/usr/lib/python2.7/site-packages/demo/__init__.py to __init__.pyc
	byte-compiling /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64/usr/lib/python2.7/site-packages/demo/driver.py to driver.pyc
	writing byte-compilation script '/tmp/tmpQFzcTZ.py'
	/usr/bin/python -O /tmp/tmpQFzcTZ.py
	removing /tmp/tmpQFzcTZ.py
	running install_egg_info
	running egg_info
	writing requirements to demo.egg-info/requires.txt
	writing demo.egg-info/PKG-INFO
	writing top-level names to demo.egg-info/top_level.txt
	writing dependency_links to demo.egg-info/dependency_links.txt
	writing entry points to demo.egg-info/entry_points.txt
	reading manifest file 'demo.egg-info/SOURCES.txt'
	reading manifest template 'MANIFEST.in'
	warning: no files found matching 'docs/build/man/Demo.1'
	warning: no previously-included files matching '*' found under directory 'tests'
	warning: no previously-included files matching '__pycache__' found under directory '*'
	warning: no previously-included files matching '*.orig' found under directory '*'
	warning: no previously-included files matching '*' found under directory 'docs'
	warning: no previously-included files matching '.pyc' found anywhere in distribution
	warning: no previously-included files matching '.pyo' found anywhere in distribution
	writing manifest file 'demo.egg-info/SOURCES.txt'
	Copying demo.egg-info to /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64/usr/lib/python2.7/site-packages/demo-0.0.1-py2.7.egg-info
	running install_scripts
	Installing demo script to /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64/usr/bin
	+ mkdir -p /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64//usr/share/man/man1
	+ cp Demo.1 /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64//usr/share/man/man1/Demo.1
	+ '[' '%{buildarch}' = noarch ']'
	+ QA_CHECK_RPATHS=1
	+ case "${QA_CHECK_RPATHS:-}" in
	+ /usr/lib/rpm/check-rpaths
	+ /usr/lib/rpm/check-buildroot
	+ /usr/lib/rpm/brp-compress
	+ /usr/lib/rpm/brp-strip /usr/bin/strip
	+ /usr/lib/rpm/brp-strip-comment-note /usr/bin/strip /usr/bin/objdump
	+ /usr/lib/rpm/brp-strip-static-archive /usr/bin/strip
	+ /usr/lib/rpm/brp-python-bytecompile /usr/bin/python 1
	Bytecompiling .py files below /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64/usr/lib/python2.7 using /usr/bin/python2.7
	+ /usr/lib/rpm/brp-python-hardlink
	+ /usr/lib/rpm/redhat/brp-java-repack-jars
	Processing files: demo-0.0.1-1.fc24.x86_64
	Executing(%doc): /bin/sh -e /var/tmp/rpm-tmp.ApnjFf
	+ umask 022
	+ cd /home/ecerquei/git/demo/rpmbuild/BUILD
	+ cd demo
	+ DOCDIR=/home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64/usr/share/doc/demo
	+ export DOCDIR
	+ /usr/bin/mkdir -p /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64/usr/share/doc/demo
	+ cp -pr README.md /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64/usr/share/doc/demo
	+ cp -pr AUTHORS /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64/usr/share/doc/demo
	+ exit 0
	Provides: demo = 0.0.1-1.fc24 demo(x86-64) = 0.0.1-1.fc24
	Requires(rpmlib): rpmlib(CompressedFileNames) <= 3.0.4-1 rpmlib(FileDigests) <= 4.6.0-1 rpmlib(PartialHardlinkSets) <= 4.0.4-1 rpmlib(PayloadFilesHavePrefix) <= 4.0-1
	Requires: /usr/bin/python python(abi) = 2.7
	Checking for unpackaged file(s): /usr/lib/rpm/check-files /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64
	Wrote: /home/ecerquei/git/demo/rpmbuild/RPMS/x86_64/demo-0.0.1-1.fc24.x86_64.rpm
	Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.HG9OL5
	+ umask 022
	+ cd /home/ecerquei/git/demo/rpmbuild/BUILD
	+ cd demo
	+ /usr/bin/rm -rf /home/ecerquei/git/demo/rpmbuild/BUILDROOT/demo-0.0.1-1.fc24.x86_64
	+ exit 0
	Executing(--clean): /bin/sh -e /var/tmp/rpm-tmp.YJnPSV
	+ umask 022
	+ cd /home/ecerquei/git/demo/rpmbuild/BUILD
	+ rm -rf demo
	+ exit 0


installing
----------

	$sudo dnf install rpmbuild/RPMS/x86_64/demo-0.0.1-1.fc24.x86_64.rpm

	Last metadata expiration check: 2:11:27 ago on Mon Oct 31 08:23:22 2016.
	Dependencies resolved.
	===================================================================================================================================================================================================================
	 Package                                       Arch                                            Version                                                 Repository                                             Size
	===================================================================================================================================================================================================================
	Installing:
	 demo                                          x86_64                                          0.0.1-1.fc24                                            @commandline                                           14 k

	Transaction Summary
	===================================================================================================================================================================================================================
	Install  1 Package

	Total size: 14 k
	Installed size: 8.0 k
	Is this ok [y/N]:





