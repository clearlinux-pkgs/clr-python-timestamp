#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-python-timestamp
Version  : 17
Release  : 33
URL      : http://localhost/cgit/projects/clr-python-timestamp/snapshot/clr-python-timestamp-17.tar.gz
Source0  : http://localhost/cgit/projects/clr-python-timestamp/snapshot/clr-python-timestamp-17.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: clr-python-timestamp-bin
Requires: clr-python-timestamp-license
Requires: python3
Requires: usrbinpython

%description
No detailed description available

%package bin
Summary: bin components for the clr-python-timestamp package.
Group: Binaries
Requires: clr-python-timestamp-license

%description bin
bin components for the clr-python-timestamp package.


%package license
Summary: license components for the clr-python-timestamp package.
Group: Default

%description license
license components for the clr-python-timestamp package.


%prep
%setup -q -n clr-python-timestamp-17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530305424
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1530305424
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/clr-python-timestamp
cp COPYING %{buildroot}/usr/share/doc/clr-python-timestamp/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/clr-python-timestamp

%files license
%defattr(-,root,root,-)
/usr/share/doc/clr-python-timestamp/COPYING
