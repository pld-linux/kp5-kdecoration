#
# Conditional build:
%bcond_with	tests		# test suite

%define		kdeplasmaver	5.27.12
%define		qt_ver		5.15.2
%define		kf_ver		5.102.0
%define		kpname		kdecoration
Summary:	A plugin-based library to create window decorations
Summary(pl.UTF-8):	Oparta na wtyczkach biblioteka do tworzenia dekoracji okien
Name:		kp5-%{kpname}
Version:	5.27.12
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	f8f1d1c2b026e28dd6cff9e275ad81df
URL:		https://kde.org/
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Test-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	kf5-extra-cmake-modules >= %{kf_ver}
BuildRequires:	kf5-kcoreaddons-devel >= %{kf_ver}
BuildRequires:	kf5-ki18n-devel >= %{kf_ver}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	kf5-ki18n >= %{kf_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A plugin-based library to create window decorations.

%description -l pl.UTF-8
Oparta na wtyczkach biblioteka do tworzenia dekoracji okien.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qt_ver}
Requires:	Qt5Gui-devel >= %{qt_ver}

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libkdecorations2.so.*.*
%ghost %{_libdir}/libkdecorations2.so.5
%attr(755,root,root) %{_libdir}/libkdecorations2private.so.*.*
%ghost %{_libdir}/libkdecorations2private.so.10

%files devel
%defattr(644,root,root,755)
%{_libdir}/libkdecorations2.so
%{_libdir}/libkdecorations2private.so
%{_includedir}/KDecoration2
%{_includedir}/KF5/kdecoration2_version.h
%{_libdir}/cmake/KDecoration2
