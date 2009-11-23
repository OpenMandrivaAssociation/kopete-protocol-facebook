#
# spec file for package kopete-protocol-facebook
#
# Copyright (c) 2008 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild

%define gitrev 3376a46

Name:           kopete-protocol-facebook
License:        GPL v2 or later
Url:            http://github.com/dmacvicar/kopete-facebook
Group:          System/GUI/KDE
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Facebook Protocol support for Kopete
Version:        0.1.4
Release:        %mkrel 2
Source:         scvalex-kopete-facebook-%{gitrev}.tar.gz
Requires:	libqjson0
BuildRequires:  kdenetwork4-devel
BuildRequires:  libqjson-devel >= 0.6 

%description
Facebook Protocol Support for Kopete

%prep
%setup -n scvalex-kopete-facebook-%{gitrev}

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr -DKOPETE_FACEBOOK_OUTOFTREE=1 -DCMAKE_BUILD_TYPE=DebugFull  ..

%install
cd build
%makeinstall

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
#%doc AUTHORS COPYING
/usr/%_lib/kde4/kopete_facebook.so
/usr/share/apps/kopete/icons/*
#/usr/share/kde4/apps/kopete_facebook
/usr/share/kde4/services/kopete_facebook.desktop

