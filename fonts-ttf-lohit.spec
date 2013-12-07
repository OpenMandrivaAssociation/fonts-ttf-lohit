Summary:	Free Indian truetype/opentype fonts
Name:		fonts-ttf-lohit
Version:	2.3.8
Release:	11
Group:		System/Fonts/True type
License:	GPLv2
Url:		http://fedoraproject.org/wiki/Lohit
Source0:	http://rbhalera.fedorapeople.org/released/lohit/lohit-fonts-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	fontconfig

%description 
This package provides Hindi, Bengali, Gujarati, Punjabi, Tamil,
Kannada, Malayalam, Oriya, Telugu, Marathi, Maithili, Kashmiri, 
Konkani, Nepali and Sindhi TrueType/Opentype fonts.

%prep
%setup -qn lohit-fonts-%{version}

%build
echo "Nothing to do in Build."

%install
install -d %{buildroot}/%{_datadir}/fonts/TTF/lohit
for i in *
do
  [ -d $i ] || continue
  install -m 0644 $i/* %{buildroot}/%{_datadir}/fonts/TTF/lohit
done

%files 
%doc COPYING README AUTHORS 
%{_datadir}/fonts/TTF/*

