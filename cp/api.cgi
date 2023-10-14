#!/usr/bin/perl
#
# Venue Info Handler - Captive Portal API (RFC 8908/8910)
#  API/CGI for Venue Information notification on Public Wi-Fi
#  to help users reach out to the web portal at the venue.
#  Target: Android, macOS, iOS/iPadOS
#
# 20231007 Hideaki Goto (Cityroam/eduroam)
# 20231015 Hideaki Goto (Cityroam/eduroam)
#
# Note:
#  This CGI relys on REMOTE_ADDR to discriminate each user device.
#  The system doesn't work over NAT.
#


require './capport.cfg';

use CGI;
use Redis;
use Digest::SHA qw(sha1 sha224 sha256 sha384 sha512);
use Digest::HMAC qw(hmac hmac_hex);


my $redis = Redis->new(server => 'localhost:6379') or die;
$redis->select($db_index);

my $q = CGI->new();
my $user_agent = $ENV{'HTTP_USER_AGENT'};

# for debugging
my $http_env='';
foreach $var (sort(keys(%ENV))) {
    $val = $ENV{$var};
    $val =~ s|\n|\\n|g;
    $val =~ s|"|\\"|g;
    $http_env .= "${var}=\"${val}\"\n";
}
$redis->set('ENV', $http_env); 

# Try to obtain client MAC address.
# This feature is for future use as it needs modification of DHCP server.
my $cli = '';
if ( defined $q->param('cli') ){ 
	$cli = $q->param('cli');
}

# Check whether popup is enforced (?cp=1 in URI).
my $captive_mode = 'false';
if ( defined $q->param('cp') ){ 
	if ( $q->param('cp') == '1' ){
		$captive_mode = 'true';
	}
}

my $ac = 0;	# 0: no auto click-through (for Android)

# For macOS, iOS, iPadOS, enforce popup and auto click-through.
# Note that Apple devices send out special HTTP_USER_AGENT
# without OS name.
if ( $user_agent =~ /CaptiveNetworkSupport/ ){
	$ac = 1;
	$captive_mode = 'true';
}


my $hmac = hmac_hex("$ENV{'REMOTE_ADDR'} $cli", $hashkey, \&sha256);
my $ukey = substr("$hmac", 0, 16);

if ( ! $redis->exists($ukey) ){
	$redis->set($ukey, '0', 'EX', $db_ttl, 'NX');
}
else{
	if ( $redis->get($ukey) > 0 ) {
		$captive_mode = 'false';
	}
}

# Block the Google's legacy mechanism.
my $hmac_gblock = hmac_hex("$ENV{'REMOTE_ADDR'}", $hashkey, \&sha256);
my $ukey_gblock = substr("$hmac_gblock", 0, 16);

$redis->set('Gb-'.$ukey_gblock, '0', 'EX', $db_ttl_gblock);


print <<EOS;
Cache-Control: private
Content-Type: application/captive+json

{
  "captive": $captive_mode,
  "user-portal-url": "$cp_url?accept=$ac&ukey=$ukey",
  "venue-info-url": "$venue_url"
}
EOS

1;
