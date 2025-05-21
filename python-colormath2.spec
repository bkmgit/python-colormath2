%global         srcname         python-colormath2
%global         shortname       colormath2
%global         forgeurl        https://github.com/bkmgit/python-colormath2
Version:        3.0.3

Name:           %{srcname}
Release:        %{autorelease}
Summary:        A python module that abstracts common color math operations

License:        BSD-3-Clause
URL:            %forgeurl
Source:         %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          cie2000-calculation.patch

BuildRequires:  python3-devel
BuildRequires:  python3-nose2
BuildRequires:  python3-tox
BuildRequires:  python3-tox-current-env

BuildArch: noarch

%global _description %{expand:
This module implements a large number of different color operations
such as color space conversions, Delta E, and density to spectral.
}

%description %_description

%package -n python3-%{shortname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{shortname}}

%description -n python3-%{shortname} %_description


%prep
%autosetup -n %{srcname}-%{version} -p 1

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{shortname}

%check
%pyproject_check_import
%tox

%files -n python3-%{shortname} -f %{pyproject_files}
 
%changelog
%autochangelog
