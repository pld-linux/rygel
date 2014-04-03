Summary:	Rygel - collection of DLNA (UPnP AV) services
Summary(pl.UTF-8):	Rygel - zbiór usług DLNA (UPnP AV)
Name:		rygel
Version:	0.22.0
Release:	2
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/rygel/0.22/%{name}-%{version}.tar.xz
# Source0-md5:	5d9b818d7bbc6c201b69d9194ee0dfa8
Source1:	git-version-gen
Patch0:		gtk-doc.patch
Patch1:		%{name}-valadoc-workaround.patch
URL:		http://live.gnome.org/Rygel
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.34.0
BuildRequires:	gssdp-devel >= 0.13.0
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gupnp-av-devel >= 0.12.4
BuildRequires:	gupnp-devel >= 0.19.0
BuildRequires:	gupnp-dlna-devel >= 0.9.4
BuildRequires:	gupnp-dlna-gst-devel >= 0.9.4
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgee-devel >= 0.8.0
BuildRequires:	libsoup-devel >= 2.42.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libunistring-devel
BuildRequires:	libuuid-devel >= 1.41.3
BuildRequires:	libxml2-devel >= 1:2.7
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel >= 3.5
BuildRequires:	tracker-devel >= 1.0
BuildRequires:	vala >= 2:0.22.0
BuildRequires:	vala-gupnp >= 0.19.0
BuildRequires:	vala-gupnp-av >= 0.12.4
BuildRequires:	valadoc >= 0.2
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	glib2 >= 1:2.34.0
Requires:	gssdp >= 0.13.0
Requires:	gstreamer >= 1.0.0
Requires:	gtk+3 >= 3.0.0
Requires:	gupnp >= 0.19.0
Requires:	gupnp-av >= 0.12.4
Requires:	gupnp-dlna >= 0.9.4
Requires:	gupnp-dlna-gst >= 0.9.4
Requires:	libgee >= 0.8.0
Requires:	libsoup >= 2.42.0
Requires:	libuuid >= 1.41.3
Requires:	libxml2 >= 1:2.7
Requires:	sqlite3 >= 3.5
Requires:	tracker-libs >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rygel is a collection of DLNA (UPnP AV) services (devices in UPnP
speak), implemented through a plug-in mechanism.

%description -l pl.UTF-8
Rygel to zbiór usług (urządzeń w języku UPnP) DLNA (UPnP AV),
zaimplementowany poprzez mechanizm wtyczek.

%package devel
Summary:	Rygel header files
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Rygel
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.34.0
Requires:	gstreamer-devel >= 1.0.0
Requires:	gupnp-av-devel >= 0.12.4
Requires:	libgee-devel >= 0.8.0
Requires:	libuuid-devel >= 1.41.3

%description devel
Rygel header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Rygel.

%package apidocs
Summary:	API documentation for Rygel libraries
Summary(pl.UTF-8):	Dokumentacja API bibliotek Rygel
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for Rygel libraries.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek Rygel.

%package -n vala-rygel
Summary:	Vala API for Rygel libraries
Summary(pl.UTF-8):	API języka Vala do bibliotek Rygel
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.22.0
Requires:	vala-gupnp >= 0.19.0
Requires:	vala-gupnp-av >= 0.12.4
Requires:	vala-libgee >= 0.8.0

%description -n vala-rygel
Vala API for Rygel libraries.

