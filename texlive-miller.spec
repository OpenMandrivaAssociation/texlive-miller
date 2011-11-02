Name:		texlive-miller
Version:	1.2
Release:	1
Summary:	Typeset miller indices
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/miller
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/miller.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/miller.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/miller.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Typeset miller indices, e.g., <1-20>, that are used in material
science with an easy syntax. Minus signs are printed as bar
above the corresponding number.

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
%{_texmfdistdir}/tex/latex/miller/miller.sty
%doc %{_texmfdistdir}/doc/latex/miller/ChangeLog
%doc %{_texmfdistdir}/doc/latex/miller/Makefile
%doc %{_texmfdistdir}/doc/latex/miller/README
%doc %{_texmfdistdir}/doc/latex/miller/miller-v.tex
%doc %{_texmfdistdir}/doc/latex/miller/miller.pdf
%doc %{_texmfdistdir}/doc/latex/miller/millertest.tex
#- source
%doc %{_texmfdistdir}/source/latex/miller/miller.dtx
%doc %{_texmfdistdir}/source/latex/miller/miller.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
