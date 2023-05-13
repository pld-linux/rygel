# TODO: split some plugins? (gstreamer?)
#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	tracker2	# tracker2 plugin

Summary:	Rygel - collection of DLNA (UPnP AV) services
Summary(pl.UTF-8):	Rygel - zbiór usług DLNA (UPnP AV)
Name:		rygel
Version:	0.42.3
Release:	1
License:	LGPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/rygel/0.42/%{name}-%{version}.tar.xz
# Source0-md5:	4c4f54a5f20df33fd165de7d31da6005
Patch0:		gtk-doc.patch
Patch1:		%{name}-pc.patch
URL:		https://wiki.gnome.org/Projects/Rygel
BuildRequires:	docbook-style-xsl-nons
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gettext-tools >= 0.19.7
BuildRequires:	glib2-devel >= 1:2.62
BuildRequires:	gobject-introspection-devel >= 1.33.4
BuildRequires:	gssdp1.6-devel >= 1.5.0
BuildRequires:	gstreamer-devel >= 1.20
BuildRequires:	gstreamer-editing-services-devel >= 1.16
# audio,pbutils,tag,video components
BuildRequires:	gstreamer-plugins-base-devel >= 1.20
BuildRequires:	gtk+3-devel >= 3.22
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.0}
BuildRequires:	gupnp-av-devel >= 0.14.1
BuildRequires:	gupnp-dlna-devel >= 0.9.4
BuildRequires:	gupnp-dlna-gst-devel >= 0.9.4
BuildRequires:	gupnp1.6-devel >= 1.5.2
BuildRequires:	libgee-devel >= 0.8.0
BuildRequires:	libmediaart2-devel >= 0.7.0
BuildRequires:	libsoup3-devel >= 2.44.0
BuildRequires:	libunistring-devel
BuildRequires:	libxml2-devel >= 1:2.7
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.58.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel >= 3.5
BuildRequires:	tar >= 1:1.22
%{?with_tracker2:BuildRequires:	tracker-devel >= 2.0}
BuildRequires:	tracker3-devel >= 3.0
BuildRequires:	vala >= 2:0.53.2
BuildRequires:	vala-gupnp-av >= 0.14.1
BuildRequires:	vala-gupnp-dlna >= 0.9.4
BuildRequires:	vala-gupnp-dlna-gst >= 0.9.4
BuildRequires:	vala-gupnp1.6 >= 1.5.2
BuildRequires:	vala-libgee >= 0.8.0
BuildRequires:	vala-libmediaart2 >= 0.7.0
BuildRequires:	vala-tracker3 >= 3.0
BuildRequires:	valadoc >= 0.2
BuildRequires:	xz
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gstreamer >= 1.20
Requires:	gstreamer-editing-services >= 1.16
Requires:	gtk+3 >= 3.22
Requires:	gupnp-dlna >= 0.9.4
Requires:	gupnp-dlna-gst >= 0.9.4
Requires:	systemd-units >= 38
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rygel is a collection of DLNA (UPnP AV) services (devices in UPnP
speak), implemented through a plug-in mechanism.

%description -l pl.UTF-8
Rygel to zbiór usług (urządzeń w języku UPnP) DLNA (UPnP AV),
zaimplementowany poprzez mechanizm wtyczek.

%package libs
Summary:	Rygel shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone Rygela
Group:		Libraries
Requires:	glib2 >= 1:2.62
Requires:	gssdp1.6 >= 1.5.0
Requires:	gupnp-av >= 0.14.1
Requires:	gupnp1.6 >= 1.5.2
Requires:	libgee >= 0.8.0
Requires:	libmediaart2 >= 0.7.0
Requires:	libsoup3 >= 2.44.0
Requires:	libxml2 >= 1:2.7
Requires:	sqlite3 >= 3.5
Conflicts:	rygel < 0.32

%description libs
Rygel shared libraries.

%description libs -l pl.UTF-8
Biblioteki współdzielone Rygela.

%package devel
Summary:	Rygel header files
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Rygel
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.62
Requires:	gstreamer-devel >= 1.20
Requires:	gupnp-av-devel >= 0.14.1
Requires:	libgee-devel >= 0.8.0

%description devel
Rygel header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Rygel.

%package apidocs
Summary:	API documentation for Rygel libraries
Summary(pl.UTF-8):	Dokumentacja API bibliotek Rygel
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Rygel libraries.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek Rygel.

