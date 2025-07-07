#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major 6
%define libname %mklibname KF6CalendarUtils
%define devname %mklibname KF6CalendarUtils -d

Name: kcalutils
Version:	25.04.3
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/kcalutils/-/archive/%{gitbranch}/kcalutils-%{gitbranchd}.tar.bz2#/kcalutils-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/kcalutils-%{version}.tar.xz
%endif
Summary: KDE calendar utility library
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6TextTemplate)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(PythonInterp)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KPim6Akonadi)
BuildRequires: %mklibname -d KF6IdentityManagement
BuildRequires: cmake(KF6Holidays)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6WidgetsAddons)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant
# Renamed 2025-05-25 after 6.0
%rename plasma6-kcalutils
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KDE calendar utility library.

%package -n %{libname}
Summary: KDE calendar utility library
Group: System/Libraries
# Not a 1:1 replacement, but we need to get rid of old cruft -- 2025-05-25 after 6.0
Obsoletes: %{mklibname KF5CalendarUtils 5}

%description -n %{libname}
KDE calendar utility library.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
# Not a 1:1 replacement, but we need to get rid of old cruft -- 2025-05-25 after 6.0
Obsoletes: %{mklibname -d KF5CalendarUtils}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kcalutils.categories
%{_datadir}/qlogging-categories6/kcalutils.renamecategories

%files -n %{libname}
%{_libdir}/*.so*
%{_qtdir}/plugins/kf6/ktexttemplate

%files -n %{devname}
%{_includedir}/*
%{_libdir}/cmake/*
