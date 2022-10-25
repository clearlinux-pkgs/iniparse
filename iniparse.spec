#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : iniparse
Version  : 5939e839bb8759bd2a0129bb298b5f01b1800508
Release  : 50
URL      : https://github.com/zeyosinc/iniparse/archive/5939e839bb8759bd2a0129bb298b5f01b1800508.tar.gz
Source0  : https://github.com/zeyosinc/iniparse/archive/5939e839bb8759bd2a0129bb298b5f01b1800508.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT Python-2.0
Requires: iniparse-license = %{version}-%{release}
Requires: iniparse-python = %{version}-%{release}
Requires: iniparse-python3 = %{version}-%{release}
Patch1: 0001-Autospec-the-package.patch

%description
Introduction to iniparse
iniparse is a INI parser for Python which is:
* Compatible with ConfigParser: Backward compatible implementations
of ConfigParser, RawConfigParser, and SafeConfigParser are included
that are API-compatible with the Python standard library.

%package license
Summary: license components for the iniparse package.
Group: Default

%description license
license components for the iniparse package.


%package python
Summary: python components for the iniparse package.
Group: Default
Requires: iniparse-python3 = %{version}-%{release}

%description python
python components for the iniparse package.


%package python3
Summary: python3 components for the iniparse package.
Group: Default
Requires: python3-core

%description python3
python3 components for the iniparse package.


%prep
%setup -q -n iniparse-5939e839bb8759bd2a0129bb298b5f01b1800508
cd %{_builddir}/iniparse-5939e839bb8759bd2a0129bb298b5f01b1800508
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635741819
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%autogen --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1635741819
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/iniparse
cp %{_builddir}/iniparse-5939e839bb8759bd2a0129bb298b5f01b1800508/LICENSE %{buildroot}/usr/share/package-licenses/iniparse/24d6fcdd5e29331140a7596cfed0f69389c89df3
cp %{_builddir}/iniparse-5939e839bb8759bd2a0129bb298b5f01b1800508/LICENSE-PSF %{buildroot}/usr/share/package-licenses/iniparse/a4fb8ddee4c297d495de4caa5aa45a567d30e0fa
%make_install

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/iniparse/24d6fcdd5e29331140a7596cfed0f69389c89df3
/usr/share/package-licenses/iniparse/a4fb8ddee4c297d495de4caa5aa45a567d30e0fa

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