%package -n vala-rygel
Summary:	Vala API for Rygel libraries
Summary(pl.UTF-8):	API języka Vala do bibliotek Rygel
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.40.10
Requires:	vala-gupnp-av >= 0.14.1
Requires:	vala-gupnp1.6 >= 1.5.2
Requires:	vala-libgee >= 0.8.0
BuildArch:	noarch

%description -n vala-rygel
Vala API for Rygel libraries.

%description -n vala-rygel -l pl.UTF-8
API języka Vala do bibliotek Rygel.

%package plugins
Summary:	Plugins for the Rygel media server
Summary(pl.UTF-8):	Wtyczki dla serwera mediów Rygel
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugins
Plugins for the Rygel UPnP/DLNA media server.

%description plugins -l pl.UTF-8
Wtyczki dla serwera mediów UPnP/DLNA Rygel

%package plugin-tracker
Summary:	tracker plugin for the Rygel media server
Summary(pl.UTF-8):	Wtyczka tracker dla serwera mediów Rygel
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	tracker-libs >= 2.0

%description plugin-tracker
Tracker plugin for the Rygel UPnP/DLNA media server.

%description plugin-tracker -l pl.UTF-8
Wtyczka tracker dla serwera mediów UPnP/DLNA Rygel

%package plugin-tracker3
Summary:	tracker3 plugin for the Rygel media server
Summary(pl.UTF-8):	Wtyczka tracker3 dla serwera mediów Rygel
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	tracker3-libs >= 3.0

%description plugin-tracker3
Tracker3 plugin for the Rygel UPnP/DLNA media server.

%description plugin-tracker3 -l pl.UTF-8
Wtyczka tracker3 dla serwera mediów UPnP/DLNA Rygel

%prep
%setup -q
%patch0 -p1
#patch1 -p1

%if %{with tracker2}
# tracker[2] plugin is still present, but not in choices
%{__sed} -i -e "/'plugins'/ s/]/, 'tracker']/" meson_options.txt
%endif

%build
%meson build \
	--default-library=shared \
	%{?with_apidocs:-Dapi-docs=true} \
	-Dexamples=false \
	-Dsystemd-user-units-dir=%{systemduserunitdir}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING.logo NEWS README.md
%attr(755,root,root) %{_bindir}/rygel
%attr(755,root,root) %{_bindir}/rygel-preferences
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rygel.conf
%dir %{_libexecdir}/rygel
%attr(755,root,root) %{_libexecdir}/rygel/mx-extract
%dir %{_libdir}/rygel-2.8
%dir %{_libdir}/rygel-2.8/engines
%attr(755,root,root) %{_libdir}/rygel-2.8/engines/librygel-media-engine-gst.so
%{_libdir}/rygel-2.8/engines/media-engine-gst.plugin
%attr(755,root,root) %{_libdir}/rygel-2.8/engines/librygel-media-engine-simple.so
%{_libdir}/rygel-2.8/engines/media-engine-simple.plugin
%{systemduserunitdir}/rygel.service
%{_desktopdir}/rygel-preferences.desktop
%{_desktopdir}/rygel.desktop
%{_datadir}/dbus-1/services/org.gnome.Rygel1.service
%{_datadir}/rygel
%{_iconsdir}/hicolor/*x*/apps/rygel.png
%{_iconsdir}/hicolor/scalable/apps/rygel.svg
%{_iconsdir}/hicolor/scalable/apps/rygel-full.svg
%{_mandir}/man1/rygel.1*
%{_mandir}/man5/rygel.conf.5*

%files plugins
%defattr(644,root,root,755)
%dir %{_libdir}/rygel-2.8/plugins
%attr(755,root,root) %{_libdir}/rygel-2.8/plugins/librygel-external.so
%{_libdir}/rygel-2.8/plugins/external.plugin
%attr(755,root,root) %{_libdir}/rygel-2.8/plugins/librygel-gst-launch.so
%{_libdir}/rygel-2.8/plugins/gst-launch.plugin
%attr(755,root,root) %{_libdir}/rygel-2.8/plugins/librygel-lms.so
%{_libdir}/rygel-2.8/plugins/lms.plugin
%attr(755,root,root) %{_libdir}/rygel-2.8/plugins/librygel-media-export.so
%{_libdir}/rygel-2.8/plugins/media-export.plugin
%attr(755,root,root) %{_libdir}/rygel-2.8/plugins/librygel-mpris.so
%{_libdir}/rygel-2.8/plugins/mpris.plugin
%attr(755,root,root) %{_libdir}/rygel-2.8/plugins/librygel-playbin.so
%{_libdir}/rygel-2.8/plugins/playbin.plugin
%attr(755,root,root) %{_libdir}/rygel-2.8/plugins/librygel-ruih.so
%{_libdir}/rygel-2.8/plugins/ruih.plugin

