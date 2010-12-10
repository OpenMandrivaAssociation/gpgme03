%define rel 10
%define version 0.3.16
%define release %mkrel %{rel} 
%define Rname gpgme
 
%define req_gnupg_version gnupg2-1.9.3

%define major 6
%define libname %mklibname %name

Summary:	GnuPG Made Easy (GPGME)
Name:		%{Rname}03
Version:	%{version}
Release:	%{release}
Source0:	ftp://ftp.gnupg.org/gcrypt/%{Rname}/%{Rname}-%{version}.tar.gz
Source1:	ftp://ftp.gnupg.org/gcrypt/%{Rname}/%{Rname}-%{version}.tar.gz.sig
License:	GPL
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{Rname}-%{version}-%{release}-buildroot
URL:		http://www.gnupg.org/gpgme.html 
BuildRequires:	gnupg >= %{req_gnupg_version}

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications.

%package	-n %{libname}_%{major}
Summary:	GnuPG Made Easy (GPGME)
Group:		System/Libraries
Requires:	gnupg >= %{req_gnupg_version}  
Provides:	%{libname} = %{version}-%{release}
Provides:	%{Rname} = %{version}-%{release} 
 

%description	-n %{libname}_%{major} 
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications.

%package	-n %{libname}_%{major}-devel
Summary:	GnuPG Made Easy (GPGME) Header files and libraries for development
Group:		Development/C
Requires:	%{libname}_%{major} = %{version}-%{release}
Provides:	lib%{Rname}-devel = %{version}-%{release}
Provides:	%{libname}-devel = %{version}-%{release} 
Conflicts:       %{Rname}-devel > %{version}
 
 
%description	-n %{libname}_%{major}-devel
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications.

Install the gpgme-devel package if you want to develop applications 
that will use the gpgme library.

%prep
%setup -q -n %{Rname}-%{version}

%build
%configure2_5x
%make
##CAE build now hangsif this is run
##%__make check

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%if %mdkversion < 200900
%post -n %{libname}_%{major} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname}_%{major} -p /sbin/ldconfig
%endif

%post -n %{libname}_%{major}-devel
%_install_info %rname.info

%postun -n %{libname}_%{major}-devel
%_remove_install_info %rname.info


%files -n %{libname}_%{major}
%defattr(-,root,root)
%{_libdir}/libgpgme.so.*

%files -n %{libname}_%{major}-devel
%defattr(-,root,root)
%doc README README-alpha TODO ChangeLog NEWS AUTHORS COPYING THANKS
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so

%{_bindir}/gpgme-config
%{_datadir}/aclocal/*
%{_includedir}/*
%{_infodir}/gpgme.info*

