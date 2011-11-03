Summary:	rygel
Name:		rygel
Version:	0.12.5
Release:	1
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/rygel/0.12/%{name}-%{version}.tar.xz
# Source0-md5:	1a52accbbe8ccb178ab428e6c1abd7a3
Source1:	git-version-gen
URL:		http://live.gnome.org/Rygel
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1.11.1
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.26
BuildRequires:	gssdp-devel <= 0.12.9999
BuildRequires:	gssdp-devel >= 0.11.0
BuildRequires:	gstreamer-devel >= 0.10.23
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.28
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gupnp-av-devel <= 0.10.9999
BuildRequires:	gupnp-av-devel >= 0.9.0
BuildRequires:	gupnp-devel <= 0.18.9999
BuildRequires:	gupnp-devel >= 0.17.1
BuildRequires:	gupnp-dlna-devel <= 0.6.9999
BuildRequires:	gupnp-dlna-devel >= 0.5.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgee-devel <= 0.6.9999
BuildRequires:	libgee-devel >= 0.5.2
BuildRequires:	libsoup-devel <= 2.36.9999
BuildRequires:	libsoup-devel >= 2.34.0
BuildRequires:	libtool >= 2.2.6
BuildRequires:	libuuid-devel >= 1.41.3
BuildRequires:	libxslt-progs
BuildRequires:	sqlite3-devel >= 3.5
BuildRequires:	vala >= 0.11.6
BuildRequires:	vala-gssdp >= 0.9.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rygel is a collection of DLNA (UPnP AV) services (devices in UPnP
speak), implemented through a plug-in mechanism.

%package devel
Summary:	Rygel header files
Summary(pl.UTF-8):	Pliki nagłówkowe rygel
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Rygel header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe rygel.

%prep
%setup -q
install -m755 %{SOURCE1} build-aux/git-version-gen

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gst-launch-plugin \
	--enable-mediathek-plugin \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/rygel-1.0/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS
%attr(755,root,root) %{_bindir}/rygel
%attr(755,root,root) %{_bindir}/rygel-preferences
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rygel.conf
%attr(755,root,root) %{_libdir}/rygel-1.0/librygel-*.so
%{_desktopdir}/rygel-preferences.desktop
%{_desktopdir}/rygel.desktop
%{_datadir}/dbus-1/services/org.gnome.Rygel1.service
%{_datadir}/rygel
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man1/rygel.1*
%{_mandir}/man5/rygel.conf.5*

%files devel
%defattr(644,root,root,755)
%{_includedir}/rygel-1.0
%{_pkgconfigdir}/rygel-1.0.pc
%{_datadir}/vala/vapi/rygel-1.0.deps
%{_datadir}/vala/vapi/rygel-1.0.vapi
