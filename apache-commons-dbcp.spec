%global pkg_name apache-commons-dbcp
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global base_name       dbcp
%global short_name      commons-%{base_name}

Name:             %{?scl_prefix}%{pkg_name}
Version:          1.4
Release:          17.7%{?dist}
Summary:          Apache Commons DataBase Pooling Package
License:          ASL 2.0
URL:              http://commons.apache.org/%{base_name}/
Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz

Patch0:           jdbc41.patch
BuildArch:        noarch

BuildRequires:    %{?scl_prefix}javapackages-tools
BuildRequires:    %{?scl_prefix}apache-commons-parent >= 26-7
BuildRequires:    %{?scl_prefix}apache-commons-pool
BuildRequires:    %{?scl_prefix}geronimo-parent-poms
BuildRequires:    %{?scl_prefix}geronimo-jta
BuildRequires:    %{?scl_prefix}maven-local


%description
Many Apache projects support interaction with a relational database. Creating a
new connection for each user can be time consuming (often requiring multiple
seconds of clock time), in order to perform a database transaction that might
take milliseconds. Opening a connection per user can be unfeasible in a
publicly-hosted Internet application where the number of simultaneous users can
be very large. Accordingly, developers often wish to share a "pool" of open
connections between all of the application's current users. The number of users
actually performing a request at any given time is usually a very small
percentage of the total number of active users, and during request processing
is the only time that a database connection is required. The application itself
logs into the DBMS, and handles any user account issues internally.

%package javadoc
Summary:          Javadoc for %{pkg_name}

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -q -n %{short_name}-%{version}-src
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
iconv -f iso8859-1 -t utf-8 RELEASE-NOTES.txt > RELEASE-NOTES.txt.conv && mv -f RELEASE-NOTES.txt.conv RELEASE-NOTES.txt

%patch0

%mvn_file : %{pkg_name} %{short_name}
%mvn_alias : org.apache.commons:%{short_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
# Skip tests, tomcat:naming-java and tomcat:naming-common not available
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt README.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-17.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-17.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-17.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-17.4
- Remove requires on java

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-17.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-17.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-17.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.4-17
- Mass rebuild 2013-12-27

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-16
- Add BuildRequires on apache-commons-parent >= 26-7

* Mon Aug 19 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-15
- Migrate away from mvn-rpmbuild (#997452)

* Fri Jul 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-14
- Remove workaround for rpm bug #646523

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-13
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4-11
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 23 2012 Pavel Tisnovsky <ptisnovs@redhat.com> - 1.4-9
- Make this package independent of OpenJDK6 (it's buildable on OpenJDK7)

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec  1 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-7
- Build with maven 3
- Fixes according to latest guidelines

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 9 2010 Chris Spike <chris.spike@arcor.de> 1.4-5
- Removed maven* BRs in favour of apache-commons-parent
- Added deprecated groupId to depmap for compatibility reasons
- Removed commons-pool from custom depmap

* Wed Oct 27 2010 Chris Spike <chris.spike@arcor.de> 1.4-4
- Added depmap entry to find commons-pool.jar

* Wed Oct 27 2010 Chris Spike <chris.spike@arcor.de> 1.4-3
- Added BR apache-commons-pool

* Mon Oct 18 2010 Chris Spike <chris.spike@arcor.de> 1.4-2
- Removed Epoch

* Mon Oct 4 2010 Chris Spike <chris.spike@arcor.de> 1.4-1
- Rename and rebase from jakarta-commons-dbcp
