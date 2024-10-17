%define gitrev 3376a46

Summary:	Facebook Protocol support for Kopete
Name:		kopete-protocol-facebook
Version:	0.1.5
Release:	5
License:	GPLv2+
Group:		Networking/Instant messaging
Url:		https://github.com/dmacvicar/kopete-facebook
Source0:	dmacvicar-kopete-facebook-%{gitrev}.tar.gz
BuildRequires:	kopete-devel
BuildRequires:	pkgconfig(QJson)

%description
Facebook Protocol support for Kopete.

%files
%{_kde_libdir}/kde4/kopete_facebook.so
%{_kde_appsdir}/kopete/icons/*
%{_kde_services}/kopete_facebook.desktop

#--------------------------------------------------------------------

%prep
%setup -n dmacvicar-kopete-facebook-%{gitrev}

%build
%cmake_kde4

%install
%makeinstall_std -C build

