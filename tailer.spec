Summary:	Tailer
Summary(pl):	Tailer
Name:		tailer
Version:	0.1
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	%{name}-%{version}.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tailer is a simple utility for writting output of executed 
applications to file and screen at the same time.

%description -l pl
Tailer to proste narzêdzie do zapisywanie wyjscia z wykonywanych
aplikacji do pliku i na ekran jednoczesnie.

%prep
%setup -q

%build
gcc -Wall -g02 tailer.c -o tailer

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_bindir}
install tailer $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
