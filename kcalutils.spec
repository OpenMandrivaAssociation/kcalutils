%define major 5
%define libname %mklibname KF5CalendarUtils %{major}
%define devname %mklibname KF5CalendarUtils -d

Name: kcalutils
Version:	20.12.2
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE calendar utility library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Grantlee5)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(PythonInterp)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5Akonadi)
BuildRequires: cmake(KF5CalendarCore)
BuildRequires: cmake(KF5IdentityManagement)
BuildRequires: cmake(KF5Holidays)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(KF5CalendarCore)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5IdentityManagement)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5WidgetsAddons)


%description
KDE calendar utility library.

%package -n %{libname}
Summary: KDE calendar utility library
Group: System/Libraries

%description -n %{libname}
KDE calendar utility library.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libkcalutils5

%files -f libkcalutils5.lang
%{_datadir}/qlogging-categories5/kcalutils.categories
%{_datadir}/qlogging-categories5/kcalutils.renamecategories
%{_libdir}/grantlee/*/kcalendar_grantlee_plugin.so

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
