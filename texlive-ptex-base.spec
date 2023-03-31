Name:		texlive-ptex-base
Version:	64072
Release:	2
Summary:	Plain TeX format for pTeX and e-pTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ptex-base
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex-base.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex-base.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle contains the plain TeX format for pTeX and e-pTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/ptex/ptex-base
%doc %{_texmfdistdir}/doc/ptex/ptex-base

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
