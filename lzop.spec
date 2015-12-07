Name:           lzop
Version:        1.03
Release:        0
Summary:        The fastest compressor and decompressor around
License:        GPLv2+
Group:          Development/Tools
Source:         lzop-%{version}.tar.gz
Source1:        _src
Url:            http://www.lzop.org
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libtool
BuildRequires:  lzo-devel
BuildRequires:  make

%description
lzop is a file compressor similar to gzip. Its main advantages over gzip
are much higher compression and decompression speed at the cost
of compression ratio.

lzop was designed with the following goals in mind:
- speed (both compression and decompression)
- reasonable drop-in compatibility to gzip
- portability

%prep
%setup -q

%build
export CPPFLAGS="-I/usr/include/lzo"
export LDFLAGS="-L%{_libdir}"
%configure
%__make %{?jobs:-j%{jobs}}

%install
%makeinstall

%clean
%__rm -rf "%{buildroot}"

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS
%{_bindir}/lzop
%doc %{_mandir}/man1/lzop.1*
