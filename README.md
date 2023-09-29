# VenueInfoHelper
API/CGI for presenting Venue Information on Public Wi-Fi to help users reach out to the web portal at the venue.

This helper is specialized for Venue Information display rather than Captive Portal that blocks the network usage. There is no access control at all. Our intention is to improve user engagement while allowing people to use the network continuously and seamlessly.

## Specifications
- CAPPORT API (RFC 8908, 8910) is the primary.
- Support (partly) Apple's legacy Captive Portal mechanism (CNA, Captive Network Assistant).
- Usable with Open, PSK, 802.1X, and Passpoint networks.

## Requirements
- Redis
- Perl
- HTTP server
- DNS server

## Limitations
- (Disturbing) Captive Portal is enforced on Apple devices since they haven't got a nice notification mechanism.
- No support for Windows 10/11 so far.

