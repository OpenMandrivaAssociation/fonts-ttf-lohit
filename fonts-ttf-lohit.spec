Name:        fonts-ttf-lohit
Version:     2.3.8
Release:     %mkrel 7
Summary:     Free Indian truetype/opentype fonts

Group:       System/Fonts/True type
License:     GPLv2
URL:         http://fedoraproject.org/wiki/Lohit
Source:      http://rbhalera.fedorapeople.org/released/lohit/lohit-fonts-%{version}.tar.gz
BuildArch:   noarch
BuildRequires: fontconfig
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

%files 
%defattr(-, root, root, -) 
%doc COPYING README AUTHORS 
%{_datadir}/fonts/TTF/*


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 2.3.8-6mdv2011.0
+ Revision: 675422
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 2.3.8-5
+ Revision: 675186
- rebuild for new rpm-setup

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.3.8-4
+ Revision: 664335
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3.8-3mdv2011.0
+ Revision: 605201
- rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 2.3.8-2mdv2010.1
+ Revision: 494153
- fc-cache is now called by an rpm filetrigger

* Mon Mar 23 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 2.3.8-1mdv2009.1
+ Revision: 360563
- Updated to version 2.3.8

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.3.1-2mdv2009.1
+ Revision: 351097
- rebuild

* Sat Sep 27 2008 Frederic Crozat <fcrozat@mandriva.com> 2.3.1-1mdv2009.0
+ Revision: 288923
- import fonts-ttf-lohit


