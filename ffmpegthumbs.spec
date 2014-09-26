
Name:    ffmpegthumbs 
Version: 4.13.97
Release: 2%{?dist}
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

BuildRequires: kdelibs4-devel
BuildRequires: libjpeg-devel
BuildRequires: pkgconfig(libavcodec) pkgconfig(libavformat) pkgconfig(libavutil) pkgconfig(libswscale)

Requires: kdelibs4%{?_isa} >= %{_kde4_version}

Provides: kffmpegthumbnailer = %{version}-%{release}
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
make install/fast -C %{_target_platform} DESTDIR=%{buildroot}


%files
%doc COPYING
%{_kde4_libdir}/kde4/ffmpegthumbs.so
%{_kde4_datadir}/kde4/services/ffmpegthumbs.desktop


%changelog
* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 4.13.97-2
- Rebuilt for FFmpeg 2.4.x

* Wed Aug 06 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.97-1
- 4.13.97

* Wed Aug 06 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.3-1
- 4.13.3

* Sat Mar 29 2014 Sérgio Basto <sergio@serjux.com> - 4.11.3-2
- Rebuilt for ffmpeg-2.2

* Wed Nov 27 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.3-1
- 4.11.3

* Tue Oct 01 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.1-1
- 4.11.1

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 4.10.1-3
- Rebuilt for FFmpeg 2.0.x

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 4.10.1-2
- Rebuilt for x264/FFmpeg

* Fri Apr 05 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.1-1
- 4.10.1

* Wed Jan 16 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.97-1
- 4.9.97

* Sat Nov 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 4.9.3-2
- Rebuilt for FFmpeg 1.0

* Thu Nov 08 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.3-1
- 4.9.3

* Wed Sep 12 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.1-1
- 4.9.1

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
