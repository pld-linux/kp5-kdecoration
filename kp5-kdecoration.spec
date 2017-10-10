%define		kdeplasmaver	5.11.0
%define		qtver		5.3.2
%define		kpname		kdecoration
Summary:	A plugin-based library to create window decorations
Name:		kp5-%{kpname}
Version:	5.11.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	a1722142859b188df4f1d056c98e10ef
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
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
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libkdecorations2.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdecorations2.so.5
%attr(755,root,root) %{_libdir}/libkdecorations2private.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdecorations2private.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkdecorations2.so
%attr(755,root,root) %{_libdir}/libkdecorations2private.so
%{_includedir}/KDecoration2
%{_includedir}/KF5/kdecoration2_version.h
%{_libdir}/cmake/KDecoration2
