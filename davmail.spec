%define		rev	2331
Summary:	DavMail POP/IMAP/SMTP/Caldav/Carddav/LDAP Exchange Gateway
Name:		davmail
Version:	4.6.0
Release:	1
License:	GPL v2
Group:		Applications/Mail
Source0:	http://downloads.sourceforge.net/davmail/%{name}-linux-x86-%{version}-%{rev}.tgz
# Source0-md5:	1f0be0173b8f4cb5cf5accaac7b412b2
Source1:	http://downloads.sourceforge.net/davmail/%{name}-linux-x86_64-%{version}-%{rev}.tgz
# Source1-md5:	4d90a3d949dcb961ad21a406c4d9003a
Patch0:		%{name}-base.patch
URL:		http://davmail.sourceforge.net/
Requires:	jre
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DavMail is a POP/IMAP/SMTP/Caldav/Carddav/LDAP exchange gateway
allowing users to use any mail/calendar client (e.g. Thunderbird with
Lightning or Apple iCal) with an Exchange server, even from the
internet or behind a firewall through Outlook Web Access.

%prep
%setup -qcT
%ifarch %{ix86}
%{__tar} zxf %{SOURCE0} --strip-components=1
%endif
%ifarch %{x8664}
%{__tar} zxf %{SOURCE1} --strip-components=1
%endif
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}
ln -sf %{_datadir}/%{name}/davmail $RPM_BUILD_ROOT%{_bindir}/davmail

install -d $RPM_BUILD_ROOT
install -p davmail.sh $RPM_BUILD_ROOT%{_datadir}/%{name}/davmail
install -p davmail.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/davmail.jar
%{__cp} -a lib $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/davmail
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/davmail
%{_datadir}/%{name}/davmail.jar
%{_datadir}/%{name}/lib
