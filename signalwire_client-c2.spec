Name:		signalwire-client-c2
Version:	2.0.0
Release:	1%{?dist}
Summary:	SignalWire's C client

Group:		Libraries/C and C++
License:	MIT
URL:		https://signalwire.com/
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	cmake, libks2-devel, openssl-devel, libatomic, libuuid-devel
Requires:	libks2, openssl-libs, libatomic, libuuid

%description
SignalWire C Client Libarry

%package devel
Summary:	Development package for SignalWire's C client
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development package for SignalWire's C client

%prep
%setup -q


%build
#configure
cmake . -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}


%install
%make_install


%files
/usr/lib64/libsignalwire_client*.so.*
%doc
/usr/share/doc/signalwire-client-c2/copyright

%files devel
/usr/include/*
/usr/lib64/lib*so
/usr/lib64/pkgconfig/signalwire_client2.pc


%changelog

