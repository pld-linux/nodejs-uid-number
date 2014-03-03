Summary:	Convert a username/group name to a UID/GID number
Name:		nodejs-uid-number
Version:	0.0.5
Release:	1
License:	ISC
Group:		Development/Libraries
URL:		https://github.com/isaacs/uid-number
Source0:	http://registry.npmjs.org/uid-number/-/uid-number-%{version}.tgz
# Source0-md5:	0fd62d3dae10069c234338fd1ffd0887
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert a username/group name to a UID/GID number

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/uid-number
cp -pr *.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/uid-number

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/uid-number