%if %{with tracker2}
%files plugin-tracker
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/rygel-2.8/plugins/librygel-tracker.so
%{_libdir}/rygel-2.8/plugins/tracker.plugin
%endif

%files plugin-tracker3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/rygel-2.8/plugins/librygel-tracker3.so
%{_libdir}/rygel-2.8/plugins/tracker3.plugin

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librygel-core-2.8.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librygel-core-2.8.so.0
%attr(755,root,root) %{_libdir}/librygel-db-2.8.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librygel-db-2.8.so.0
%attr(755,root,root) %{_libdir}/librygel-renderer-2.8.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librygel-renderer-2.8.so.0
%attr(755,root,root) %{_libdir}/librygel-renderer-gst-2.8.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librygel-renderer-gst-2.8.so.0
%attr(755,root,root) %{_libdir}/librygel-ruih-2.8.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librygel-ruih-2.8.so.0
%attr(755,root,root) %{_libdir}/librygel-server-2.8.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librygel-server-2.8.so.0
%{_libdir}/girepository-1.0/RygelCore-2.8.typelib
%{_libdir}/girepository-1.0/RygelRenderer-2.8.typelib
%{_libdir}/girepository-1.0/RygelRendererGst-2.8.typelib
%{_libdir}/girepository-1.0/RygelServer-2.8.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librygel-core-2.8.so
%attr(755,root,root) %{_libdir}/librygel-db-2.8.so
%attr(755,root,root) %{_libdir}/librygel-renderer-2.8.so
%attr(755,root,root) %{_libdir}/librygel-renderer-gst-2.8.so
%attr(755,root,root) %{_libdir}/librygel-ruih-2.8.so
%attr(755,root,root) %{_libdir}/librygel-server-2.8.so
%{_datadir}/gir-1.0/RygelCore-2.8.gir
%{_datadir}/gir-1.0/RygelRenderer-2.8.gir
%{_datadir}/gir-1.0/RygelRendererGst-2.8.gir
%{_datadir}/gir-1.0/RygelServer-2.8.gir
%dir %{_includedir}/rygel-2.8
%{_includedir}/rygel-2.8/rygel-core.h
%{_includedir}/rygel-2.8/rygel-db.h
%{_includedir}/rygel-2.8/rygel-renderer-gst.h
%{_includedir}/rygel-2.8/rygel-renderer.h
%{_includedir}/rygel-2.8/rygel-ruih.h
%{_includedir}/rygel-2.8/rygel-server.h
%{_pkgconfigdir}/rygel-core-2.8.pc
%{_pkgconfigdir}/rygel-renderer-2.8.pc
%{_pkgconfigdir}/rygel-renderer-gst-2.8.pc
%{_pkgconfigdir}/rygel-ruih-2.8.pc
%{_pkgconfigdir}/rygel-server-2.8.pc

%files -n vala-rygel
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/rygel-core-2.8.deps
%{_datadir}/vala/vapi/rygel-core-2.8.vapi
%{_datadir}/vala/vapi/rygel-db-2.8.deps
%{_datadir}/vala/vapi/rygel-db-2.8.vapi
%{_datadir}/vala/vapi/rygel-renderer-2.8.deps
%{_datadir}/vala/vapi/rygel-renderer-2.8.vapi
%{_datadir}/vala/vapi/rygel-renderer-gst-2.8.deps
%{_datadir}/vala/vapi/rygel-renderer-gst-2.8.vapi
%{_datadir}/vala/vapi/rygel-ruih-2.8.deps
%{_datadir}/vala/vapi/rygel-ruih-2.8.vapi
%{_datadir}/vala/vapi/rygel-server-2.8.deps
%{_datadir}/vala/vapi/rygel-server-2.8.vapi

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/librygel-core
%{_gtkdocdir}/librygel-db
%{_gtkdocdir}/librygel-renderer
%{_gtkdocdir}/librygel-renderer-gst
%{_gtkdocdir}/librygel-server
