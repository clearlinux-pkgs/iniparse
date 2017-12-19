#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : iniparse
Version  : 5939839875920129298501.b1800508
Release  : 19
URL      : https://github.com/zeyosinc/iniparse/archive/5939e839bb8759bd2a0129bb298b5f01b1800508.tar.gz
Source0  : https://github.com/zeyosinc/iniparse/archive/5939e839bb8759bd2a0129bb298b5f01b1800508.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT Python-2.0
Requires: iniparse-python3
Requires: iniparse-python
BuildRequires : python-dev
BuildRequires : python3
Patch1: 0001-Autospec-the-package.patch

%description
Introduction to iniparse
iniparse is a INI parser for Python which is:
* Compatible with ConfigParser: Backward compatible implementations
of ConfigParser, RawConfigParser, and SafeConfigParser are included
that are API-compatible with the Python standard library.

%package python
Summary: python components for the iniparse package.
Group: Default
Requires: iniparse-python3

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
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507668265
%autogen --disable-static
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1507668265
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
