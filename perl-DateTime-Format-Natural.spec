#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v3
# autospec commit: 750e50d
#
Name     : perl-DateTime-Format-Natural
Version  : 1.18
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/S/SC/SCHUBIGER/DateTime-Format-Natural-1.18.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SC/SCHUBIGER/DateTime-Format-Natural-1.18.tar.gz
Summary  : 'Parse informal natural language date/time strings'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-DateTime-Format-Natural-bin = %{version}-%{release}
Requires: perl-DateTime-Format-Natural-man = %{version}-%{release}
Requires: perl-DateTime-Format-Natural-perl = %{version}-%{release}
Requires: perl(DateTime::HiRes)
BuildRequires : buildreq-cpan
BuildRequires : perl(Clone)
BuildRequires : perl(DateTime)
BuildRequires : perl(DateTime::HiRes)
BuildRequires : perl(DateTime::TimeZone)
BuildRequires : perl(List::MoreUtils)
BuildRequires : perl(Module::Util)
BuildRequires : perl(Params::Validate)
BuildRequires : perl(Test::MockTime::HiRes)
BuildRequires : perl(boolean)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
DateTime::Format::Natural - Parse informal natural language date/time
strings

%package bin
Summary: bin components for the perl-DateTime-Format-Natural package.
Group: Binaries

%description bin
bin components for the perl-DateTime-Format-Natural package.


%package dev
Summary: dev components for the perl-DateTime-Format-Natural package.
Group: Development
Requires: perl-DateTime-Format-Natural-bin = %{version}-%{release}
Provides: perl-DateTime-Format-Natural-devel = %{version}-%{release}
Requires: perl-DateTime-Format-Natural = %{version}-%{release}

%description dev
dev components for the perl-DateTime-Format-Natural package.


%package man
Summary: man components for the perl-DateTime-Format-Natural package.
Group: Default

%description man
man components for the perl-DateTime-Format-Natural package.


%package perl
Summary: perl components for the perl-DateTime-Format-Natural package.
Group: Default
Requires: perl-DateTime-Format-Natural = %{version}-%{release}

%description perl
perl components for the perl-DateTime-Format-Natural package.


%prep
%setup -q -n DateTime-Format-Natural-1.18
cd %{_builddir}/DateTime-Format-Natural-1.18
pushd ..
cp -a DateTime-Format-Natural-1.18 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dateparse

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DateTime::Format::Natural.3
/usr/share/man/man3/DateTime::Format::Natural::Calc.3
/usr/share/man/man3/DateTime::Format::Natural::Compat.3
/usr/share/man/man3/DateTime::Format::Natural::Duration.3
/usr/share/man/man3/DateTime::Format::Natural::Expand.3
/usr/share/man/man3/DateTime::Format::Natural::Extract.3
/usr/share/man/man3/DateTime::Format::Natural::Formatted.3
/usr/share/man/man3/DateTime::Format::Natural::Helpers.3
/usr/share/man/man3/DateTime::Format::Natural::Lang::Base.3
/usr/share/man/man3/DateTime::Format::Natural::Lang::EN.3
/usr/share/man/man3/DateTime::Format::Natural::Rewrite.3
/usr/share/man/man3/DateTime::Format::Natural::Test.3
/usr/share/man/man3/DateTime::Format::Natural::Utils.3
/usr/share/man/man3/DateTime::Format::Natural::Wrappers.3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dateparse.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
