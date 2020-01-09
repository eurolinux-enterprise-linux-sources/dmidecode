Summary:        Tool to analyse BIOS DMI data
Name:           dmidecode
Version:        3.1
Release:        2%{?dist}
Epoch:          1
Group:          System Environment/Base
License:        GPLv2+
Source0:        %{name}-%{version}.tar.xz
URL:            http://www.nongnu.org/dmidecode/
Patch0:         0001-dmidecode-Add-system-family-direct-string-option.patch
Patch1:         0002-Goodbye-CHANGELOG-welcome-NEWS.patch
Patch2:         0003-Fix-install-doc-target.patch
Patch3:         0004-biosdecode-Add-option-pir-full.patch
Patch4:         0005-biosdecode-Clean-up-the-PIR-table-output.patch
Patch5:         0006-biosdecode-Avoid-repeating-pointer-arithmetic.patch
Patch6:         0007-dmioem-Reflect-HPE-s-new-company-name.patch
Patch7:         0008-dmioem-Sort-vendor-names-alphabetically.patch
Patch8:         0009-UEFI-support-on-FreeBSD.patch
Patch9:         0010-dmidecode-Share-common-EFI-code.patch
Patch10:        0001-dmidecode-Fix-firmware-version-of-TPM-device.patch
Patch11:        0002-dmioem-decode-HPE-UEFI-type-219-Misc-Features.patch
Patch12:        0003-dmidecode-Use-lowercase-letters-for-UUID.patch

Buildroot:      %{_tmppath}/%{name}-%{version}-root
BuildRequires:  automake autoconf
ExclusiveArch:  %{ix86} x86_64 ia64 aarch64

%description
dmidecode reports information about x86 & ia64 hardware as described in the
system BIOS according to the SMBIOS/DMI standard. This information
typically includes system manufacturer, model name, serial number,
BIOS version, asset tag as well as a lot of other details of varying
level of interest and reliability depending on the manufacturer.

This will often include usage status for the CPU sockets, expansion
slots (e.g. AGP, PCI, ISA) and memory module slots, and the list of
I/O ports (e.g. serial, parallel, USB).

%prep
%setup -q
%patch0 -p1 -b .add_system_family
%patch1 -p1 -b .changelog_to_new
%patch2 -p1 -b .fix_install_doc
%patch3 -p1 -b .add_option_pir
%patch4 -p1 -b .clean_up_pir
%patch5 -p1 -b .avoid_repeating
%patch6 -p1 -b .reflect_hpe
%patch7 -p1 -b .sort_vendor_names
%patch8 -p1 -b .uefi_support_bsd
%patch9 -p1 -b .share_common_efi
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fPIE" LDFLAGS="-pie -Wl,-z,now"

%install
rm -rf ${buildroot}
make %{?_smp_mflags} DESTDIR=%{buildroot} prefix=%{_prefix} install-bin install-man

%clean
rm -rf ${buildroot}

