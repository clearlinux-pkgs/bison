#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x0DDCAA3278D5264E (akim@gnu.org)
#
Name     : bison
Version  : 3.5.3
Release  : 42
URL      : https://mirrors.kernel.org/gnu/bison/bison-3.5.3.tar.xz
Source0  : https://mirrors.kernel.org/gnu/bison/bison-3.5.3.tar.xz
Source1  : https://mirrors.kernel.org/gnu/bison/bison-3.5.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: bison-bin = %{version}-%{release}
Requires: bison-data = %{version}-%{release}
Requires: bison-info = %{version}-%{release}
Requires: bison-license = %{version}-%{release}
Requires: bison-locales = %{version}-%{release}
Requires: bison-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : flex
BuildRequires : glibc-locale
BuildRequires : libxslt-bin
BuildRequires : valgrind

%description
This package contains the GNU Bison parser generator.
# Installation
## Build from git
Here are basic installation instructions for a repository checkout:

%package bin
Summary: bin components for the bison package.
Group: Binaries
Requires: bison-data = %{version}-%{release}
Requires: bison-license = %{version}-%{release}

%description bin
bin components for the bison package.


%package data
Summary: data components for the bison package.
Group: Data

%description data
data components for the bison package.


%package dev
Summary: dev components for the bison package.
Group: Development
Requires: bison-bin = %{version}-%{release}
Requires: bison-data = %{version}-%{release}
Provides: bison-devel = %{version}-%{release}
Requires: bison = %{version}-%{release}

%description dev
dev components for the bison package.


%package doc
Summary: doc components for the bison package.
Group: Documentation
Requires: bison-man = %{version}-%{release}
Requires: bison-info = %{version}-%{release}

%description doc
doc components for the bison package.


%package info
Summary: info components for the bison package.
Group: Default

%description info
info components for the bison package.


%package license
Summary: license components for the bison package.
Group: Default

%description license
license components for the bison package.


%package locales
Summary: locales components for the bison package.
Group: Default

%description locales
locales components for the bison package.


%package man
Summary: man components for the bison package.
Group: Default

%description man
man components for the bison package.


%prep
%setup -q -n bison-3.5.3
cd %{_builddir}/bison-3.5.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583790622
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
# test suite is not parallel-safe
make check

%install
export SOURCE_DATE_EPOCH=1583790622
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bison
cp %{_builddir}/bison-3.5.3/COPYING %{buildroot}/usr/share/package-licenses/bison/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install
%find_lang bison-gnulib
%find_lang bison-runtime
%find_lang bison

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bison
/usr/bin/yacc

%files data
%defattr(-,root,root,-)
/usr/share/bison/README.md
/usr/share/bison/bison-default.css
/usr/share/bison/m4sugar/foreach.m4
/usr/share/bison/m4sugar/m4sugar.m4
/usr/share/bison/skeletons/README-D.txt
/usr/share/bison/skeletons/bison.m4
/usr/share/bison/skeletons/c++-skel.m4
/usr/share/bison/skeletons/c++.m4
/usr/share/bison/skeletons/c-like.m4
/usr/share/bison/skeletons/c-skel.m4
/usr/share/bison/skeletons/c.m4
/usr/share/bison/skeletons/d-skel.m4
/usr/share/bison/skeletons/d.m4
/usr/share/bison/skeletons/glr.c
/usr/share/bison/skeletons/glr.cc
/usr/share/bison/skeletons/java-skel.m4
/usr/share/bison/skeletons/java.m4
/usr/share/bison/skeletons/lalr1.cc
/usr/share/bison/skeletons/lalr1.d
/usr/share/bison/skeletons/lalr1.java
/usr/share/bison/skeletons/location.cc
/usr/share/bison/skeletons/stack.hh
/usr/share/bison/skeletons/variant.hh
/usr/share/bison/skeletons/yacc.c
/usr/share/bison/xslt/bison.xsl
/usr/share/bison/xslt/xml2dot.xsl
/usr/share/bison/xslt/xml2text.xsl
/usr/share/bison/xslt/xml2xhtml.xsl

%files dev
%defattr(-,root,root,-)
/usr/share/aclocal/*.m4

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/bison/*

%files info
%defattr(0644,root,root,0755)
/usr/share/info/bison.info

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bison/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/bison.1
/usr/share/man/man1/yacc.1

%files locales -f bison-gnulib.lang -f bison-runtime.lang -f bison.lang
%defattr(-,root,root,-)

