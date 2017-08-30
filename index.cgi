#!/usr/bin/perl -w

use strict;
use warnings;
use CGI qw(:cgi-lib :escapeHTML :unescapeHTML);
use Data::Dumper;


sub dbConnect
{
	my $dbh = DBI->connect('dbi:mysql:user1','user1','tuser1');
	return $dbh;
}

sub getData
{
	my $self = $_[0];	
	my $dbh = $self->dbConnect;
	my $sth = $dbh->prepare("Select id_article, id_user, title, content, date_insert, from journal_articles;");
	$sth->execute();

	my $data = {};

	while (my $row = $sth->fetchrow_hashref())
	{
		$data->{$row->{'id_article'}}{id_user} = $row->{'id_user'};
		$data->{$row->{'id_article'}}{title} = $row->{'title'};
		$data->{$row->{'id_article'}}{content} = $row->{'content'};
		$data->{$row->{'id_article'}}{date_insert} = $row->{'date_insert'};
	}
		
	$sth->finish();
	$dbh->disconnect();
	return $data;
}


print "Content-type: text/html; charset=utf-8\n\n";
print '<pre>'.Dumper(\%ENV).'</pre>';


$|=1; # ÏÔËÌÀÞÁÅÍ ÂÕÆÅÒÉÚÁÃÉÀ ××ÏÄÁ ÄÁÎÎÙÈ;
ReadParse(); # ÐÏÌÕÞÁÅÔ ÄÁÎÎÙÅ ÉÚ HTML ÆÏÒÍÙ ×  ÈÜÛ %in

use vars qw(%in);
print '<pre>'.Dumper(\%in).'</pre>';







