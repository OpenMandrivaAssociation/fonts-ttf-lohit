Name:        fonts-ttf-lohit
Version:     2.3.1
Release:     %mkrel 1
Summary:     Free Indian truetype/opentype fonts

Group:       System/Fonts/True type
License:     GPLv2
URL:         http://fedoraproject.org/wiki/Lohit
Source:      http://rbhalera.fedorapeople.org/released/lohit/lohit-fonts-%{version}.tar.gz
BuildArch:   noarch
BuildRoot:   %{_tmppath}/%{name}-%{version}-%{release}-root
Obsoletes:   fonts-ttf-gurmukhi <= 1.0
Provides:    fonts-ttf-gurmukhi = %{version}-%{release}

%description 
This package provides Hindi, Bengali, Gujarati, Punjabi, Tamil,
Kannada, Malayalam, Oriya, Telugu, Marathi, Maithili, Kashmiri, 
Konkani, Nepali and Sindhi TrueType/Opentype fonts.

%prep
%setup -q -n lohit-fonts-%{version}

%build
echo "Nothing to do in Build."

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_datadir}/fonts/TTF/lohit
for i in *
do
  [ -d $i ] || continue
  install -m 0644 $i/* $RPM_BUILD_ROOT/%{_datadir}/fonts/TTF/lohit
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 

%postun
if [ "$1" = "0" ]; then
  [ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 
fi

%files 
%defattr(-, root, root, -) 
%doc COPYING README AUTHORS 
%{_datadir}/fonts/TTF/*
