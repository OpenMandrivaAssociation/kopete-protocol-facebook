%define gitrev 3376a46

Name:           kopete-protocol-facebook
License:        GPLv2+
Url:            http://github.com/dmacvicar/kopete-facebook
Group:          Networking/Instant messaging
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Facebook Protocol support for Kopete
Version:        0.1.4
Release:        %mkrel 5
Source:         scvalex-kopete-facebook-%{gitrev}.tar.gz
BuildRequires:  kdenetwork4-devel
BuildRequires:  libqjson-devel >= 0.6 

%description
Facebook Protocol Support for Kopete

%files
%defattr(-,root,root)
%_kde_libdir/kde4/kopete_facebook.so
%_kde_appsdir/kopete/icons/*
%_kde_datadir/kde4/services/kopete_facebook.desktop

#--------------------------------------------------------------------

%prep
%setup -n scvalex-kopete-facebook-%{gitrev}

%build
%cmake_kde4

%install
%makeinstall_std -C build 

%clean
rm -rf $RPM_BUILD_ROOT
