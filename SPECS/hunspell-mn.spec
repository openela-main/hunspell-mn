Name: hunspell-mn
Summary: Mongolian hunspell dictionaries
%global upstreamid 20080709
Version: 0.%{upstreamid}
Release: 16%{?dist}
# Another Upstream https://extensions.openoffice.org/en/project/mongolian-spell-checking-dictionary
# gives below Source URL
Source: https://downloads.sourceforge.net/project/aoo-extensions/1408/0/dict-mn_0.06-5.oxt 
URL: http://mnspell.openmn.org
License: GPLv2
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-mn)

%description
Mongolian hunspell dictionaries.

%prep
%autosetup -c -n hunspell-mn

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p mn_MN.* $RPM_BUILD_ROOT/%{_datadir}/myspell/


%files
%doc README_mn_MN.txt
%{_datadir}/myspell/*

%changelog
* Sun Jul 08 2018 Parag Nemade <pnemade AT fedoraproject DOT org> - 0.20080709-16
- Update Source tag
- Drop LGPLv2+ as we are not installing hyphenation rules

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080709-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080709-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080709-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 19 2016 Parag Nemade <pnemade AT redhat DOT com> - 0.20080709-12
- Add Supplements: tag for langpacks naming guidelines
- Clean the specfile to follow current packaging guidelines

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080709-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080709-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080709-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080709-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080709-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 05 2012 Caolan McNamara <caolanm@redhat.com> - 0.20080709-6
- uninstalled hyphenation patterns are under unversioned LGPLv2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080709-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080709-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080709-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080709-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 03 2009 Caolan McNamara <caolanm@redhat.com> - 0.20080709.1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 28 2008 Caolan McNamara <caolanm@redhat.com> - 0.60.2-1
- initial version
