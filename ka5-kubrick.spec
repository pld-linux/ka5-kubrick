%define		kdeappsver	21.04.2
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kubrick
Summary:	kubrick
Summary(pl.UTF-8):	kubrick
Name:		ka5-%{kaname}
Version:	21.04.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	8b77ee265df2fcff5a8bbc2d2c7769dd
URL:		http://www.kde.org/
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5OpenGL-devel
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kubrick is a game based on the Rubik's Cube™ puzzle. The cube sizes
range from 2x2x2 up to 6x6x6, or you can play with irregular "bricks"
such as 5x3x2 or "mats" such as 6x4x1 or 2x2x1. The game has a
selection of puzzles at several levels of difficulty, as well as demos
of pretty patterns and solution moves, or you can make up your own
puzzles.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kubrick
%{_desktopdir}/org.kde.kubrick.desktop
%{_iconsdir}/hicolor/128x128/apps/kubrick.png
%{_iconsdir}/hicolor/16x16/apps/kubrick.png
%{_iconsdir}/hicolor/22x22/apps/kubrick.png
%{_iconsdir}/hicolor/32x32/apps/kubrick.png
%{_iconsdir}/hicolor/48x48/apps/kubrick.png
%{_iconsdir}/hicolor/64x64/apps/kubrick.png
%{_datadir}/kubrick
%dir %{_datadir}/kxmlgui5/kubrick
%{_datadir}/kxmlgui5/kubrick/kubrickui.rc
%{_datadir}/metainfo/org.kde.kubrick.appdata.xml
%{_datadir}/qlogging-categories5/kubrick.categories
