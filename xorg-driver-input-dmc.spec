# http://lists.x.org/archives/xorg-devel/2009-February/000220.html
Summary:	X.org input driver for DMC FIT10 controller
Summary(pl.UTF-8):	Sterownik wejściowy X.org dla kontrolera DMC FIT10
Name:		xorg-driver-input-dmc
Version:	1.1.2
Release:	3.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-dmc-%{version}.tar.bz2
# Source0-md5:	91021ea8f3593221c0d9ee9cc14deb48
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.4
BuildRequires:	rpmbuild(macros) >= 1.389
%{?requires_xorg_xserver_xinput}
Requires:	xorg-xserver-server >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for DMC FIT10 controller.

%description -l pl.UTF-8
Sterownik wejściowy X.org dla kontrolera DMC FIT10.

%prep
%setup -q -n xf86-input-dmc-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/input/dmc_drv.so
%{_mandir}/man4/dmc.4*
