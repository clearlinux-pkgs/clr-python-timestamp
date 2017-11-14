#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-python-timestamp
Version  : 10
Release  : 20
URL      : http://localhost/cgit/projects/clr-python-timestamp/snapshot/clr-python-timestamp-10.tar.gz
Source0  : http://localhost/cgit/projects/clr-python-timestamp/snapshot/clr-python-timestamp-10.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: clr-python-timestamp-bin

%description
No detailed description available

%package bin
Summary: bin components for the clr-python-timestamp package.
Group: Binaries

%description bin
bin components for the clr-python-timestamp package.


%prep
%setup -q -n clr-python-timestamp-10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1510692400
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
%reconfigure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1510692400
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/clr-python-avx512
/usr/bin/clr-python-timestamp
