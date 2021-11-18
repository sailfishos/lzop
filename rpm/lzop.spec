Name:           lzop
Version:        1.04
Release:        0
Summary:        The fastest compressor and decompressor around
License:        GPLv2+
Source:         lzop-%{version}.tar.gz
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

%package doc
Summary:        LZOP documentation
Requires:       lzop = %{version}-%{release}

%description doc
lzop documentation. Man pages and html docs.

%prep
%setup -q

%build
export CPPFLAGS="-I/usr/include/lzo"
export LDFLAGS="-L%{_libdir}"
%configure
%make_build

%install
%makeinstall

%files
%defattr(-,root,root)
%license COPYING
%{_bindir}/lzop

%files doc
%defattr(-,root,root)
%{_docdir}/lzop
%doc %{_mandir}/man1/lzop.1*

