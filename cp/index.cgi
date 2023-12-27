#!/usr/bin/perl
#
# Venue Info Handler - Splash page for Captive Portal API
#  API/CGI for Venue Information notification on Public Wi-Fi
#  to help users reach out to the web portal at the venue.
#  Target: Android, macOS, iOS/iPadOS
#
# 20231007 Hideaki Goto (Cityroam/eduroam)
# 20231015 Hideaki Goto (Cityroam/eduroam)
# 20231228 Hideaki Goto (Cityroam/eduroam)
#	Fixed HTML.
#
# Note:
#  Customize the splash page contents in this file.
#

require './capport.cfg';

use CGI;
use Redis;

my $redis = Redis->new(server => 'localhost:6379') or die;
$redis->select($db_index);

my $q = CGI->new();

my $accepted = 0;
my $ukey = 'void';
if ( ! defined $q->param('ukey') ){	# check the given user key

print <<EOS;
Content-Type: text/html

<html>
<head></head>
<body>
<font size="+2">
Please turn off Wi-Fi once and try again from turning it on.
</font>
</body>
</html>
EOS

}

else{
	$ukey = $q->param('ukey');
	if ( defined $q->param('accept') ){
		if ( $q->param('accept') == '1' ){
			$redis->set($ukey, '1', 'EX', $db_ttl);
			$accepted = 1;
		}
	}

if ( ! $accepted ){

# first display before tap
print <<EOS;
Content-Type: text/html

<html>
<head></head>
<body>
<div style="text-align: center">
<img alt="venue logo" src="$logo_file">
</div>
<br><br>
<div style="text-align: center">
<button type="button" onclick="location.href='./?accept=1&ukey=$ukey'">
<font size="+2">Got it</font></button>
</div>
</body>
</html>
EOS
}

else{

# second display after tapping
print <<EOS;
Content-Type: text/html

<html>
<head></head>
<body>
<div style="text-align: center">
<a href="$venue_url">
<img alt="venue logo" src="$logo_file">
</a>
</div>
<br><br>
<div style="text-align: center">
<font size="+2"><a href="$venue_url">Go to portal</a></font>
</div>
</body>
</html>
EOS
}

}

1;
