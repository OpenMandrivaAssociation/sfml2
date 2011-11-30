%define	major		2
%define	minor		0

%define	libname_a	%mklibname %{name}-audio %{major}.%{minor}
%define	libname_g	%mklibname %{name}-graphics %{major}.%{minor}
%define	libname_n	%mklibname %{name}-network %{major}.%{minor}
%define	libname_s	%mklibname %{name}-system %{major}.%{minor}
%define	libname_w	%mklibname %{name}-window %{major}.%{minor}
%define	develname	%mklibname %{name} -d

Name:		sfml2
Version:	2.0
Release:	%mkrel 0.1
Summary:	Simple and Fast Multimedia Library
License:	zlib/libpng License
Group:		System/Libraries
URL:		http://sourceforge.net/projects/sfml
# Use git snapshot
Source0:	%{name}-%{version}.tar.bz2
Patch0:		sfml2-2.0-dont_install_docs.patch
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
BuildRequires:	glew-devel
BuildRequires:	freetype2-devel
BuildRequires:	libx11-devel
BuildRequires:	libxrandr-devel
BuildRequires:	openal-devel
BuildRequires:	sndfile-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

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

########################################################

%package -n %{develname}
Summary:	Header and .so files for %{name}
Group:		Development/C++
Requires:	%{name}-audio = %{version}-%{release}
Requires:	%{name}-graphics = %{version}-%{release}
Requires:	%{name}-network = %{version}-%{release}
Requires:	%{name}-system = %{version}-%{release}
Requires:	%{name}-window = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	libsfml-audio-devel < %{version}
Conflicts:	libsfml-graphics-devel < %{version}
Conflicts:	libsfml-network-devel < %{version}
Conflicts:	libsfml-system-devel < %{version}
Conflicts:	libsfml-window-devel < %{version}

%description -n %{develname}
Includes files for developing programs based on %{name}.

%package -n %{libname_a}
Summary:	Dynamic libraries from %{name}-audio
Group:		System/Libraries
Provides:	%{name}-audio = %{version}-%{release}

%description -n %{libname_a}
Dynamic libraries from %{name}-audio.

%package -n %{libname_g}
Summary:	Dynamic libraries from %{name}-graphics
Group:		System/Libraries
Provides:	%{name}-graphics = %{version}-%{release}

%description -n %{libname_g}
Dynamic libraries from %{name}-graphics.

%package -n %{libname_n}
Summary:	Dynamic libraries from %{name}-network
Group:		System/Libraries
Provides:	%{name}-network = %{version}-%{release}

%description -n %{libname_n}
Dynamic libraries from %{name}-network.

%package -n %{libname_s}
Summary:	Dynamic libraries from %{name}-system
Group:		System/Libraries
Provides:	%{name}-system = %{version}-%{release}

%description -n %{libname_s}
Dynamic libraries from %{name}-system.

%package -n %{libname_w}
Summary:	Dynamic libraries from %{name}-window
Group:		System/Libraries
Provides:	%{name}-window = %{version}-%{release}

%description -n %{libname_w}
Dynamic libraries from %{name}-window.

%package	doc
Summary:	Documenation for %{name}
Group:		Books/Computer books
BuildArch:	noarch

%description	doc
Documenation for %{name}.

########################################################

%prep
%setup -q
%patch0 -p1

%build
%cmake -DBUILD_DOC=TRUE
%make
%make doc

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc readme.txt license.txt

%files -n %{develname}
%defattr(0644,root,root,0755)
%{_includedir}/SFML
%{_libdir}/libsfml-*.so
%{_datadir}/cmake/Modules/*.cmake

%files -n %{libname_a}
%defattr(0644,root,root,0755)
%{_libdir}/libsfml-audio.so.%{major}
%{_libdir}/libsfml-audio.so.%{major}.%{minor}

%files -n %{libname_g}
%defattr(0644,root,root,0755)
%{_libdir}/libsfml-graphics.so.%{major}
%{_libdir}/libsfml-graphics.so.%{major}.%{minor}

%files -n %{libname_n}
%defattr(0644,root,root,0755)
%{_libdir}/libsfml-network.so.%{major}
%{_libdir}/libsfml-network.so.%{major}.%{minor}

%files -n %{libname_s}
%defattr(0644,root,root,0755)
%{_libdir}/libsfml-system.so.%{major}
%{_libdir}/libsfml-system.so.%{major}.%{minor}

%files -n %{libname_w}
%defattr(0644,root,root,0755)
%{_libdir}/libsfml-window.so.%{major}
%{_libdir}/libsfml-window.so.%{major}.%{minor}

%files doc
%defattr(0644,root,root,0755)
%doc build/doc/html examples

