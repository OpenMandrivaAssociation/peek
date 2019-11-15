Name:           peek
Version:        1.3.1
Release:        1
Summary:        Simple animated GIF screen recorder with an easy to use interface
Group:          Video/Utilities
License:        GPLv3
URL:            https://github.com/phw/peek
Source0:        https://github.com/phw/peek/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(keybinder-3.0)
BuildRequires:  pkgconfig(vapigen)

Requires:       ffmpeg
Requires:       imagemagick
Requires:       gstreamer1.0-plugins-good
Recommends:     gstreamer1.0-plugins-bad

%description
A simple tool that allows you to record short animated GIF images
from your screen.

%prep
%autosetup

%build
%cmake -DBUILD_TESTS=OFF
%make_build

%install
%make_install -C build

%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/com.uploadedlobster.%{name}.desktop
%{_datadir}/dbus-1/services/com.uploadedlobster.%{name}.service
%{_datadir}/glib-2.0/schemas/com.uploadedlobster.%{name}.gschema.xml
%{_datadir}/metainfo/com.uploadedlobster.%{name}.appdata.xml
%{_iconsdir}/hicolor/*/apps/com.uploadedlobster.%{name}.png
