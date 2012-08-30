
Name:    ffmpegthumbs 
Version: 4.9.0
Release: 1%{?dist}
Summary: KDE ffmpegthumbnailer service

License: GPLv2+
URL:     https://projects.kde.org/projects/kde/kdemultimedia/%{name}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: kdelibs4-devel >= %{version}
BuildRequires: libjpeg-devel
BuildRequires: pkgconfig(libavcodec) pkgconfig(libavformat) pkgconfig(libavutil) pkgconfig(libswscale)

Requires: kdelibs4%{?_isa} >= %{_kde4_version}

Provides: kffmpegthumbnailer = %{version}-%{release}
%if 0%{?fedora} && 0%{?fedora} < 19
Obsoletes: kdemultimedia-extras-freeworld < %{version}-%{release}
%endif
Provides: kdemultimedia-extras-freeworld = %{version}-%{release}

%description
KDE ffmpegthumbnailer service


%prep
%setup -q 


%build

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} \
  -DKDE4_BUILD_TESTS:BOOL=ON \
  ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}

make install/fast -C %{_target_platform} DESTDIR=%{buildroot}


%files
%doc COPYING
%{_kde4_libdir}/kde4/ffmpegthumbs.so
%{_kde4_datadir}/kde4/services/ffmpegthumbs.desktop


%changelog
* Thu Aug 30 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.0-1
- 4.9.0

* Mon Jun 18 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.90-4
- ffmpegthumbs

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 4.7.2-4
- Rebuilt for c++ ABI breakage

* Tue Feb 28 2012 Nicolas Chauvet <kwizart@gmail.com> - 4.7.2-3
- Rebuilt for x264/FFmpeg

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 4.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 01 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-1
- 4.7.2

* Mon Sep 26 2011 Nicolas Chauvet <kwizart@gmail.com> - 4.7.0-2
- Rebuilt for FFmpeg-0.8

* Fri Aug 12 2011 Magnus Tuominen magnus.tuominen@gmail.com> 4.7.0-1
- 4.7.0
- patch50 no longer needed

* Fri Apr 08 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.1-1
- 4.6.1

* Sun Jan 23 2011 Rex Dieter <rdieter@fedoraproject.org> - 4.6.0-1
- 4.6.0

* Thu Dec 09 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.85-1
- 4.5.85 (4.6beta2)
- drop Obsoletes/Provides ffmpegthumnailer

* Mon Nov 22 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.80-1
- 4.5.80 (4.6beta1)

* Mon Nov 22 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.3-2
- Obsoletes: ffmpegthumbnailer-devel too

* Thu Nov 18 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.3-1
- 4.5.3

* Fri Oct 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.2-1
- 4.5.2

* Sun Sep 19 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 4.5.1-2
- drop patch
- obsolete < 15

* Mon Sep 13 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 4.5.1-1
- first attempt on kdemultimedia-extras-freeworld
