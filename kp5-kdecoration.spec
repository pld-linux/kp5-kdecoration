%define		kdeplasmaver	5.21.2
%define		qtver		5.9.0
%define		kpname		kdecoration
Summary:	A plugin-based library to create window decorations
Name:		kp5-%{kpname}
Version:	5.21.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	fa438382bf231647e5dfad701bbb3d44
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A plugin-based library to create window decorations.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

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
%attr(755,root,root) %ghost %{_libdir}/libkdecorations2.so.5
%attr(755,root,root) %{_libdir}/libkdecorations2private.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdecorations2private.so.8

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkdecorations2.so
%attr(755,root,root) %{_libdir}/libkdecorations2private.so
%{_includedir}/KDecoration2
%{_includedir}/KF5/kdecoration2_version.h
%{_libdir}/cmake/KDecoration2
