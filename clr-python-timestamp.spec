#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-python-timestamp
Version  : 17
Release  : 36
URL      : http://localhost/cgit/projects/clr-python-timestamp/snapshot/clr-python-timestamp-17.tar.gz
Source0  : http://localhost/cgit/projects/clr-python-timestamp/snapshot/clr-python-timestamp-17.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: clr-python-timestamp-bin = %{version}-%{release}
Requires: clr-python-timestamp-license = %{version}-%{release}
Requires: clr-avx-tools
Requires: python3
Requires: usrbinpython
BuildRequires : clr-avx-tools
BuildRequires : python3
BuildRequires : usrbinpython

%description
No detailed description available

%package bin
Summary: bin components for the clr-python-timestamp package.
Group: Binaries
Requires: clr-python-timestamp-license = %{version}-%{release}

%description bin
bin components for the clr-python-timestamp package.


%package license
Summary: license components for the clr-python-timestamp package.
Group: Default

%description license
license components for the clr-python-timestamp package.


%prep
%setup -q -n clr-python-timestamp-17
cd %{_builddir}/clr-python-timestamp-17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585183954
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1585183954
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-python-timestamp
cp %{_builddir}/clr-python-timestamp-17/COPYING %{buildroot}/usr/share/package-licenses/clr-python-timestamp/04319952ed7b0f3b3a70ae4d5d9f954317b8f970
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/clr-python-timestamp

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-python-timestamp/04319952ed7b0f3b3a70ae4d5d9f954317b8f970
