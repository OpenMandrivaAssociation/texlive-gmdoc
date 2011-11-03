# revision 21292
# category Package
# catalog-ctan /macros/latex/contrib/gmdoc
# catalog-date 2011-02-02 20:24:54 +0100
# catalog-license lppl
# catalog-version 0.993
Name:		texlive-gmdoc
Version:	0.993
Release:	1
Summary:	Documentation of LaTeX packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gmdoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmdoc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmdoc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A LaTeX package and an example class for documenting (La)TeX
packages, document classes, .dtx etc., providing hyperlinks.
The package is believed to be compatible with doc and permits
minimal markup of code (the macrocode environment is no longer
necessary). The package provides automatic detection of
definitions (detecting such things as \def, \newcommand,
\DeclareOption etc.). The package needs hyperref and the
author's three ''basic' packages: gmutils, gmverb and gmiflink.
As a bonus (and as an example of doc compatibility) driver
files are provided that may be used to typeset the LaTeX Base.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/gmdoc/gmglo.ist
%{_texmfdistdir}/tex/latex/gmdoc/gmdoc.sty
%{_texmfdistdir}/tex/latex/gmdoc/gmdocc.cls
%{_texmfdistdir}/tex/latex/gmdoc/gmoldcomm.sty
%doc %{_texmfdistdir}/doc/latex/gmdoc/README
%doc %{_texmfdistdir}/doc/latex/gmdoc/basedrivers/doc_gmdoc.tex
%doc %{_texmfdistdir}/doc/latex/gmdoc/basedrivers/docstrip_gmdoc.tex
%doc %{_texmfdistdir}/doc/latex/gmdoc/basedrivers/source2e_gmdoc.tex
%doc %{_texmfdistdir}/doc/latex/gmdoc/gmdoc.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
