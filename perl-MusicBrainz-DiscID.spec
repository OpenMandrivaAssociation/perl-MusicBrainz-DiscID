%define upstream_name MusicBrainz-DiscID
%undefine _debugsource_packages

%{?perl_default_filter}

Name:perl-%{upstream_name}
Version:0.06
Release:6

Summary:Perl interface for the MusicBrainz libdiscid library
License:MIT
Group:Development/Perl
Url:https://metacpan.org/dist/%{upstream_name}
Source0:https://cpan.metacpan.org/modules/by-module/MusicBrainz/%{upstream_name}-%{version}.tar.gz
Patch0:MusicBrainz-DiscID-0.06-parsexs-offsets.patch

BuildRequires:make
BuildRequires:perl(ExtUtils::CBuilder)
BuildRequires:perl(Module::Build)
BuildRequires:perl(Test)
BuildRequires:perl(Test::More)
BuildRequires:perl-devel
BuildRequires:pkgconfig(libdiscid)

Obsoletes: %{name} = 0.60.0-1

%description
MusicBrainz::DiscID is a class to calculate a MusicBrainz DiscID from an
audio CD in the drive.

%prep
%setup -qn %{upstream_name}-%{version}
%patch 0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc Changes META.yml README.md
%{_mandir}/man3/*
%{perl_vendorarch}/*