%files
%doc AUTHORS NEWS README
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_sbindir}/dmidecode
%ifnarch ia64 aarch64
%{_sbindir}/vpddecode
%{_sbindir}/ownership
%{_sbindir}/biosdecode
%endif
%{_mandir}/man8/*

%changelog
* Thu Apr 26 2018 Lianbo Jiang <lijiang@redhat.com> - 1:3.1-1
- Sync with upstream
- Resolves: rhbz#1568227

* Wed May 3 2017 Petr Oros <poros@redhat.com> - 1:3.0-5
- Update compiler flags for hardened builds
- Resolves: #1420763

* Tue Feb 28 2017 Petr Oros <poros@redhat.com> - 1:3.0-4
- Sync with upstream
- Resolves: #1385884

* Tue Nov 8 2016 Petr Oros <poros@redhat.com> - 1:3.0-3
- Hide irrelevant fixup message
- Resolves: #1384195

* Wed Jun 29 2016 Petr Oros <poros@redhat.com> - 1:3.0-2
- Unmask LRDIMM in memmory type detail
- Resolves: #1321342

* Wed May 4 2016 Petr Oros <poros@redhat.com> - 1:3.0-1
- Update to upstream 3.0 release.
- Resolves: #1273487

* Mon Sep 21 2015 Petr Oros <poros@redhat.com> - 1:2.12-9
- dmioem: Decode Acer-specific DMI type 170
- dmioem: Decode HP-specific DMI types 212 and 219
- dmioem: Decode HP-specific DMI type 233, and refactored 209 and 221 to use a common function
- Resolves: #1232501

* Thu Jul 23 2015 Petr Oros <poros@redhat.com> - 1:2.12-8
- Support upstream sysfs filename for smbios entry point (Mark Salter)
- Resolves: #1232153

* Thu Jul 16 2015 Petr Oros <poros@redhat.com> - 1:2.12-7
- only use SMBIOS3 on aarch64 systems (Jeffrey Bastian)
- Resolves: #1242409

* Wed May 13 2015 Petr Oros <poros@redhat.com> - 1:2.12-6
- Add preliminary support for SMBIOS 64-bit entry point (Mark Salter)
- Add support for DDR4 memmory

* Fri Feb 21 2014 Anton Arapov <anton@redhat.com> - 2.12-5
- Spec file fixes for the Aarch64. (John Feeney )

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:2.12-4
- Mass rebuild 2013-12-27

* Thu May 09 2013 Anton Arapov <anton@redhat.com> - 1:2.12-3
- Accomodate few more necesary, to enable SMBIOS v2.8, changes from upstream.

* Fri Apr 26 2013 Anton Arapov <anton@redhat.com> - 1:2.12-2
- Fixup, so that it actually read SMBIOS 2.8.0 table.

* Wed Apr 17 2013 Anton Arapov <anton@redhat.com> - 1:2.12-1
- Update to upstream 2.12 release.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 26 2012 Anton Arapov <anton@redhat.com> - 1:2.11-8
- Update dmidecode.8 manpage

* Mon Mar 12 2012 Anton Arapov <anton@redhat.com> - 1:2.11-7
- Add "PXE" to HP OEM Type 209 record output
- Properly print the hexadecimal value of invalid string characters

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 14 2011 Anton Arapov <anton@redhat.com> - 1:2.11-5
- Fix the wrong call of the dmi_chassis_type function call. Thus fix
  an issue on the systems with the chassis lock available, application
  doesn't fall out with the out of spec error anymore.

* Tue May 03 2011 Anton Arapov <anton@redhat.com> - 1:2.11-4
- Update to SMBIOS 2.7.1
- Fix the boundaries check in type16

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 19 2011 Anton Arapov <anton@redhat.com> - 1:2.11-2
- Update to upstream 2.11 release. (#623047)

* Wed Jan 19 2011 Anton Arapov <anton@redhat.com> - 1:2.11-1
- Fix the changelog's NVR.

* Mon Nov 08 2010 Prarit Bhargava <prarit@redhat.com> - 1:2.10-3
- updated kernel.spec for review [BZ 225698]

* Fri Oct 15 2010 Anton Arapov <aarapov@redhat.com> - 1:2.10-2
- Does not build with gnu make v3.82+ (#631407)

* Fri Dec 18 2009 Prarit Bhargava <prarit@redhat.com> - 1:2.10-1.40
- Fix rpmlint errors in specfile

* Fri Aug 28 2009 Jarod Wilson <jarod@redhat.com> - 1:2.10-1.39
- Fix cache associativity mapping (was missing some commas)

* Mon Aug 24 2009 Jarod Wilson <jarod@redhat.com> - 1:2.10-1.38
- Add support for newer sockets, processors and pcie slot types

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.10-1.36.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 Matthias Clasen <mclasen@redhat.com>
- Build for i586

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.10-1.34.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 09 2009 Prarit Bhargava <prarit@redhat.com> 1:2.10
- rebuild with version 2.10

* Wed Jan 28 2009 Prarit Bhargava <prarit@redhat.com> 1:2.9-1.32
- fix Summary field (BZ 225698)

* Wed Jul 16 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1:2.9-1.30
- fix license tag

* Fri Mar 14 2008 Doug Chapman <doug.chapman@hp.com> 1:2.9-1.29.1
- Do not package vpddecode, ownership and biosdecode on ia64 since those are x86 only

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:2.9-1.27.1
- Autorebuild for GCC 4.3

* Mon Oct 22 2007 Prarit Bhargava <prarit@redhat.com> - 1:2.9
- rebuild with version 2.9
* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:2.7-1.25.1
- rebuild

* Thu Feb 09 2006 Dave Jones <davej@redhat.com>
- rebuild.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Nov 28 2005 Dave Jones <davej@redhat.com>
- Integrate several specfile cleanups from Robert Scheck. (#172543)

* Sat Sep 24 2005 Dave Jones <davej@redhat.com>
- Revert yesterdays patch, its unneeded in 2.7

* Fri Sep 23 2005 Dave Jones <davej@redhat.com>
- Don't try to modify areas mmap'd read-only.
- Don't build on ia64 any more.
  (It breaks on some boxes very badly, and works on very few).

* Mon Sep 12 2005 Dave Jones <davej@redhat.com>
- Update to upstream 2.7

* Fri Apr 15 2005 Florian La Roche <laroche@redhat.com>
- remove empty scripts

* Wed Mar  2 2005 Dave Jones <davej@redhat.com>
- Update to upstream 2.6

* Tue Mar  1 2005 Dave Jones <davej@redhat.com>
- Rebuild for gcc4

* Tue Feb  8 2005 Dave Jones <davej@redhat.com>
- Rebuild with -D_FORTIFY_SOURCE=2

* Tue Jan 11 2005 Dave Jones <davej@redhat.com>
- Add missing Obsoletes: kernel-utils

* Mon Jan 10 2005 Dave Jones <davej@redhat.com>
- Update to upstream 2.5 release.

* Sat Dec 18 2004 Dave Jones <davej@redhat.com>
- Initial packaging, based upon kernel-utils package.

