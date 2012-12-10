%define gitrev 3376a46

Summary:	Facebook Protocol support for Kopete
Name:		kopete-protocol-facebook
License:	GPLv2+
Url:		http://github.com/dmacvicar/kopete-facebook
Group:		Networking/Instant messaging
Version:	0.1.5
Release:	2
Source:		dmacvicar-kopete-facebook-%{gitrev}.tar.gz
BuildRequires:	kdenetwork4-devel
BuildRequires:	pkgconfig(QJson)

%description
Facebook Protocol Support for Kopete

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

