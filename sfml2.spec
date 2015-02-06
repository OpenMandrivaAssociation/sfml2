%define	major		2
%define	minor		0

%define	libname_a	%mklibname %{name}-audio %{major}.%{minor}
%define	libname_g	%mklibname %{name}-graphics %{major}.%{minor}
%define	libname_n	%mklibname %{name}-network %{major}.%{minor}
%define	libname_s	%mklibname %{name}-system %{major}.%{minor}
%define	libname_w	%mklibname %{name}-window %{major}.%{minor}
%define	devname		%mklibname %{name} -d

Summary:	Simple and Fast Multimedia Library
Name:		sfml2
Version:	2.0
Release:	3
License:	zlib/libpng License
Group:		System/Libraries
Url:		http://sourceforge.net/projects/sfml
# Use git snapshot
Source0:	%{name}-%{version}.tar.bz2
Patch0:		sfml2-2.0-dont_install_docs.patch
Patch1:		sfml2-2.0-gcc4.7.patch
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xrandr)

%description
SFML is a portable and easy to use multimedia API written in C++.

Its features are :
 - portability,
 - object-oriented design,
 - flexibility (a lot of small packages),
 - easy to use,
 - easy to integrate with GUI toolkits.

The library is divided in 5 small packages :
 - audio
 - graphics
 - network
 - system
 - window

%files
%defattr(0644,root,root,0755)
%doc readme.txt license.txt

#----------------------------------------------------------------------------

%package -n %{libname_a}
Summary:	Dynamic libraries from %{name}-audio
Group:		System/Libraries
Provides:	%{name}-audio = %{EVRD}

%description -n %{libname_a}
Dynamic libraries from %{name}-audio.

%files -n %{libname_a}
%{_libdir}/libsfml-audio.so.%{major}
%{_libdir}/libsfml-audio.so.%{major}.%{minor}

#----------------------------------------------------------------------------

%package -n %{libname_g}
Summary:	Dynamic libraries from %{name}-graphics
Group:		System/Libraries
Provides:	%{name}-graphics = %{EVRD}

%description -n %{libname_g}
Dynamic libraries from %{name}-graphics.

%files -n %{libname_g}
%{_libdir}/libsfml-graphics.so.%{major}
%{_libdir}/libsfml-graphics.so.%{major}.%{minor}

#----------------------------------------------------------------------------

%package -n %{libname_n}
Summary:	Dynamic libraries from %{name}-network
Group:		System/Libraries
Provides:	%{name}-network = %{EVRD}

%description -n %{libname_n}
Dynamic libraries from %{name}-network.

%files -n %{libname_n}
%{_libdir}/libsfml-network.so.%{major}
%{_libdir}/libsfml-network.so.%{major}.%{minor}

#----------------------------------------------------------------------------

%package -n %{libname_s}
Summary:	Dynamic libraries from %{name}-system
Group:		System/Libraries
Provides:	%{name}-system = %{EVRD}

%description -n %{libname_s}
Dynamic libraries from %{name}-system.

%files -n %{libname_s}
%{_libdir}/libsfml-system.so.%{major}
%{_libdir}/libsfml-system.so.%{major}.%{minor}

#----------------------------------------------------------------------------

%package -n %{libname_w}
Summary:	Dynamic libraries from %{name}-window
Group:		System/Libraries
Provides:	%{name}-window = %{EVRD}

%description -n %{libname_w}
Dynamic libraries from %{name}-window.

%files -n %{libname_w}
%{_libdir}/libsfml-window.so.%{major}
%{_libdir}/libsfml-window.so.%{major}.%{minor}

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Header and .so files for %{name}
Group:		Development/C++
Requires:	%{name}-audio = %{EVRD}
Requires:	%{name}-graphics = %{EVRD}
Requires:	%{name}-network = %{EVRD}
Requires:	%{name}-system = %{EVRD}
Requires:	%{name}-window = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	libsfml-audio-devel < %{version}
Conflicts:	libsfml-graphics-devel < %{version}
Conflicts:	libsfml-network-devel < %{version}
Conflicts:	libsfml-system-devel < %{version}
Conflicts:	libsfml-window-devel < %{version}

%description -n %{devname}
Includes files for developing programs based on %{name}.

%files -n %{devname}
%defattr(0644,root,root,0755)
%{_includedir}/SFML
%{_libdir}/libsfml-*.so
%{_datadir}/cmake/Modules/*.cmake

#----------------------------------------------------------------------------

%package doc
Summary:	Documenation for %{name}
Group:		Books/Computer books
BuildArch:	noarch

%description doc
Documenation for %{name}.

%files doc
%defattr(0644,root,root,0755)
%doc build/doc/html examples

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake -DBUILD_DOC=TRUE
%make
%make doc

%install
%makeinstall_std -C build

