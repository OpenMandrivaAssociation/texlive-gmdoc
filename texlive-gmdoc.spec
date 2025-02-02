Name:		texlive-gmdoc
Version:	21292
Release:	2
Summary:	Documentation of LaTeX packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gmdoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmdoc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmdoc.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc %{buildroot}%{_texmfdistdir}