%description -n vala-rygel -l pl.UTF-8
API języka Vala do bibliotek Rygel.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
#install -m755 %{SOURCE1} build-aux/git-version-gen

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
	--disable-silent-rules \
	--disable-valadoc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/rygel-2.2/*/*.la \
	$RPM_BUILD_ROOT%{_libdir}/*.la

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
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/rygel
%attr(755,root,root) %{_bindir}/rygel-preferences
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rygel.conf
%attr(755,root,root) %{_libdir}/librygel-core-2.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librygel-core-2.2.so.2
%attr(755,root,root) %{_libdir}/librygel-renderer-2.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librygel-renderer-2.2.so.2
%attr(755,root,root) %{_libdir}/librygel-renderer-gst-2.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librygel-renderer-gst-2.2.so.2
%attr(755,root,root) %{_libdir}/librygel-server-2.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librygel-server-2.2.so.2
%dir %{_libdir}/rygel-2.2
%dir %{_libdir}/rygel-2.2/engines
%attr(755,root,root) %{_libdir}/rygel-2.2/engines/librygel-media-engine-gst.so
%{_libdir}/rygel-2.2/engines/media-engine-gst.plugin
%attr(755,root,root) %{_libdir}/rygel-2.2/engines/librygel-media-engine-simple.so
%{_libdir}/rygel-2.2/engines/media-engine-simple.plugin
%dir %{_libdir}/rygel-2.2/plugins
%attr(755,root,root) %{_libdir}/rygel-2.2/plugins/librygel-external.so
%{_libdir}/rygel-2.2/plugins/external.plugin
%attr(755,root,root) %{_libdir}/rygel-2.2/plugins/librygel-gst-launch.so
%{_libdir}/rygel-2.2/plugins/gst-launch.plugin
%attr(755,root,root) %{_libdir}/rygel-2.2/plugins/librygel-media-export.so
%{_libdir}/rygel-2.2/plugins/media-export.plugin
%attr(755,root,root) %{_libdir}/rygel-2.2/plugins/librygel-mediathek.so
%{_libdir}/rygel-2.2/plugins/mediathek.plugin
%attr(755,root,root) %{_libdir}/rygel-2.2/plugins/librygel-mpris.so
%{_libdir}/rygel-2.2/plugins/mpris.plugin
%attr(755,root,root) %{_libdir}/rygel-2.2/plugins/librygel-tracker.so
%{_libdir}/rygel-2.2/plugins/tracker.plugin
%attr(755,root,root) %{_libdir}/rygel-2.2/plugins/librygel-playbin.so
%{_libdir}/rygel-2.2/plugins/playbin.plugin
%{_desktopdir}/rygel-preferences.desktop
%{_desktopdir}/rygel.desktop
%{_datadir}/dbus-1/services/org.gnome.Rygel1.service
%{_datadir}/rygel
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man1/rygel.1*
%{_mandir}/man5/rygel.conf.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librygel-core-2.2.so
%attr(755,root,root) %{_libdir}/librygel-renderer-2.2.so
%attr(755,root,root) %{_libdir}/librygel-renderer-gst-2.2.so
%attr(755,root,root) %{_libdir}/librygel-server-2.2.so
%dir %{_includedir}/rygel-2.2
%{_includedir}/rygel-2.2/rygel-core.h
%{_includedir}/rygel-2.2/rygel-renderer-gst.h
%{_includedir}/rygel-2.2/rygel-renderer.h
%{_includedir}/rygel-2.2/rygel-server.h
%{_pkgconfigdir}/rygel-core-2.2.pc
%{_pkgconfigdir}/rygel-renderer-2.2.pc
%{_pkgconfigdir}/rygel-renderer-gst-2.2.pc
%{_pkgconfigdir}/rygel-server-2.2.pc

%files -n vala-rygel
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/rygel-core-2.2.deps
%{_datadir}/vala/vapi/rygel-core-2.2.vapi
%{_datadir}/vala/vapi/rygel-renderer-2.2.deps
%{_datadir}/vala/vapi/rygel-renderer-2.2.vapi
%{_datadir}/vala/vapi/rygel-renderer-gst-2.2.deps
%{_datadir}/vala/vapi/rygel-renderer-gst-2.2.vapi
%{_datadir}/vala/vapi/rygel-server-2.2.deps
%{_datadir}/vala/vapi/rygel-server-2.2.vapi

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/librygel-core
%{_gtkdocdir}/librygel-renderer
%{_gtkdocdir}/librygel-renderer-gst
%{_gtkdocdir}/librygel-server
