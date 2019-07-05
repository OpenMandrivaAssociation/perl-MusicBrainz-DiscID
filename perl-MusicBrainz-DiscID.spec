%define upstream_name		MusicBrainz-DiscID
%define upstream_version 0.04

%{?perl_default_filter}

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Perl interface for the MusicBrainz libdiscid library
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MusicBrainz/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(libdiscid)

%description
MusicBrainz::DiscID is a class to calculate a MusicBrainz DiscID from an
audio CD in the drive. The coding style is slightly different to the C
interface to libdiscid, because it makes use of perl's Object Oriented
functionality.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%make_build

%install
%make_install

%files
%doc Changes META.yml README.md
%{_mandir}/man3/*
%{perl_vendorarch}/*
