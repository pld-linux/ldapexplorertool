Summary:	A free multi-platform LDAP client
Summary(pl.UTF-8):	Wolny wieloplatformowy klient LDAP
Name:		ldapexplorertool
Version:	2.0.1
Release:	1
License:	BSD
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/ldaptool/%{name}-%{version}.tar.gz
# Source0-md5:	edeb4c2ec779675925a57b4d4c4fc329
Patch0:		%{name}-inc-path.patch
Patch1:		%{name}-wx28.patch
URL:		http://ldaptool.sourceforge.net/
BuildRequires:	openldap-devel
BuildRequires:	wxWidgets-devel
Obsoletes:	LDAPExplorerTool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LDAP Explorer Tool is a free LDAP client, that enables the user to
manage LDAP directories. With this tool you can view, edit or delete
any entry of the LDAP server. You can also manage the schema, export
and import entries using the LDIF format. LDAP Explorer aims to run on
mutliple platforms like Windows, Linux, Solaris, Mac OS X...

%description -l pl.UTF-8
LDAP Explorer Tool jest wolnodostępnym klientem LDAP umożliwiającym
użytkownikowi zarządzanie katalogami LDAP. Przy użyciu tego narzędzia
można przeglądać, modyfikować i usuwać dowolne wpisy serwera LDAP.
Można też zarządzać schematami, eksportować i importować wpisy
korzystając z formatu LDIF. LDAP Explorer może działać na takich
platformach jak Windows, Linux, Solaris, Mac OS X...

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
