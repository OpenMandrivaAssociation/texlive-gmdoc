%global tl_name gmdoc
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.993
Release:	%{tl_revision}.1
Summary:	Documentation of LaTeX packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gmdoc
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gmdoc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gmdoc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A LaTeX package and an example class for documenting (La)TeX packages,
document classes, .dtx etc., providing hyperlinks. The package is
believed to be compatible with doc and permits minimal markup of code
(the macrocode environment is no longer necessary). The package provides
automatic detection of definitions (detecting such things as \def,
\newcommand, \DeclareOption etc.). The package needs hyperref and the
author's three 'basic' packages: gmutils, gmverb and gmiflink. As a
bonus (and as an example of doc compatibility) driver files are provided
that may be used to typeset the LaTeX Base.

