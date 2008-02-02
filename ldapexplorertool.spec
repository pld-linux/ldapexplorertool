#TODO: wx-config is now in two files :wx-gtk2-ansi-config,wx-x11univ-ansi-config
Summary:	LDAPExplorerTool is a multi-platform LDAP browser and editor (GUI).
Name:		ldapexplorertool
Version:	2.0.1
Release:	0.1
License:	BSD
Group:		Applications
Source0:	http://dl.sourceforge.net/ldaptool/%{name}-%{version}.tar.gz
# Source0-md5:	edeb4c2ec779675925a57b4d4c4fc329
Patch0:		%{name}-inc-path.patch
Patch1:		%{name}-wx28.patch
URL:		http://ldaptool.sourceforge.net/
BuildRequires:	wxWidgets-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LDAPExplorerTool is a multi-platform LDAP browser and editor (GUI)
for Windows and Linux.

Main features are:
* SSL/TLS support
* Full UNICODE support
* Create/edit/remove LDAP objects
* Multivalue support (including edition)

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build

%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install src/ldapexplorertool2 $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}2
%{_datadir}/%{name}2
