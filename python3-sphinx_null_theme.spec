Summary:	Null Theme for Sphinx
Name:		python3-sphinx_null_theme
Version:	1.0.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-null-theme/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-null-theme/sphinx_null_theme-%{version}.tar.gz
# Source0-md5:	f401a030382714abc641c2970fbd09ba
URL:		https://pypi.org/project/sphinx-null-theme/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A weird Sphinx theme with no appereance but functionaly only. Intented
to be used as parent theme by other ReadCraft themes.

%prep
%setup -q -n sphinx_null_theme-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%{py3_sitescriptdir}/sphinx_null_theme
%{py3_sitescriptdir}/sphinx_null_theme-%{version}.dist-info
